"""Messdaten des Anno-Monitors für die öffentliche Seite verdichten und von Privatem befreien.

Reine Funktionen ohne Zugriff auf den Monitor, damit sie auch in der GitHub-Prüfung laufen;
`publish-monitor.py` liest die Quellen und schreibt die Dateien.

Öffentlich werden nur gültige Messungen (verworfene Abschnitte nach einem Neuladen bleiben weg),
nur die eigenen Inseln und keine Pfade, Dateinamen, Prüfsummen oder Kontokennungen.
"""

from __future__ import annotations

import json
import re

SCHEMA = 1

# Laufwerkspfade (ohne „https:/“), Benutzer- und Dokumentenordner, Kontoordner, Kennungen im GUID-Format
PRIVAT = re.compile(
    r"(?<![A-Za-z])[A-Za-z]:[\\/]|/(?:Users|home)/|\baccounts\b|Dokumente|Documents|"
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    re.I,
)

KURZ_FELDER = ("mid", "quelle", "erfasst_um", "spielzeit_ms", "geld", "bilanz", "einnahmen", "ausgaben",
               "bevoelkerung", "je_stufe", "inseln")
EREIGNIS_FELDER = ("mid", "art", "text", "spielzeit_ms", "erfasst_um", "quelle", "insel", "stufe", "ware", "betrieb",
                   "entscheidung", "wahl", "seit_ms", "spielzeit_stand_ms", "erstmals", "teilnehmer", "vorher",
                   "provinz", "anzahl", "neu", "forschung", "beginn", "auftrag", "auftrag_id", "gott",
                   "hingabe_stufe")
# Nur lokal im Monitor: technische Neuladen-Zeilen, Ereignisfenster (datieren Entscheidungen) und Bildschirmfotos
LOKALE_ARTEN = {"neuladen", "verworfen", "fenster", "bildschirmfoto"}
INSEL_FELDER = ("id", "name", "provinz", "bewohner", "haeuser", "grundsteuer", "stufen", "beduerfnisse", "betriebe",
                "status", "aus_spielstand", "religion")
RIVALEN_FELDER = ("id", "name", "attribute", "geld_je_minute", "hoechststand_je_stufe", "inseln")


def json_bytes(obj) -> bytes:
    """Gleicher Inhalt ergibt gleiche Bytes: Unveränderte Dateien erscheinen in keinem Commit."""
    return (json.dumps(obj, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def privat_funde(obj, pfad: str = "") -> list[str]:
    """Stellen (Schlüssel oder Text), die nach Pfad, Konto oder Benutzerordner aussehen."""
    funde: list[str] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(k, str) and PRIVAT.search(k):
                funde.append(f"{pfad}/{k} (Schlüssel)")
            funde += privat_funde(v, f"{pfad}/{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            funde += privat_funde(v, f"{pfad}[{i}]")
    elif isinstance(obj, str) and PRIVAT.search(obj):
        funde.append(f"{pfad}: {obj[:60]}")
    return funde


def kurz(k: dict) -> dict:
    """Kurzwerte einer Messung (Zeile aus messungen.jsonl des Monitors) ohne Dateinamen und Prüfsumme."""
    return {f: k[f] for f in KURZ_FELDER if k.get(f) is not None}


def oeffentlich(e: dict) -> bool:
    """Gehört diese Chronikzeile des Monitors auf die öffentliche Seite?"""
    return e.get("art") not in LOKALE_ARTEN


def ereignis(e: dict, umbenannt: dict | None = None) -> dict:
    """Chronikzeile des Monitors; umbenannte Inseln mit dem Namen aus dem Spiel."""
    out = {f: e[f] for f in EREIGNIS_FELDER if e.get(f) is not None}
    for alt, neu in (umbenannt or {}).items():
        if alt and neu and alt in out.get("text", ""):
            out["text"] = out["text"].replace(alt, neu)
    return out


def _ohne_nullen(d: dict | None) -> dict:
    return {k: v for k, v in (d or {}).items() if v not in (0, 0.0, None)}


def _insel(i: dict) -> dict:
    e = {f: i[f] for f in INSEL_FELDER if i.get(f) is not None}
    e["lager"] = _ohne_nullen(i.get("lager"))
    s = i.get("statistik")
    if isinstance(s, dict):  # nur der letzte Schnappschuss der Spielstatistik
        e["statistik"] = {k: s[k] for k in ("zeit_ms", "erzeugung", "verbrauch") if k in s}
    return e


def stand(m: dict, katalog: dict | None = None) -> dict:
    """Letzter Stand der Partie: eigene Inseln, Geld, Bevölkerung, Rivalen; dazu die deutschen Namen."""
    welt = m.get("welt") or {}
    out = {
        "schema": SCHEMA,
        "mid": m.get("mid"),
        "quelle": m.get("quelle"),
        "erfasst_um": m.get("erfasst_um"),
        "spielzeit_ms": m.get("spielzeit_ms"),
        "welt": {k: welt[k] for k in ("id", "name", "seed", "schwierigkeit", "dlcs") if welt.get(k) is not None},
        "geld": m.get("geld"),
        "geld_je_minute": m.get("geld_je_minute"),
        "bevoelkerung": m.get("bevoelkerung"),
        "attribute": m.get("attribute"),
        "provinzen": m.get("provinzen"),
        "aktive_provinz": m.get("aktive_provinz"),
        "inseln": [_insel(i) for i in m.get("inseln") or [] if i.get("eigene")],
        "rivalen": [{k: r[k] for k in RIVALEN_FELDER if r.get(k) is not None} for r in m.get("rivalen") or []],
    }
    if isinstance(m.get("forschung"), dict):  # Spieler und Praetoren: abgeschlossen, laufend, vorgemerkt
        out["forschung"] = {pid: {k: f.get(k) or [] for k in ("fertig", "laeuft", "warteschlange")}
                            for pid, f in m["forschung"].items()}
    if isinstance(m.get("auftraege"), list):
        out["auftraege"] = [{k: e[k] for k in ("auftrag", "erledigt", "vertrag", "provinz", "gegenueber") if k in e}
                            for e in m["auftraege"]]
    if isinstance(m.get("religion"), dict):  # gesammelte Hingabe je Teilnehmer und Gottheit
        out["religion"] = m["religion"]
    erg = m.get("ergaenzt_aus")
    if isinstance(erg, dict):  # ohne Dateinamen des Spielstands
        out["ergaenzt_aus"] = {k: erg[k] for k in ("spielzeit_ms", "gespeichert_um") if erg.get(k) is not None}
    out = {k: v for k, v in out.items() if v not in (None, [], {})}
    if katalog:
        out["namen"] = namen(out, katalog)
    return out


def namen(s: dict, katalog: dict) -> dict:
    """Deutsche Namen der Stufen, Waren und Betriebe, die im Stand vorkommen (aus dem Spielkatalog)."""
    stufen, waren, betriebe = set(), set(), set()
    bev = s.get("bevoelkerung") or {}
    for teil in ("je_stufe", "hoechststand_je_stufe"):
        stufen.update(bev.get(teil) or {})
    for i in s.get("inseln") or []:
        stufen.update(i.get("stufen") or {})
        for stufe, bed in (i.get("beduerfnisse") or {}).items():
            stufen.add(stufe)
            waren.update(bed or {})
        waren.update(i.get("lager") or {})
        st = i.get("statistik") or {}
        waren.update(st.get("erzeugung") or {})
        waren.update(st.get("verbrauch") or {})
        betriebe.update(i.get("betriebe") or {})

    def nachschlagen(teil: str, kennungen: set) -> dict:
        tabelle = katalog.get(teil) or {}
        out = {}
        for g in sorted(kennungen, key=lambda x: int(x) if str(x).isdigit() else 0):
            e = tabelle.get(str(g)) or {}
            if e.get("text") or e.get("name"):
                out[str(g)] = e.get("text") or e.get("name")
        return out

    forschungen, goetter, auftraege = set(), set(), set()
    for f in (s.get("forschung") or {}).values():
        for k in ("fertig", "laeuft", "warteschlange"):
            forschungen.update(f.get(k) or [])
    for verehrt in (s.get("religion") or {}).values():
        goetter.update(verehrt or {})
    for i in s.get("inseln") or []:
        if (i.get("religion") or {}).get("gott"):
            goetter.add(i["religion"]["gott"])
    for e in s.get("auftraege") or []:
        auftraege.add(e.get("auftrag"))
    return {"stufen": nachschlagen("stufen", stufen), "waren": nachschlagen("produkte", waren),
            "betriebe": nachschlagen("betriebe", betriebe), "forschungen": nachschlagen("forschungen", forschungen),
            "goetter": nachschlagen("goetter", goetter), "auftraege": nachschlagen("auftraege", auftraege)}


def nach_tagen(messungen: list[dict], ereignisse: list[dict]) -> dict[str, dict]:
    """Messungen und Chronikzeilen nach dem Tag der Aufnahme (Ortszeit des Monitors)."""
    tage: dict[str, dict] = {}
    for k in messungen:
        tag = (k.get("erfasst_um") or "")[:10]
        tage.setdefault(tag, {"messungen": [], "ereignisse": []})["messungen"].append(k)
    for e in ereignisse:
        tag = (e.get("erfasst_um") or "")[:10]
        tage.setdefault(tag, {"messungen": [], "ereignisse": []})["ereignisse"].append(e)
    return {tag: inhalt for tag, inhalt in sorted(tage.items()) if re.fullmatch(r"\d{4}-\d{2}-\d{2}", tag)}


def index(welt_id: str, welt: dict, tage: dict[str, dict], verworfen: int, neuladen: int) -> dict:
    alle = [k for t in tage.values() for k in t["messungen"]]
    zeiten = [k["spielzeit_ms"] for k in alle if isinstance(k.get("spielzeit_ms"), (int, float))]
    erfasst = sorted(k["erfasst_um"] for k in alle if k.get("erfasst_um"))
    return {
        "schema": SCHEMA,
        "world_id": welt_id,
        "welt": {k: welt[k] for k in ("name", "seed", "schwierigkeit", "dlcs") if welt.get(k) is not None},
        "messungen": len(alle),
        "verworfen": verworfen,
        "neuladen": neuladen,
        "spielzeit_von_ms": min(zeiten) if zeiten else None,
        "spielzeit_bis_ms": max(zeiten) if zeiten else None,
        "erfasst_von": erfasst[0] if erfasst else None,
        "erfasst_bis": erfasst[-1] if erfasst else None,
        "tage": [{
            "datum": tag,
            "datei": f"tag-{tag}.json",
            "messungen": len(t["messungen"]),
            "ereignisse": len(t["ereignisse"]),
            "spielzeit_von_ms": min((k["spielzeit_ms"] for k in t["messungen"] if k.get("spielzeit_ms") is not None), default=None),
            "spielzeit_bis_ms": max((k["spielzeit_ms"] for k in t["messungen"] if k.get("spielzeit_ms") is not None), default=None),
        } for tag, t in tage.items()],
        "stand": "stand.json",
    }
