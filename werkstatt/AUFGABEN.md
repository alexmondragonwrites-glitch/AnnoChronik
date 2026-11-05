# Aufgaben

Wer etwas anfängt, trägt sich unter „In Arbeit“ ein (wer, seit wann, welche Dateien). Fertiges wandert nach „Zur Prüfung“ oder „Erledigt“.

## In Arbeit

_(leer)_

## Zur Prüfung

- **Kapitel I „Zwanzig Bretter“** (Claude, 5.11.2026): 0:00 bis 19:33 min Spielzeit, schließt mit den ersten Plebejern; Bericht, neun Tagebucheinträge, Randnotiz, Register `erster-lauf-0004` bis `-0012`, Quelle Q6. Online seit `21d4859`, Messdaten `b3e3a10`. Ohne Faktenblatt geschrieben, direkt aus dem Monitor (siehe `LOG.md`). Prüfen: Zahlen und Spielzeiten gegen die Messdaten, Textarten getrennt, Kanon (kein Amt, Offenes offen), Schreibweise.

- **Gerüst der AnnoChronik** (Claude, 5.11.2026): Portal, Chronik „Caesia Varilla · Erster Lauf“, Design „römisch“, Register, Prüfskript, Action „Datenqualität“, Hochlade-Skript mit Datenschutzfilter, Werkstatt, Doku. Prüfen: Regeln in `docs/ERSTER-LAUF.md` gegen `BRIEFING.md` und `lore/caesia-varilla.md`.
- **Caesia als Protagonistin** (Claude, 5.11.2026): Abschnitt „Die Protagonistin“ in `saves/erster-lauf/chronik.html` nach dem Dossier, offene Punkte unter „Offene Fragen“, Quelle Q4. Prüfen: nichts Offenes als Tatsache, kein Amt, Ton.
- **Titel und Adresse** (Spieler): Die Chronik heißt „Caesia Varilla · Erster Lauf“ unter `saves/erster-lauf/`, online seit `caeddda`.

## Offen

- **Faktenblatt-Skript je Kapitel** (Claude): `werkstatt/erster-lauf/fakten/kapitel-N.md` aus dem Anno-Monitor für einen Spielzeitraum. Vor Kapitel I.
- **Kapitel II** (Claude): ab 19:33 min bis zum nächsten Einschnitt, den der Spieler bestätigt; Stoff in `werkstatt/erster-lauf/STAND.md`.
- **Schrift Cinzel** (Claude, auf Wunsch): Capitalis für Titel statt Cormorant in Versalien; braucht einen Download mit Freigabe.

## Erledigt

- **Steckbrief der Protagonistin** (Spieler, 5.11.2026): Dossier `lore/caesia-varilla.md`, Commit `6977952`.
- **Erster Upload der Messdaten** (Claude, 5.11.2026): `0321ce3`, 8 Messungen bis 5:36 min Spielzeit.
- **Entscheidungen, Erkundung, Inselnahmen automatisch** (Claude, 5.11.2026): im Anno-Monitor eingebaut (Spielstand, Spielprotokoll, Katalog Schema 2); die AnnoChronik übernimmt sie über `publish-monitor.py`, Ereignisfenster und Bildschirmfotos bleiben lokal.
