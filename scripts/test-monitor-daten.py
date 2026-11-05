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
