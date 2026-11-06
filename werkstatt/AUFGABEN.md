# Aufgaben

Wer etwas anfängt, trägt sich unter „In Arbeit“ ein (wer, seit wann, welche Dateien). Fertiges wandert nach „Zur Prüfung“ oder „Erledigt“.

## In Arbeit

_(leer)_

## Zur Prüfung

- **Kapitel V „Olivaria“** (Claude, 6.11.2026): 125:17 bis 146:09 min Spielzeit, schließt mit den ersten Plebejern auf Olivaria; Bericht, sieben Tagebucheinträge, Randnotiz, Register `erster-lauf-0049` bis `-0060`, neue Quelle Q9 (Spielstände bei 125:17 und 140:26 min), zwei offene Fragen (Beginn der Unruhen, Ausgang von Tarragons Lieferung); in der Inselliste Olivaria mit „bis 125:17 min Lorica“ sowie Caer Morgan und Zibanitu. Online seit `6272304`, Messdaten `a404828`. Prüfen: Zahlen und Spielzeiten gegen Messdaten und Register, die Unruhen (Messdaten nennen 120:12 min), Tarragons Zahlung und die Werft als Abgeleitet, Schreibweise nach `SCHREIBSTIL.md`.

- **Kapitel IV „Lorica“** (Claude, 6.11.2026): 75:22 bis 125:17 min Spielzeit, schließt mit Lorica, der ersten neuen Insel; Bericht, sieben Tagebucheinträge (darunter der Brief „Die erste Seife“ mit dem Vergleich zu Rom, auf Wunsch des Spielers), Randnotiz, Register `erster-lauf-0037` bis `-0048`, offene Frage zu den Einheiten. Online seit `996cbe5`, Messdaten `9f866e3`. Prüfen: Zahlen und Spielzeiten gegen Messdaten und Register, Siedlungsrechte und Koch als Abgeleitet gekennzeichnet, Kanon (Mutter nichts festgelegt), Schreibweise nach `SCHREIBSTIL.md`.

- **Kapitel III „Eisen und Segel“** (Claude, 6.11.2026): 47:25 bis 75:22 min Spielzeit, schließt mit der Kleinen Gemeinde; Bericht, acht Tagebucheinträge, Randnotiz, Register `erster-lauf-0025` bis `-0036`, Quelle Q8 (Feuer aus dem Spielstand und nach Angabe des Spielers), offene Frage zum Bevölkerungssprung bei 74:59 min. Erstes Kapitel nach `docs/SCHREIBSTIL.md`. Online seit `6695e44`, Messdaten `4d6145c`. Prüfen: Zahlen und Spielzeiten gegen Messdaten und Register, Feuer gegen den Spielstand, Kanon (Pirat ohne Bezug zum Vater, Entscheidung des Spielers), Schreibweise nach `SCHREIBSTIL.md`.

- **Kapitel II „Brot und Ziegel“** (Claude, 5.11.2026): 19:33 bis 47:25 min Spielzeit, schließt mit dem Großen Vicus; Bericht, neun Tagebucheinträge, Randnotiz, Register `erster-lauf-0013` bis `-0024`, Quelle Q7 (nachgelesene Spielstände), offene Frage zu Zara Nitus Vertrag. Online seit `ef48cca`, Messdaten `e3214ee`. Ohne Faktenblatt geschrieben (siehe `LOG.md`). Prüfen: Zahlen und Spielzeiten gegen Messdaten und Register, Textarten getrennt, Kanon (kein Amt, Offenes offen, Erinnerung an das Feuer ohne neue Festlegung), Schreibweise.

- **Spezialisten und Gegenstände aus dem Monitor** (Claude, 5.11.2026): `scripts/monitor_daten.py` übernimmt `items` in den Stand und die Chronikzeilen `art: item`; Namen, Seltenheit und Gebäude unter `namen`; Test und `docs/MONITOR.md`. Dazu Korrektur „1 71438“ → Gaius Julius Lupus in `chronik.html` und `werkstatt/erster-lauf/STAND.md`. Online seit `c778e0d`, Messdaten `e3214ee` (84 Messungen bis 1:04 h, noch ohne Items: Monitor vor dem Neustart). Prüfen: keine privaten Angaben im Stand, Wortlaut der Korrektur.
- **Kapitel I „Zwanzig Bretter“** (Claude, 5.11.2026): 0:00 bis 19:33 min Spielzeit, schließt mit den ersten Plebejern; Bericht, neun Tagebucheinträge, Randnotiz, Register `erster-lauf-0004` bis `-0012`, Quelle Q6. Online seit `21d4859`, Messdaten `b3e3a10`. Ohne Faktenblatt geschrieben, direkt aus dem Monitor (siehe `LOG.md`). Prüfen: Zahlen und Spielzeiten gegen die Messdaten, Textarten getrennt, Kanon (kein Amt, Offenes offen), Schreibweise.

- **Gerüst der AnnoChronik** (Claude, 5.11.2026): Portal, Chronik „Caesia Varilla · Erster Lauf“, Design „römisch“, Register, Prüfskript, Action „Datenqualität“, Hochlade-Skript mit Datenschutzfilter, Werkstatt, Doku. Prüfen: Regeln in `docs/ERSTER-LAUF.md` gegen `BRIEFING.md` und `lore/caesia-varilla.md`.
- **Caesia als Protagonistin** (Claude, 5.11.2026): Abschnitt „Die Protagonistin“ in `saves/erster-lauf/chronik.html` nach dem Dossier, offene Punkte unter „Offene Fragen“, Quelle Q4. Prüfen: nichts Offenes als Tatsache, kein Amt, Ton.
- **Titel und Adresse** (Spieler): Die Chronik heißt „Caesia Varilla · Erster Lauf“ unter `saves/erster-lauf/`, online seit `caeddda`.

## Offen

- **Faktenblatt-Skript je Kapitel** (Claude): `werkstatt/erster-lauf/fakten/kapitel-N.md` aus dem Anno-Monitor für einen Spielzeitraum. Vor Kapitel I.
- **Kapitel VI** (Claude): ab 146:09 min bis zum nächsten Einschnitt, den der Spieler bestätigt. Bis 165:38 min ist schon gemessen: Valerias Geleit und der unterschriebene Vertrag an Bord, Ceres auf Stufe 3, „Kult der Minerva“ begonnen, Ziegeleien und Brot auf Olivaria; Einzelheiten in `werkstatt/erster-lauf/STAND.md`.
- **Ausbruchszeit der Unruhen in den Messdaten** (Monitor-Sitzung): Die Chronikzeile vom Autosave bei 135:16 min nennt 120:12 min, belegt ist ein Beginn nach 125:17 min (Kapitel V). Wenn der Monitor das berichtigt, unter „Korrekturen“ in `chronik.html` vermerken.
- **Kapitel I und II nach `SCHREIBSTIL.md`** (Claude, nur auf Freigabe des Spielers): Dort stehen noch Kontrastformeln und Schlusspointen (etwa „Stattdessen grüße ich sie höflich“); Überarbeitung nur, wenn der Spieler sie gesondert freigibt, mit Eintrag unter „Korrekturen“.
- **Schrift Cinzel** (Claude, auf Wunsch): Capitalis für Titel statt Cormorant in Versalien; braucht einen Download mit Freigabe.

## Erledigt

- **Steckbrief der Protagonistin** (Spieler, 5.11.2026): Dossier `lore/caesia-varilla.md`, Commit `6977952`.
- **Erster Upload der Messdaten** (Claude, 5.11.2026): `0321ce3`, 8 Messungen bis 5:36 min Spielzeit.
- **Entscheidungen, Erkundung, Inselnahmen automatisch** (Claude, 5.11.2026): im Anno-Monitor eingebaut (Spielstand, Spielprotokoll, Katalog Schema 2); die AnnoChronik übernimmt sie über `publish-monitor.py`, Ereignisfenster und Bildschirmfotos bleiben lokal.
