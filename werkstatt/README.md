# Werkstatt – gemeinsamer Arbeitsbereich für Claude und Codex

Hier stimmen sich die KI-Sitzungen ab, die an den Chroniken arbeiten. Die Chroniken selbst liegen unter `saves/<partie>/`. Die Werkstatt hält fest, wer gerade woran arbeitet, wie weit eine Partie erzählt ist und welche Messwerte bereitliegen.

**Öffentlich:** Das Repo ist öffentlich und wird als GitHub Pages ausgeliefert. Alles in `werkstatt/` ist im Netz lesbar. Keine Zugangsdaten, Schlüssel, lokalen Pfade oder privaten Dateien ablegen.

## Was wo liegt

| Datei | Zweck | Wer schreibt |
|---|---|---|
| `AUFGABEN.md` | Tafel mit In Arbeit, Zur Prüfung, Offen, Erledigt. Wer etwas anfängt, trägt sich zuerst hier ein. | alle Sitzungen |
| `LOG.md` | Übergaben und Reviews, neueste oben. Nur ergänzen, nichts umschreiben. | alle Sitzungen |
| `erster-lauf/STAND.md` | Wie weit der erste Lauf erzählt ist, nächste freie Quellennummer, Datenstand, Formen und Figuren des Tagebuchs. | wer ein Kapitel abschließt |
| `erster-lauf/fakten/kapitel-N.md` | Faktenblatt je Kapitel aus dem Anno-Monitor, für den Spielzeitraum des Kapitels. Erzeugt von einem Skript, nicht von Hand ändern. | Skript |
| `../lore/caesia-varilla.md` | Charakterdossier der Protagonistin Caesia Varilla: verbindlicher Kanon des Spielers. Das Tagebuch hält sich daran; Offenes bleibt offen. | Spieler |

## Ablauf einer Sitzung

1. **Aktualisieren:** `git fetch origin` und `git merge --ff-only origin/main`. Andere Sitzungen schieben parallel.
2. **Lesen:** `AUFGABEN.md`, die obersten Einträge in `LOG.md`, den `STAND.md` der Partie.
3. **Eintragen:** Aufgabe unter „In Arbeit“ mit Wer, Datum und Dateien. Solange dort jemand für eine Datei eingetragen ist, ändert niemand sonst sie. `chronik.html` und `data/events.json` einer Partie gelten zusammen als eine Einheit.
4. **Arbeiten** nach den Regeln der Partie (`docs/<PARTIE>.md`).
5. **Prüfen:** mindestens `node scripts/validate-data.mjs`.
6. **Abschließen:** Aufgabe nach „Erledigt“ (mit Commit) oder nach „Zur Prüfung“, `STAND.md` nachziehen, Übergabe oben in `LOG.md`.
7. **Hochladen nur mit Freigabe des Spielers.** Vor dem Push erneut `git fetch`; ist `origin/main` weiter, zusammenführen. Kein `--force`, keine fremden Commits umschreiben.

## Regeln für alle

- **Wortlaut:** Veröffentlichte Kapitel nicht umschreiben. Ausnahme: ein Fehler. Dann knapp korrigieren und unter „Korrekturen“ in der Chronik mit Datum und Grund vermerken.
- **Register:** `data/events.json` ist append-only. Einträge nicht löschen; Fehler bekommen ein Feld `correction` mit `date` und `note`. Ins Register kommt nur Belegtes (`fakt`) und Abgeleitetes (`rekonstruktion`); Erzähltes steht im Tagebuch.
- **Zahlen** nur aus Messungen, Faktenblättern, Bildschirmfotos oder Angaben des Spielers. Fehlt etwas, bleibt es offen und kommt unter „Offene Fragen“.
- **Zeit:** Anno hat kein Kalenderdatum. Angaben sind Spielzeit der Partie („3:20 h“), daneben steht der Tag der Aufnahme. Erfundene Tageszählungen gibt es keine.
- **Neuladen:** Springt die Spielzeit zurück, gehören die Messungen dahinter zu einem verworfenen Abschnitt. Sie kommen weder in die Chronik noch in die veröffentlichten Messdaten.
- **Namen** von Inseln, Städten und Figuren erst nach Bestätigung des Spielers; was er im Spiel vergibt, gilt als bestätigt.
- **Quellen:** Nummern (Q1, Q2, …) vergibt, wer ein Kapitel schreibt. Die nächste freie Nummer steht im `STAND.md` der Partie.
- **Bilder** unter `saves/<partie>/images/`, nur eigene Bilder oder Bildschirmfotos mit Freigabe des Spielers; keine Spielgrafik (Porträts, Artwork, Ladebilder). KI-Bilder als solche kennzeichnen.
- **Keine Zukunft:** Keine Sitzung plant, was in der Partie passieren wird. Der Spieler spielt, die Chronik folgt.
- **Partien getrennt:** Nichts aus einer Partie in eine andere übernehmen.

## Wer was kann

- **Claude** (Claude Code auf dem Rechner des Spielers) kommt an den Anno-Monitor: lädt Messdaten hoch (`scripts/publish-monitor.py`), erzeugt Faktenblätter, schreibt Kapitel.
- **Codex** hat in der Regel nur dieses Repo. Prüft Kapitel gegen Faktenblätter, Messdaten und Register (Zahlen, Spielzeiten, Textarten, Regeln), schreibt auf Absprache auch Kapitel. Messdaten erzeugt Codex nicht selbst; fehlt ein Faktenblatt, kommt das als Aufgabe für Claude auf die Tafel.

## Review-Format

Wer prüft, schreibt in `LOG.md` einen Eintrag „Review“ mit Fundstellen: Datei, Abschnitt, was steht, was die Quelle sagt, Vorschlag. Ändern darf die Sitzung, die die Datei unter „In Arbeit“ hält, oder nach Absprache die prüfende.
