# Aufgaben

Wer etwas anfängt, trägt sich unter „In Arbeit“ ein (wer, seit wann, welche Dateien). Fertiges wandert nach „Zur Prüfung“ oder „Erledigt“.

## In Arbeit

_(leer)_

## Zur Prüfung

- **Gerüst der AnnoChronik** (Claude, 5.11.2026): Portal, Chronik „Caesia Varilla · Erster Lauf“, Design „römisch“, Register, Prüfskript, Action „Datenqualität“, Hochlade-Skript mit Datenschutzfilter, Werkstatt, Doku. Prüfen: Regeln in `docs/ERSTER-LAUF.md` gegen `BRIEFING.md` und `lore/caesia-varilla.md`.
- **Caesia als Protagonistin** (Claude, 5.11.2026): Abschnitt „Die Protagonistin“ in `saves/erster-lauf/chronik.html` nach dem Dossier, offene Punkte unter „Offene Fragen“, Quelle Q4. Prüfen: nichts Offenes als Tatsache, kein Amt, Ton.
- **Titel und Adresse** (Spieler): Die Chronik heißt „Caesia Varilla · Erster Lauf“ unter `saves/erster-lauf/`; vor dem ersten Push noch änderbar.

## Offen

- **Erster Upload der Messdaten** (Claude): nach dem ersten Autosave der Partie mit `py -3 scripts/publish-monitor.py --save erster-lauf`, nur mit Freigabe.
- **Faktenblatt-Skript je Kapitel** (Claude): `werkstatt/erster-lauf/fakten/kapitel-N.md` aus dem Anno-Monitor für einen Spielzeitraum. Vor Kapitel I.
- **Kapitel I** (Claude): nach dem ersten Einschnitt der Partie; den Einschnitt bestätigt der Spieler.
- **Schrift Cinzel** (Claude, auf Wunsch): Capitalis für Titel statt Cormorant in Versalien; braucht einen Download mit Freigabe.

## Erledigt

- **Steckbrief der Protagonistin** (Spieler, 5.11.2026): Dossier `lore/caesia-varilla.md`, Commit `6977952`.
