# Aufgaben

Wer etwas anfängt, trägt sich unter „In Arbeit“ ein (wer, seit wann, welche Dateien). Fertiges wandert nach „Zur Prüfung“ oder „Erledigt“.

## In Arbeit

_(leer)_

## Zur Prüfung

- **Gerüst der AnnoChronik** (Claude, 5.11.2026): Portal, Chronik „Caesia Varilla · Erster Lauf“, Design „römisch“, Register, Prüfskript, Action „Datenqualität“, Hochlade-Skript mit Datenschutzfilter, Werkstatt, Doku. Prüfen: Regeln in `docs/ERSTER-LAUF.md` gegen `BRIEFING.md` und `lore/caesia-varilla.md`.
- **Caesia als Protagonistin** (Claude, 5.11.2026): Abschnitt „Die Protagonistin“ in `saves/erster-lauf/chronik.html` nach dem Dossier, offene Punkte unter „Offene Fragen“, Quelle Q4. Prüfen: nichts Offenes als Tatsache, kein Amt, Ton.
- **Titel und Adresse** (Spieler): Die Chronik heißt „Caesia Varilla · Erster Lauf“ unter `saves/erster-lauf/`, online seit `caeddda`.

## Offen

- **Faktenblatt-Skript je Kapitel** (Claude): `werkstatt/erster-lauf/fakten/kapitel-N.md` aus dem Anno-Monitor für einen Spielzeitraum. Vor Kapitel I.
- **Kapitel I** (Claude): nach dem ersten Einschnitt der Partie; den Einschnitt bestätigt der Spieler.
- **Entscheidungen automatisch erfassen** (Claude, Probe): prüfen, ob der Spielstand oder der Live-Mod Titel, Wahlmöglichkeiten und Wahl von Ereignissen wie „Ein Libertus grüßt dich“ liefert (Lua: `CDecisionComponent`, `CGovernorDecisionManager`; Spielstand: Quest- und Entscheidungsdaten). Bis dahin über Bildschirmfotos des Spielers.
- **Schrift Cinzel** (Claude, auf Wunsch): Capitalis für Titel statt Cormorant in Versalien; braucht einen Download mit Freigabe.

## Erledigt

- **Steckbrief der Protagonistin** (Spieler, 5.11.2026): Dossier `lore/caesia-varilla.md`, Commit `6977952`.
- **Erster Upload der Messdaten** (Claude, 5.11.2026): `0321ce3`, 8 Messungen bis 5:36 min Spielzeit.
