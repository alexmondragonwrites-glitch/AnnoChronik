# Werkstatt-Log

Übergaben und Reviews, neueste oben. Nur ergänzen.

## 2026-11-05 – Caesia Varilla als Protagonistin, Chronik „Erster Lauf“ (Claude)

- Spieler: „Bitte berücksichtige die Datei lore/caesia-varilla.md als verbindliche Charaktergrundlage für unsere AnnoChronik. Baue Caesia als Protagonistin in die Website ein. Ihre weitere Geschichte entwickeln wir anhand des tatsächlichen Spielverlaufs. das ist der erste lauf“. Das Dossier hat er selbst hochgeladen (`6977952`); das Gerüst setzt darauf auf.
- Chronik heißt jetzt „Caesia Varilla · Erster Lauf“ unter `saves/erster-lauf/` (vorher Arbeitstitel „Cassandra“, `saves/cassandra/`); „Cassandra“ bleibt als Profil im Spiel und als Partie-Ordner für den Monitor. Umbenannt: Werkstattordner, `docs/ERSTER-LAUF.md`, Registerkennung `erster-lauf-0001`.
- Neuer Abschnitt I „Die Protagonistin“ (Etikett „Figurenkanon“, Stil `.ac-kanon`, Quelle Q4): Steckbrief, Wesen, Familie, Verlobung und die Nacht der Flucht als Vorgeschichte, nah am Dossier. Offenes steht unter „Offene Fragen“; der vorgeschlagene Name des Vaters erscheint auf der Seite nicht, weil er noch nicht festgelegt ist. Kein Amt, keine Statthalterschaft.
- Leitlinien des Dossiers in `docs/ERSTER-LAUF.md` übernommen. Versalziffern in den Versalzeilen (Ziffernart wurde von der font-Kurzschreibweise zurückgesetzt). Prüfungen grün, Browser hell und dunkel, 375 px.
- Freigabe zum Hochladen: „die seite kann dann auch live geschaltet werden“, Pages hatte der Spieler eingeschaltet.

## 2026-11-05 – Gerüst angelegt (Claude)

- Auftrag des Spielers: das Repo „gleich aufsetzen wie das TF3 Git dann mit Pages“; erste Partie ist seine neue Partie vom 5.11.2026 (Profil Cassandra). Vorher Briefing mit vier Antworten (`BRIEFING.md`): Kapitel nach Meilensteinen, Tagebuch der Protagonistin, römisches Design, Messdaten im Repo.
- Angelegt: Portal `index.html`, `saves/erster-lauf/` mit Chronikseite (Titelblatt, Steckbrief der Partie, Register, Tagebuch, Inseln und Provinzen, offene Fragen, Quellen Q1 bis Q3, Korrekturen), `data/worlds.json`, `data/monitor-sources.json`, Design `assets/roemisch.css` mit Lorbeer und Mäander (`scripts/ornamente.py`), Schriften EB Garamond und Cormorant (SIL OFL, aus der TF3-Chronik).
- Datenweg: `scripts/publish-monitor.py` liest den Anno-Monitor, schreibt `saves/erster-lauf/data/monitor/` (je Aufnahmetag eine Datei, `stand.json`, `index.json`) ohne Pfade, Dateinamen und Kontokennung; `scripts/monitor_daten.py` mit Tests. Probelauf an der alten Partie „Alexandra Lupara“ (nur lokal, nichts geschrieben): 14 Messungen, 92 Chronikzeilen, umbenannte Insel richtig, keine privaten Funde.
- Prüfungen: `scripts/validate-data.mjs` (Weltregister, Manifeste, Register, Quellenanker, Messdaten, Datenschutz), Action „Datenqualität“.
- Offen: siehe `AUFGABEN.md`.
