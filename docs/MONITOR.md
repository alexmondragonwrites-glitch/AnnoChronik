# Messdaten aus dem Anno-Monitor

Der Anno-Monitor (`E:\KI-Projekte\Anno-Monitor`, lokal beim Spieler) liest die Autosaves der Partie (etwa alle fünf Minuten) und einen Live-Mod (Details alle 60 Sekunden). Er speichert je Welt Kurzwerte, eine Chronik und den letzten vollständigen Stand. `scripts/publish-monitor.py` bringt davon die gültigen Messungen auf die Seite.

## Hochladen

Im Anno-Monitor `WEBSITE_AKTUALISIEREN.bat` doppelklicken, oder hier:

```text
py -3 scripts/publish-monitor.py                  alle Welten aus data/monitor-sources.json, fragt vor dem Upload
py -3 scripts/publish-monitor.py --save erster-lauf nur eine Welt
py -3 scripts/publish-monitor.py --no-push        nur lokal schreiben und prüfen
py -3 scripts/publish-monitor.py --yes            ohne Rückfrage
```

Ablauf: GitHub-Stand nachziehen (nur Fast-Forward), Dateien bauen, auf Privates prüfen, nur geänderte Dateien schreiben, `validate-data.mjs` ausführen, Änderungen zeigen, nach Bestätigung committen und pushen. Schlägt eine Prüfung fehl, wird nichts committet. Ohne neue Messungen entsteht kein Commit.

Hat eine Welt in `data/monitor-sources.json` noch keine `world_id`, sucht das Skript im Monitor die Welt aus Spielständen mit dem Partie-Ordner (`partie`) und trägt die Kennung in `monitor-sources.json` und `meta.json` ein; das Manifest zeigt danach auf `data/monitor/index.json`.

## Was veröffentlicht wird

`saves/<welt>/data/monitor/`:

- `index.json`: Weltkennung, Zahl der Messungen, verworfene Messungen und Neuladen (nur gezählt), Spielzeit von und bis, Aufnahmezeit von und bis, Liste der Tage.
- `tag-JJJJ-MM-TT.json`: je Tag der Aufnahme die Kurzwerte jeder gültigen Messung (Spielzeit, Quelle, Geld, Bilanz je Minute, Bevölkerung gesamt und je Stufe, Bewohner je eigener Insel) und die Chronikzeilen des Monitors (neue Inseln und Stufen, Bevölkerungssprünge, Bedürfnisse, Betriebe, leere Lager).
- `stand.json`: der letzte Stand (Live, ergänzt um den letzten Spielstand, sonst der Spielstand): Geld und Kategorien, Bevölkerung, Attribute, Provinzen, je eigener Insel Stufen, Bedürfnisse, Lager (ohne Nullen), Betriebe und die letzte Spielstatistik, Rivalen; dazu die deutschen Namen der vorkommenden Stufen, Waren und Betriebe aus dem Spielkatalog.

Abgeschlossene Tage bleiben byte-gleich und erscheinen in keinem weiteren Commit. Ein Neuladen im Spiel kann die Datei des laufenden Tages ändern, weil verworfene Messungen herausfallen.

## Was wegbleibt

- Pfade, Dateinamen der Spielstände, Prüfsummen, der Kontoordner und die Kontokennung des Spielers. `monitor_daten.privat_funde` und `validate-data.mjs` schlagen an, wenn doch etwas davon auftaucht.
- Inseln anderer Teilnehmer und der Lagerverlauf der letzten 20 Minuten.
- Verworfene Messungen nach einem Neuladen und die technischen Neuladen-Zeilen.

## Bedeutung und Grenzen

- Bevölkerung: Der Spielwert je Stufe kann von der Summe der Bewohner in Wohnhäusern abweichen; der Monitor führt beides getrennt.
- Erzeugung und Verbrauch stammen aus der Spielstatistik der Autosaves (alle zehn Spielminuten ein Schnappschuss); Handelsrouten und Schiffsladungen fehlen in den Daten.
- Live-Werte haben ihre eigene Uhr: Teile, die aus dem Spielstand ergänzt sind, nennt `stand.json` unter `aus_spielstand` (je Insel) und `ergaenzt_aus`.
