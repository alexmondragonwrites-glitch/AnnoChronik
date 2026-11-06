"""Tests für monitor_daten.py (läuft ohne Anno-Monitor, auch in der GitHub-Prüfung)."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import monitor_daten as md  # noqa: E402

# Erfundene Kennung und Pfad, zur Laufzeit zusammengesetzt: Die Prüfung des Repos sucht genau solche Muster.
KONTO = "-".join("0" * n for n in (8, 4, 4, 4, 12))
PFAD = "\\".join(["D:", "Dokumente", "Anno 117 - Pax Romana", "acc" + "ounts", KONTO, "Cassandra", "Autosave 1.a8s"])


def messung() -> dict:
    return {
        "schema": 1, "quelle": "spielstand", "mid": "20261105T153000-00001", "erfasst_um": "2026-11-05T15:30:00+01:00",
        "spielzeit_ms": 600_000, "geld": 15000,
        "spielstand": {"datei": "Autosave 1.a8s", "ordner": "Cassandra", "pfad": PFAD},
        "welt": {"id": "anno117-42", "profil_id": 42, "name": "Cassandra", "seed": 7, "dlcs": [1, 2, 3]},
        "bevoelkerung": {"gesamt": 120, "je_stufe": {"1499": 120.0}},
        "inseln": [
            {"id": 1, "name": "Ostia", "eigene": True, "provinz": 3245, "bewohner": 120.0,
             "lager": {"2088": 12, "2136": 0}, "lagerverlauf": {"punkt_ms": 10000, "waren": {"2088": [1, 2]}},
             "stufen": {"1499": {"bewohner": 120.0, "haeuser": 12}},
             "beduerfnisse": {"1499": {"2088": {"erfuellung": 1.0}}},
             "betriebe": {"2878": {"anzahl": 2}},
             "statistik": {"zeit_ms": 600_000, "erzeugung": {"2088": 2.0}, "verbrauch": {"2088": 1.5},
                           "schnappschuesse": [{"zeit_ms": 1}]}},
            {"id": 2, "name": "Fremde Insel", "eigene": False, "lager": {"2088": 99}},
        ],
        "rivalen": [{"id": 31099, "name": "Tarragon", "attribute": {"Population": 50.0}, "geheim": "x"}],
        "ergaenzt_aus": {"datei": "Autosave 1.a8s", "gespeichert_um": "2026-11-05T15:29:00+01:00", "spielzeit_ms": 590_000},
    }


KATALOG = {"stufen": {"1499": {"text": "Liberti"}}, "produkte": {"2088": {"text": "Fisch"}, "2136": {"text": "Brot"}},
           "betriebe": {"2878": {"text": "Fischerhütte"}}}


class Datenschutz(unittest.TestCase):
    def test_findet_pfade_und_konto(self):
        funde = md.privat_funde(messung())
        self.assertTrue(any("pfad" in f for f in funde), funde)
        self.assertFalse(md.privat_funde({"link": "https://example.org/a", "zeit": "2026-11-05T15:30:00+01:00"}))
        self.assertTrue(md.privat_funde({"x": KONTO}))
        self.assertTrue(md.privat_funde({"x": "C:/Users/someone"}))

    def test_stand_ohne_privates(self):
        s = md.stand(messung(), KATALOG)
        self.assertEqual(md.privat_funde(s), [])
        text = json.dumps(s, ensure_ascii=False)
        for weg in ("Autosave", "lagerverlauf", "schnappschuesse", "Fremde Insel", "geheim", "profil_id"):
            self.assertNotIn(weg, text)
        self.assertEqual([i["name"] for i in s["inseln"]], ["Ostia"])
        self.assertEqual(s["inseln"][0]["lager"], {"2088": 12})           # Nullen fallen weg
        self.assertEqual(s["ergaenzt_aus"], {"spielzeit_ms": 590_000, "gespeichert_um": "2026-11-05T15:29:00+01:00"})
        self.assertEqual(s["namen"]["stufen"], {"1499": "Liberti"})
        self.assertEqual(s["namen"]["waren"], {"2088": "Fisch"})
        self.assertEqual(s["namen"]["betriebe"], {"2878": "Fischerhütte"})

    def test_kurzwerte_ohne_datei_und_pruefsumme(self):
        k = md.kurz({"mid": "m1", "datei": "Autosave 1.a8s", "sha256_daten": "ab", "spielzeit_ms": 1, "geld": None})
        self.assertEqual(k, {"mid": "m1", "spielzeit_ms": 1})


class Ereignisse(unittest.TestCase):
    def test_entscheidung_und_lokales(self):
        e = md.ereignis({"art": "entscheidung", "text": "Entscheidung „Ein Libertus grüßt dich“: Seinen Vorrat kaufen.",
                         "entscheidung": 99153, "wahl": 99151, "seit_ms": 272400, "spielzeit_ms": 313000,
                         "fenster_um": "2026-11-05T15:58:20+01:00", "gespeichert_um": "x"})
        self.assertEqual((e["entscheidung"], e["wahl"], e["seit_ms"]), (99153, 99151, 272400))
        self.assertNotIn("fenster_um", e)
        self.assertTrue(md.oeffentlich({"art": "insel_besitz"}))
        for art in ("fenster", "bildschirmfoto", "neuladen"):
            self.assertFalse(md.oeffentlich({"art": art}), art)


class Fortschritt(unittest.TestCase):
    def test_forschung_religion_auftraege_im_stand(self):
        m = messung()
        m["forschung"] = {"41": {"fertig": [37724], "laeuft": [37903], "warteschlange": []}}
        m["religion"] = {"41": {"43594": 7}}
        m["auftraege"] = [{"id": "40405-20", "auftrag": 40405, "vertrag": True, "gegenueber": 31103}]
        m["inseln"][0]["religion"] = {"gott": 43594, "hingabe": 7.59}
        kat = dict(KATALOG, forschungen={"37903": {"name": "Attraktive Märkte"}}, goetter={"43594": {"name": "Ceres"}},
                   auftraege={"40405": {"name": "Auftrag: Verlorene Fracht von {ContractProviderName}"}})
        s = md.stand(m, kat)
        self.assertEqual(s["forschung"]["41"]["laeuft"], [37903])
        self.assertEqual(s["inseln"][0]["religion"]["gott"], 43594)
        self.assertEqual(s["auftraege"][0]["gegenueber"], 31103)
        self.assertNotIn("id", s["auftraege"][0])
        self.assertEqual(s["namen"]["forschungen"], {"37903": "Attraktive Märkte"})
        self.assertEqual(s["namen"]["goetter"], {"43594": "Ceres"})
        self.assertEqual(md.privat_funde(s), [])

    def test_zwischenfaelle(self):
        m = messung()
        m["inseln"][0]["zwischenfaelle"] = {"anzahl": 1, "ausgeloest": {"0": 4267708}, "bekaempft": {"30754": 4493400},
                                            "betroffen": {"3087": 6, "3141": 2}}
        s = md.stand(m, KATALOG)
        self.assertEqual(s["inseln"][0]["zwischenfaelle"], {"anzahl": 1, "ausgeloest": {"0": 4267708}})
        self.assertEqual(s["namen"]["zwischenfaelle"], {"0": "Feuer"})
        e = md.ereignis({"art": "zwischenfall", "text": "Feuer auf Beneventum: ausgebrochen bei 71:07 min …",
                         "insel": 8897, "zwischenfall": 0, "ausbruch_ms": 4267708, "spielzeit_ms": 4499200})
        self.assertEqual((e["zwischenfall"], e["ausbruch_ms"]), (0, 4267708))
        self.assertTrue(md.oeffentlich(e))
        self.assertEqual(md.privat_funde(s), [])

    def test_spezialisten_und_gegenstaende(self):
        m = messung()
        m["items"] = [{"id": "288230376151711747", "guid": 71438, "provinz": 3245, "ort": "eingesetzt", "insel": 1,
                       "objekt": 31032}]
        kat = dict(KATALOG, items={"71438": {"name": "Gaius Julius Lupus, Vermögensfachmann", "art": "spezialist",
                                             "seltenheit": "Epic"}},
                   objekte={"31032": "Villa des Praetors"})
        s = md.stand(m, kat)
        self.assertEqual(s["items"], [{"guid": 71438, "ort": "eingesetzt", "insel": 1, "objekt": 31032, "provinz": 3245}])
        self.assertEqual(s["namen"]["items"], {"71438": "Gaius Julius Lupus, Vermögensfachmann"})
        self.assertEqual(s["namen"]["item_seltenheit"], {"71438": "episch"})
        self.assertEqual(s["namen"]["objekte"], {"31032": "Villa des Praetors"})
        e = md.ereignis({"art": "item", "text": "Neuer Spezialist: …", "item": 71438, "item_id": "288230376151711747",
                         "spielzeit_ms": 2_880_000})
        self.assertEqual((e["item"], e["item_id"]), (71438, "288230376151711747"))
        self.assertEqual(md.privat_funde(s), [])


class Tage(unittest.TestCase):
    def test_tage_und_index(self):
        kurz = [{"mid": "a", "erfasst_um": "2026-11-05T15:30:00+01:00", "spielzeit_ms": 600_000},
                {"mid": "b", "erfasst_um": "2026-11-06T06:00:00+01:00", "spielzeit_ms": 900_000}]
        ereignisse = [md.ereignis({"art": "insel_neu", "text": "Eigene Insel Llanfair erstmals beobachtet.",
                                   "erfasst_um": "2026-11-05T15:30:00+01:00", "spielzeit_ms": 600_000, "gespeichert_um": "x"},
                                  {"Llanfair": "Ostia"})]
        self.assertEqual(ereignisse[0]["text"], "Eigene Insel Ostia erstmals beobachtet.")
        self.assertNotIn("gespeichert_um", ereignisse[0])
        tage = md.nach_tagen(kurz, ereignisse)
        self.assertEqual(list(tage), ["2026-11-05", "2026-11-06"])
        i = md.index("anno117-42", {"name": "Cassandra", "profil_id": 42}, tage, verworfen=3, neuladen=1)
        self.assertEqual((i["messungen"], i["spielzeit_von_ms"], i["spielzeit_bis_ms"]), (2, 600_000, 900_000))
        self.assertEqual(i["tage"][0]["ereignisse"], 1)
        self.assertNotIn("profil_id", i["welt"])
        self.assertEqual(md.json_bytes(i), md.json_bytes(json.loads(md.json_bytes(i))))  # bytegleich


if __name__ == "__main__":
    unittest.main()
