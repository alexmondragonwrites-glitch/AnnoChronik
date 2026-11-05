# AnnoChronik

**Chroniken eigener Partien in Anno 117: Pax Romana**, erzählt aus den Messungen des Spiels. Aufgebaut wie die [Transport Fever Chronicles](https://github.com/alexmondragonwrites-glitch/Transport-Fever-Chronicles): statische Seite auf GitHub Pages, Register, Messdaten aus einem eigenen Monitor, Werkstatt für Claude und Codex.

## Partien

- **Caesia Varilla · Erster Lauf** (seit 5.11.2026): erzählt im Tagebuch von Caesia Varilla, die aus Rom flieht; mit Update 3.0 und allen drei Erweiterungen. Figurenkanon: [lore/caesia-varilla.md](lore/caesia-varilla.md). Kapitel enden mit Einschnitten der Partie, etwa einer neuen Bevölkerungsstufe oder Provinz. [Chronik](saves/erster-lauf/chronik.html) · [Regeln](docs/ERSTER-LAUF.md)

## Arbeitsweise

Das Spiel ist die Quelle, die Chronik erzählt. Der Anno-Monitor liest die Autosaves und einen kleinen Mod, der während des Spiels Werte ins Spielprotokoll schreibt. Belegtes, Abgeleitetes und das Tagebuch sind getrennt gekennzeichnet. Anno kennt kein Kalenderdatum: Zeitangaben sind Spielzeit der Partie, daneben steht der Tag der Aufnahme.

- [Architektur](docs/ARCHITECTURE.md) · [Messdaten](docs/MONITOR.md) · [Werkstatt](werkstatt/README.md)

## Lokal ausführen

```bash
python -m http.server 8000
node scripts/validate-data.mjs
python scripts/test-monitor-daten.py
```

Eine private Fan-Chronik, unabhängig von Ubisoft. Anno ist eine Marke von Ubisoft Entertainment. Schriften: EB Garamond und Cormorant unter der SIL Open Font License (`assets/fonts/`).
