# AnnoChronik

**Chroniken eigener Partien in Anno 117: Pax Romana**, erzählt aus den Messungen des Spiels. Aufgebaut wie die [Transport Fever Chronicles](https://github.com/alexmondragonwrites-glitch/Transport-Fever-Chronicles): statische Seite auf GitHub Pages, Register, Messdaten aus einem eigenen Monitor, Werkstatt für Claude und Codex.

## Partien

- **Caesia Varilla · Erster Lauf** (5.11.2026 begonnen, am 15.11.2026 abgeschlossen, acht Kapitel): erzählt im Tagebuch von Caesia Varilla, die aus Rom flieht; mit Update 3.0 und allen drei Erweiterungen. Figurenkanon: [lore/caesia-varilla.md](lore/caesia-varilla.md). Kapitel enden mit Einschnitten der Partie, etwa einer neuen Bevölkerungsstufe oder Provinz. [Chronik](saves/erster-lauf/chronik.html) · [Regeln](docs/ERSTER-LAUF.md)
- **Antonia Corvina · Zweiter Lauf** (8.11.2026 begonnen, am 15.11.2026 abgeschlossen, elf Kapitel und ein Sonderkapitel): erzählt im Tagebuch von Antonia Corvina, die im kaiserlichen Auftrag Siedlungen gründet und verwaltet; mit Update 3.0. Kanon: [lore/antonia-corvina.md](lore/antonia-corvina.md), [lore/marcus-antonius-felix.md](lore/marcus-antonius-felix.md), [lore/welt-antonia-corvina.md](lore/welt-antonia-corvina.md). [Chronik](saves/zweiter-lauf/chronik.html) · [Regeln](docs/ZWEITER-LAUF.md)
- **Aelwen · Dritter Lauf** (seit 15.11.2026): erzählt im Tagebuch von Aelwen, einer verwitweten Keltin aus Albion, die auf einer abgelegenen Insel beginnt, die Rom ihr überlassen hat; mit Update 3.0 und einem keltischen Erscheinungsbild in Waldgrün und Gold. Kanon: [lore/aelwen.md](lore/aelwen.md), [lore/welt-aelwen.md](lore/welt-aelwen.md). [Chronik](saves/dritter-lauf/chronik.html) · [Regeln](docs/DRITTER-LAUF.md)

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
