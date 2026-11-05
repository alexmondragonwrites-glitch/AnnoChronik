# Werkstatt-Log

Übergaben und Reviews, neueste oben. Nur ergänzen.

## 2026-11-05 – Spezialisten und Gegenstände aus dem Monitor (Claude)

- Spieler: „haben wir auch spezialisten und items drin?“, danach „Ja, einbauen“.
- Im Anno-Monitor:
  - Katalog Schema 5 mit 760 Items (Name, Art, Seltenheit, Preis) und 126 Gebäuden und Schiffen mit Plätzen für Items.
  - Der Spielstand-Leser verfolgt die eigenen Stücke mit Ort: Lager einer eigenen Insel, eingesetzt in einem Gebäude, an Bord eines eigenen Schiffs. Treibende Fracht zählt nicht.
  - Chronikzeilen „Neuer Spezialist: …“, Ortswechsel, „Abgegeben (verkauft, verbraucht oder übergeben): …“.
  - Belohnungen von Entscheidungen tragen jetzt Item-Namen. Gesprächsschritte („Sprich mit …“) einer Entscheidung, deren Wahl feststeht, bekommen keine eigene Zeile mehr.
  - Seltenheit im Wortlaut des Spiels (Mythic heißt „heroisch“).
- Hier:
  - `scripts/monitor_daten.py` übernimmt `items` in `stand.json` (guid, ort, insel, objekt, provinz) und die Felder `item`, `item_id` der Chronikzeilen.
  - Namen stehen unter `namen.items`, `namen.item_seltenheit` und `namen.objekte`.
  - Neuer Test in `test-monitor-daten.py`, Beschreibung in `docs/MONITOR.md`.
- Hinweis aus Kapitel I erledigt: „1 71438“ ist der Spezialist Gaius Julius Lupus, Vermögensfachmann (episch).
  - Die Zeile in der Monitor-Chronik ist beim Spieler berichtigt, mit Vermerk `korrigiert`; die alte Datei liegt daneben.
  - Korrektur in `chronik.html` unter „Korrekturen“; `werkstatt/erster-lauf/STAND.md` nachgezogen.
  - Im Spielstand bei 48:21 min sitzt Gaius schon in der Villa des Praetors auf Beneventum. Die zwei Kisten aus „Verlorene Fracht“ treiben bei 50:47 min noch im Meer.
- Geprüft:
  - Anno-Monitor: 39 Tests grün, darunter Autosave 9 und 11 als feste Testkopien.
  - Hier: `test-monitor-daten.py` (7 Tests) und `validate-data.mjs`.
  - Stand aus dem echten Autosave 11 ohne private Funde.
- Noch nicht hochgeladen: wartet auf die Freigabe des Spielers, zusammen mit den neuen Messdaten.

## 2026-11-05 – Kapitel I „Zwanzig Bretter“ (Claude, Nebensitzung)

- Auftrag über die Monitor-Sitzung: Kapitel I als Tagebuch der Protagonistin mit Bericht. Vorgeschlagen war als Einschnitt die erste Bevölkerungsstufe, die ersten Plebejer (19:33 min Spielzeit, Aufnahme 16:34), als Alternative das erste Heiligtum (38:35 min). Spieler: „Bei den Plebejern“.
- Ohne Faktenblatt geschrieben (das Skript ist offen, `scripts/` lag bei der Monitor-Sitzung), direkt aus dem Anno-Monitor: Kurzwerte und Chronik der Welt, vollständige Messungen der Läufe ab 15:09 und 16:29, die Spielprotokolle vom 5.11. und das Bildschirmfoto vom Libertus. Welche Werte nur in den vollständigen Messungen stehen, sagt die Quellenzeile des Berichts.
- `chronik.html`:
  - Kapitel I mit Kopf, Bericht (Kennzahlen, Zeitachse, Quellen Q3, Q5 und neu Q6 Spielprotokoll), neun Tagebucheinträgen und Randnotiz „Abgeleitet“;
  - „Inseln und Provinzen“ mit Beneventum, Hortia Poenitentium, Umbra und Werddon;
  - Verweis auf das Kapitel im Inhalt.
- Register `erster-lauf-0004` bis `-0012`: Inselnahmen der drei Praetoren, erste Liberti, Kleiner Vicus, Bilanz im Plus, Tarragon respektvoll gegrüßt, die ersten Plebejer; als Abgeleitet, dass Zara Nitu vor Caesia Plebejer hatte.
- `roemisch.css` ergänzt: Kapitelkopf, Zeitachse, Einträge und Formen des Tagebuchs.
- Geprüft:
  - `validate-data.mjs` und `test-monitor-daten.py`;
  - Wortprüfung (Verneinungen, KI-Wörter) ohne Fund im neuen Text;
  - Browser bei 1280 und 375 px, hell und dunkel, ohne Konsolenfehler und ohne waagrechtes Scrollen.
  - Beim Gegenlesen zwei Lagerangaben im Tagebuch an die Messungen angepasst (25 Bretter beim ersten Gang, 6 bei der Zählung mit dem Kleinen Vicus).
- Hochgeladen auf Freigabe („Ja, hochladen“): `b3e3a10` (Messdaten, 72 Messungen bis 55:22 min, Skriptstand `067fbfb` der Monitor-Sitzung) und `21d4859` (Kapitel I). „Datenqualität“ für `21d4859` grün.
- Für eine Prüfung durch Codex:
  - Spielzeiten und Kurzwerte stehen in `saves/erster-lauf/data/monitor/tag-2026-11-05.json`.
  - Status, Wohnhäuser, Lager, Betriebe am Stichtag, Geldposten und die Zahlen der Praetoren liegen nur in den vollständigen Messungen beim Spieler.
  - Die Zeiten der Inselnahmen und Ereignisfenster kommen aus dem Spielprotokoll und sind zwischen die Messungen davor und danach eingeordnet.
- Hinweis an die Monitor-Sitzung: Bei „Zwillinge in der Zwickmühle“ (47:25 bis 48:21 min) steht als Belohnung „1 71438“, der Name fehlt im Katalog.

## 2026-11-05 – Ereignisse automatisch aus dem Monitor (Claude)

- Spieler: „können wir die ereignisse nicht irgenwie erfassen anders?“, danach „Ja, einbauen“.
- Im Anno-Monitor:
  - Entscheidungen aus dem Spielstand (QuestManager), mit Titel, Wahl, Kosten und Wirkung aus den Spieldaten;
  - Erkundung (DiscoveryManager, entdeckte Inseln je Provinz);
  - aus dem Spielprotokoll Inselnahmen von Spieler und Praetoren, Ereignisfenster (genaue Spielzeit der Entscheidung) und Bildschirmfotos.
  - Am echten Lauf geprüft: Libertus (Vorrat gekauft), „Begegnung mit einem Rivalen“ (Tarragon, respektvoll gegrüßt), Latium bis 12 entdeckte Inseln, Inselnahmen von Tarragon (Hortia Poenitentium), Zara Nitu (Umbra) und Athr Iorgwyn (Werddon).
- Hier: `publish-monitor.py` lässt Ereignisfenster und Bildschirmfotos weg (`monitor_daten.oeffentlich`), neue Felder in den Ereignissen; `docs/MONITOR.md`, `docs/ERSTER-LAUF.md`. Wirksam, sobald der Spieler den Monitor neu startet.

## 2026-11-05 – Erste Insel und erste Entscheidung im Register (Claude)

- Hochgeladen auf Freigabe („Ja, hochladen“): `a6e5341` (Partie-Name, Korrektur im Steckbrief), `0321ce3` (erste Messdaten, 8 Messungen bis 5:36 min). „Datenqualität“ und Pages grün, live geprüft.
- Spieler schickte zwei Bildschirmfotos vom Ereignis „Ein Libertus grüßt dich“ mit der Frage „nehmen wir sowas auch mit auf? geht das?“. Eingetragen (lokal): Register `erster-lauf-0002` (erste eigene Insel Beneventum, Q3) und `erster-lauf-0003` (Bretter gekauft, Q5 und Q3), Q5 unter Quellen, Startprovinz im Steckbrief, Landungsort unter „Offene Fragen“, Regeln unter „Ereignisse und Entscheidungen im Spiel“ in `docs/ERSTER-LAUF.md`. Der Monitor zeigt den Kauf im Geld (17.684 bei 4:38 min, 17.009 bei 5:36 min), die Entscheidung selbst nicht; Probe dazu auf der Tafel.

## 2026-11-05 – Partie-Name korrigiert, Datenweg mit der echten Partie geprüft (Claude)

- Erster Autosave der Partie um 15:52: Im Spielstand heißt sie „Caesia Varilla“ (Partie-Ordner und Firmenname), Weltkennung `anno117-1793890256`, Seed 6949, drei Erweiterungen, Praetoren Tarragon, Athr Iorgwyn, Zara Nitu. „Cassandra“ ist das Profil der Einstellungsübersicht. `data/monitor-sources.json` und `meta.json` stehen jetzt auf `partie: "Caesia Varilla"`; mit „Cassandra“ hätte das Hochlade-Skript die Welt nie gefunden.
- Chronik: Steckbrief der Partie mit „Name im Spielstand: Caesia Varilla“ (Q3), dazu ein Eintrag unter „Korrekturen“, weil dort seit dem ersten Push „Profil im Spiel: Cassandra“ stand.
- `publish-monitor.py --save erster-lauf --no-push`: Weltkennung gefunden und eingetragen, 3 Messungen, Stand aus Live (1:38 min Spielzeit, Geld 20.000, noch ohne eigene Insel), Prüfung auf Privates bestanden. Schwierigkeit und Erweiterungen kommen jetzt auch bei einem Live-Stand aus dem Spielstand. Nicht hochgeladen.

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
