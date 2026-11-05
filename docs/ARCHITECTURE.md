# AnnoChronik · Architektur

Ein Repository für beliebig viele Partien in Anno 117: Pax Romana, nach dem Vorbild der Transport Fever Chronicles. Jede Partie hat ein eigenes Verzeichnis, eine eigene Adresse und eine eindeutige Weltkennung aus dem Anno-Monitor. Ausgeliefert wird statisch über GitHub Pages, ohne Framework, Backend oder fremde Server.

## Grundsätze

1. **Daten vor Deutung:** Belegtes, Abgeleitetes und Erzähltes sind sichtbar getrennt.
2. **Archiv statt Überschreiben:** Das Register wächst nur; Messdaten je Aufnahmetag bleiben stehen.
3. **Manifest statt fester Verweise:** `data/manifest.json` jeder Partie nennt die aktuelle Seite und die Messdaten.
4. **Partien getrennt:** gleiche Inselnamen in verschiedenen Partien kollidieren nicht.
5. **Datenschutz:** keine Pfade, Kontokennungen oder Spielgrafik im öffentlichen Repo; geprüft bei jedem Push.
6. **Reproduzierbar:** Prüfskripte und GitHub Actions überwachen Register, Verweise und Messdaten.
7. **Schlank:** reines HTML, CSS und JavaScript, Schriften lokal, hell und dunkel, Handy und PC.

## Repository

```text
/
├── index.html                  # Portal: alle Partien (data/worlds.json)
├── assets/
│   ├── roemisch.css            # Erscheinungsbild „römisch“ (Variablen, Bausteine)
│   ├── chronik.js              # Weltseite: Register, Zeile zu den Messdaten
│   ├── portal.js               # Portal: Karten aus dem Weltregister
│   ├── lorbeer.svg, maeander.svg   # Ornamente (scripts/ornamente.py)
│   └── fonts/                  # EB Garamond, Cormorant (SIL OFL)
├── data/
│   ├── worlds.json             # Weltregister
│   └── monitor-sources.json    # Partie → Weltkennung im Anno-Monitor
├── saves/<partie>/
│   ├── index.html              # leitet auf latestReport
│   ├── chronik.html            # die Chronik
│   └── data/                   # meta.json, manifest.json, events.json, monitor/
├── werkstatt/                  # Abstimmung der KI-Sitzungen (README, AUFGABEN, LOG, <partie>/)
├── scripts/
│   ├── publish-monitor.py      # Messdaten aus dem Anno-Monitor, Upload nach Bestätigung
│   ├── monitor_daten.py        # Verdichten und Datenschutzfilter (getestet in test-monitor-daten.py)
│   ├── validate-data.mjs       # Datenprüfung
│   ├── new-save.mjs            # neue Partie anlegen
│   └── ornamente.py            # Lorbeer und Mäander als SVG
├── docs/                       # ARCHITECTURE.md, MONITOR.md, <PARTIE>.md
├── .github/workflows/validate.yml
└── AGENTS.md, CLAUDE.md, README.md, BRIEFING.md
```

## Datenmodell

- `data/worlds.json`: je Partie `id`, `name`, `path` (`saves/<id>/`), `page`, `status` (`laufend` oder `abgeschlossen`), `started`, `description`.
- `saves/<id>/data/events.json`: je Eintrag `id` (`<partie>-NNNN`), `spielzeit_ms` (Spielzeit der Partie) oder `game_time_label`, `recorded` (Tag der Aufnahme), `kind` (`fakt` = Belegt, `rekonstruktion` = Abgeleitet), `category`, `title`, `description`, `source` (Quellennummern wie `Q1`), optional `chapter` und `correction` (`date`, `note`).
- Messdaten: siehe `docs/MONITOR.md`.

## Neue Partie

```bash
node scripts/new-save.mjs --id neue-partie --name "Neue Partie" --partie "Profilname"
```

Danach ist sie im Portal und im Hochlade-Skript eingetragen; die Weltkennung findet das Skript nach dem ersten Autosave selbst.

## Lokal ansehen und prüfen

```bash
python -m http.server 8000
node scripts/validate-data.mjs
python scripts/test-monitor-daten.py
```

Dann http://localhost:8000 öffnen. Direkte `file://`-Aufrufe laden Register und Messdaten wegen `fetch` nicht.
