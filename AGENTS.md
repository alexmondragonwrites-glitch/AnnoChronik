# AnnoChronik – Hinweise für KI-Sitzungen

Statische Website (GitHub Pages) mit Chroniken eigener Partien in Anno 117: Pax Romana, aufgebaut wie die Transport Fever Chronicles. Erste Partie: Caesia Varilla · Erster Lauf (`saves/erster-lauf/`, seit 5.11.2026, im Spielstand „Caesia Varilla“). Zweite Partie: Antonia Corvina · Zweiter Lauf (`saves/zweiter-lauf/`, seit 8.11.2026). Claude Code und Codex arbeiten daran, auch parallel.

## Zuerst lesen

1. `werkstatt/README.md`: Ablauf, Regeln, wer was kann.
2. `werkstatt/AUFGABEN.md`: wer gerade woran arbeitet. Vor dem Ändern eintragen.
3. Die obersten Einträge in `werkstatt/LOG.md`.
4. Für den ersten Lauf: `werkstatt/erster-lauf/STAND.md`, `docs/ERSTER-LAUF.md` und der verbindliche Figurenkanon `lore/caesia-varilla.md`.
5. Für den zweiten Lauf: `werkstatt/zweiter-lauf/STAND.md`, `docs/ZWEITER-LAUF.md` und der verbindliche Kanon `lore/antonia-corvina.md`, `lore/marcus-antonius-felix.md` und `lore/welt-antonia-corvina.md`.

## Kurzregeln

- Vor dem Arbeiten und vor jedem Push `git fetch origin`; zusammenführen statt überschreiben. Kein `--force`.
- Hochladen nur mit Freigabe des Spielers.
- Keine Zahlen erfinden. Belegt, Abgeleitet und Tagebuch trennen. Namen erst nach Bestätigung des Spielers; was er im Spiel benennt, gilt als bestätigt.
- Anno hat kein Kalenderdatum: Zeitangaben sind Spielzeit der Partie, daneben steht der Tag der Aufnahme.
- Veröffentlichten Wortlaut nur zur Korrektur eines Fehlers ändern, mit Eintrag unter „Korrekturen“. `data/events.json` ist append-only.
- Figuren: `lore/` ist verbindlicher Kanon des Spielers. Offenes bleibt offen; die Geschichte der Figuren entsteht aus dem tatsächlichen Spielverlauf.
- Neuladen (Rücksprung der Spielzeit) wird nicht erzählt.
- Partien nicht vermischen.
- Öffentliches Repo: keine Zugangsdaten, keine lokalen Pfade, keine Kontokennung des Spielers, keine Spielgrafik (Porträts, Artwork).

## Prüfen

```bash
node scripts/validate-data.mjs
python3 scripts/test-monitor-daten.py
```

Weitere Prüfungen laufen in `.github/workflows/validate.yml`.
