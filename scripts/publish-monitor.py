"""Messdaten aus dem Anno-Monitor auf die Seite bringen; hochgeladen wird erst nach Bestätigung.

    py -3 scripts/publish-monitor.py                  alle Welten aus data/monitor-sources.json
    py -3 scripts/publish-monitor.py --save erster-lauf nur eine Welt
    py -3 scripts/publish-monitor.py --no-push        nur lokal schreiben und prüfen
    py -3 scripts/publish-monitor.py --yes            ohne Rückfrage (z. B. für geplante Aufgaben)

Der Monitor liegt neben dem Repo (`../Anno-Monitor`, sonst `--monitor PFAD`). Gelesen werden
`history/welten.json` und je Welt `history/welten/<Welt>/` (Kurzwerte, Chronik, letzter Stand).
Geschrieben wird `saves/<welt>/data/monitor/`: je Aufnahmetag eine Datei, dazu `stand.json` und
`index.json`. Hat eine Welt noch keine Weltkennung, sucht das Skript die Partie über ihren Ordnernamen
(`partie`) und trägt die Kennung ein, sobald es einen Autosave gibt.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
ROOT = HIER.parent
sys.path.insert(0, str(HIER))
import monitor_daten as md  # noqa: E402

QUELLEN = ROOT / "data" / "monitor-sources.json"


def einstellung_bytes(obj) -> bytes:
    """Register und Manifeste wie von Hand und von new-save.mjs: Einzug mit zwei Leerzeichen."""
    return (json.dumps(obj, ensure_ascii=False, indent=2) + chr(10)).encode("utf-8")


def spielzeit(ms) -> str:
    if not isinstance(ms, (int, float)):
        return "–"
    minuten = int(ms // 60000)
    return f"{minuten // 60}:{minuten % 60:02d} h"


def git(*args: str, pruefen: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, check=pruefen, capture_output=True, text=True, encoding="utf-8")


def monitor_module(monitor: Path):
    sys.path.insert(0, str(monitor))
    import katalog  # noqa: E402  (Module des Anno-Monitors)
    import messung  # noqa: E402
    import welten  # noqa: E402
    return welten, messung, katalog


def welt_finden(verzeichnis, partie: str | None) -> str | None:
    """Welt aus Spielständen mit diesem Partie-Ordner; unter mehreren die zuletzt gesehene."""
    if not partie:
        return None
    kandidaten = [(e.get("zuletzt") or "", wid) for wid, e in verzeichnis.lesen().items()
                  if e.get("ordner") == partie and e.get("profil_id") is not None]
    return max(kandidaten)[1] if kandidaten else None


def aktueller_stand(welt, messung, verworfen: set) -> dict | None:
    """Live-Messung, ergänzt um den letzten Spielstand, sonst der letzte Spielstand (wie im Monitor)."""
    sp, lua = welt.letzte("spielstand"), welt.letzte("lua")
    sp = sp if sp and sp.get("mid") not in verworfen else None
    lua = lua if lua and lua.get("mid") not in verworfen else None
    if lua and (not sp or (lua.get("spielzeit_ms") or 0) > (sp.get("spielzeit_ms") or 0)):
        return messung.zusammenfuehren(lua, sp)
    if not sp and not lua:  # Welten aus der Zeit vor den getrennten letzten Ständen je Quelle
        m = welt.letzte()
        return m if m and m.get("mid") not in verworfen else None
    return sp or lua


def bauen(quelle: dict, monitor: Path, module) -> tuple[str, dict[Path, bytes], str] | None:
    welten, messung, katalog = module
    verzeichnis = welten.Verzeichnis(monitor)
    wid = quelle.get("world_id") or welt_finden(verzeichnis, quelle.get("partie"))
    if not wid:
        print(f"{quelle['name']}: noch kein Autosave der Partie „{quelle.get('partie')}“ im Monitor.")
        return None
    welt = welten.Welt(monitor, wid)
    gueltig = welt.gueltige_messungen()
    if not gueltig:
        print(f"{quelle['name']}: keine gültigen Messungen für {wid}.")
        return None
    verworfen = welt.verworfene()
    chronik = welt.chronik()
    neuladen = sum(1 for e in chronik if e.get("art") == "neuladen")

    namen = verzeichnis.inselnamen(wid)
    aktuell = aktueller_stand(welt, messung, verworfen)
    if aktuell:
        aktuell = messung.namen_anwenden(json.loads(json.dumps(aktuell)), namen)
        # Live kennt Seed und Namen, Schwierigkeit und Erweiterungen stehen nur im Spielstand
        aktuell["welt"] = {**((welt.letzte("spielstand") or {}).get("welt") or {}), **(aktuell.get("welt") or {})}
    # Vom Spieler umbenannte Inseln: Chronikzeilen aus Spielständen tragen den ursprünglichen Namen.
    umbenannt = {}
    for m in (welt.letzte("spielstand"), welt.letzte(), aktuell):
        for i in (m or {}).get("inseln") or []:
            neu, alt = namen.get(str(i.get("id"))), i.get("name_spielstand") or i.get("name")
            if neu and alt and alt != neu:
                umbenannt[alt] = neu

    tage = md.nach_tagen([md.kurz(k) for k in gueltig],
                         [md.ereignis(e, umbenannt) for e in chronik if e.get("art") != "neuladen"])
    eintrag = verzeichnis.lesen().get(wid) or {}
    ziel = ROOT / "saves" / quelle["save"] / "data" / "monitor"
    dateien: dict[Path, bytes] = {}
    for tag, inhalt in tage.items():
        dateien[ziel / f"tag-{tag}.json"] = md.json_bytes({"schema": md.SCHEMA, "datum": tag, **inhalt})
    if aktuell:
        dateien[ziel / "stand.json"] = md.json_bytes(md.stand(aktuell, katalog.laden()))
    idx = md.index(wid, {**eintrag, **((aktuell or {}).get("welt") or {})}, tage, len(verworfen), neuladen)
    dateien[ziel / "index.json"] = md.json_bytes(idx)

    for pfad, inhalt in dateien.items():
        funde = md.privat_funde(json.loads(inhalt))
        if funde:
            raise SystemExit(f"Abbruch: {pfad.relative_to(ROOT)} enthält Privates: {funde[:3]}")
    beschreibung = f"{quelle['name']} bis {spielzeit(idx['spielzeit_bis_ms'])} Spielzeit ({idx['messungen']} Messungen)"
    return wid, dateien, beschreibung


def kennung_eintragen(quelle: dict, wid: str) -> list[Path]:
    """Neu gefundene Weltkennung in monitor-sources.json und meta.json; Manifest auf die Messdaten."""
    geaendert = []
    quellen = json.loads(QUELLEN.read_text(encoding="utf-8"))
    for q in quellen:
        if q.get("save") == quelle["save"] and q.get("world_id") != wid:
            q["world_id"] = wid
            QUELLEN.write_bytes(einstellung_bytes(quellen))
            geaendert.append(QUELLEN)
    daten = ROOT / "saves" / quelle["save"] / "data"
    meta_pfad, manifest_pfad = daten / "meta.json", daten / "manifest.json"
    meta = json.loads(meta_pfad.read_text(encoding="utf-8"))
    if (meta.get("monitor") or {}).get("world_id") != wid:
        meta.setdefault("monitor", {})["world_id"] = wid
        meta_pfad.write_bytes(einstellung_bytes(meta))
        geaendert.append(meta_pfad)
    manifest = json.loads(manifest_pfad.read_text(encoding="utf-8"))
    if manifest.get("monitor") != "data/monitor/index.json":
        manifest["monitor"] = "data/monitor/index.json"
        manifest_pfad.write_bytes(einstellung_bytes(manifest))
        geaendert.append(manifest_pfad)
    return geaendert


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--save", help="nur diese Welt (Kennung aus data/monitor-sources.json)")
    ap.add_argument("--monitor", default=str(ROOT.parent / "Anno-Monitor"), help="Ordner des Anno-Monitors")
    ap.add_argument("--no-push", action="store_true", help="nur lokal schreiben und prüfen")
    ap.add_argument("--yes", action="store_true", help="ohne Rückfrage hochladen")
    args = ap.parse_args(argv)

    monitor = Path(args.monitor)
    if not (monitor / "welten.py").exists():
        print(f"Anno-Monitor nicht gefunden: {monitor}", file=sys.stderr)
        return 2
    module = monitor_module(monitor)
    quellen = [q for q in json.loads(QUELLEN.read_text(encoding="utf-8")) if not args.save or q["save"] == args.save]
    if not quellen:
        print(f"Welt „{args.save}“ steht nicht in data/monitor-sources.json.", file=sys.stderr)
        return 2

    if not args.no_push and git("remote", pruefen=False).stdout.strip():
        git("fetch", "origin", pruefen=False)
        if git("rev-parse", "--verify", "-q", "origin/main", pruefen=False).returncode == 0 and \
                git("rev-parse", "--verify", "-q", "HEAD", pruefen=False).returncode == 0:
            r = git("merge", "--ff-only", "origin/main", pruefen=False)
            if r.returncode != 0:
                print("GitHub-Stand lässt sich nur mit Zusammenführen übernehmen; bitte zuerst von Hand klären.\n" + r.stderr,
                      file=sys.stderr)
                return 3

    pfade: list[Path] = []
    beschreibungen: list[str] = []
    for quelle in quellen:
        ergebnis = bauen(quelle, monitor, module)
        if not ergebnis:
            continue
        wid, dateien, beschreibung = ergebnis
        if not quelle.get("world_id"):
            print(f"{quelle['name']}: Weltkennung {wid} gefunden und eingetragen.")
        pfade += kennung_eintragen(quelle, wid)
        for pfad, inhalt in dateien.items():
            if not pfad.exists() or pfad.read_bytes() != inhalt:
                pfad.parent.mkdir(parents=True, exist_ok=True)
                pfad.write_bytes(inhalt)
                pfade.append(pfad)
        beschreibungen.append(beschreibung)

    if not pfade:
        print("Keine neuen Messdaten.")
        return 0
    pruefung = subprocess.run(["node", "scripts/validate-data.mjs"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    print(pruefung.stdout.strip())
    if pruefung.returncode != 0:
        print("Prüfung fehlgeschlagen, nichts committet.\n" + pruefung.stderr, file=sys.stderr)
        return 4
    namen = sorted({str(p.relative_to(ROOT)).replace("\\", "/") for p in pfade})
    print("Geändert:\n  " + "\n  ".join(namen))
    if args.no_push:
        return 0
    if not args.yes and input("Hochladen? [j/N] ").strip().lower() not in ("j", "ja", "y", "yes"):
        print("Nicht hochgeladen; die Dateien bleiben lokal.")
        return 0
    git("add", "--", *namen)
    git("commit", "-m", "Messdaten " + "; ".join(beschreibungen))
    r = git("push", "origin", "HEAD:main", pruefen=False)
    if r.returncode != 0:
        print("Push fehlgeschlagen:\n" + r.stderr, file=sys.stderr)
        return 5
    print("Hochgeladen: " + "; ".join(beschreibungen))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
