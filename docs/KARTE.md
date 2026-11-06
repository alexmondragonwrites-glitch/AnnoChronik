# Karte

Die Kartenseite `saves/<partie>/karte.html` zeigt die Provinz zum Ende jedes Kapitels, je Kapitel einen Kartenstand. Wunsch des Spielers vom 6.11.2026: „nicht so aufwendig wie in tf3 aber hübsch … eher so wie eine landkarte“; freigegeben mit „Ja, so bauen“ (siehe `BRIEFING.md`, Abschnitt Karte).

## Was die Karte zeigt

- **Aus dem Spielstand:**
  - Lage und Drehung jeder Insel (`MapTemplate`);
  - Wohnhäuser, Betriebe und Lager, Straßen;
  - wem eine Fläche gehört (wie im Anno-Monitor: die meisten Wohnhäuser, Betriebe und Lager);
  - welche Inseln Caesia entdeckt hat (`DiscoveredIslands4`).
- **Aus den Inseldaten des Spiels:** Küsten und Höhen, Flüsse, Wald (aus der Vorlage der Insel; wo gebaut ist, fehlt er) und die Flächen einer Insel.
- **Unentdeckte Inseln** erscheinen nur gepunktet umrissen, ohne Namen, Besitz und Bauten.
- **Namen** wie im Spiel. Umbenennungen des Spielers stehen in `data/karte.json` unter `umbenennungen` und gelten ab `ab_ms`, denn der Spielstand führt nur den Originalnamen.
- **Zeichen:** Kartusche mit Spielzeit des Spielstands und Tag der Aufnahme, Legende, Windrose, Maßstab in Feldern.

Gezeichnet wird für die Chronik: Pergament, Wasserlinien, Schummerung, Farben, Schrift (Cormorant, EB Garamond). Bilder aus dem Spiel sind nicht verwendet. Die Inseldaten bleiben beim Anno-Monitor im lokalen Zwischenspeicher.

## Kartenstand je Kapitel

- Jeder Kartenstand folgt dem **letzten Spielstand vor dem Einschnitt** des Kapitels (`data-spielzeit-bis` im Kapitel von `chronik.html`), der noch im Kapitel liegt.
- Spielstände eines verworfenen Abschnitts (nach einem Neuladen) zählen nicht.
- Der Anno-Monitor sucht im Spielordner und in seinen lokalen Sicherungen. Das Spiel löscht alte Autosaves, deshalb sichert das Werkzeug jeden Spielstand, nach dem es eine Karte zeichnet.
- Provinzen, in denen Caesia noch nichts entdeckt hat, bekommen keine Karte.

## Dateien

| Datei | Inhalt |
|---|---|
| `saves/<partie>/karte.html` | Seite; der Block zwischen `<!-- KARTE:ANFANG … -->` und `<!-- KARTE:ENDE -->` wird vom Werkzeug geschrieben. |
| `saves/<partie>/data/karte.json` | Kartenstände (Kapitel, Spielzeiten, Bilder, Inseln je Besitzer, Legende) und Umbenennungen. |
| `saves/<partie>/images/karte/kapitel-N.webp` | Karte in voller Größe (etwa 0,7 MB); `kapitel-N-klein.webp` für die Seite. |
| `assets/karte.js` | Kapitelwahl ohne Neuladen; ohne JavaScript stehen alle Stände untereinander. |

`scripts/validate-data.mjs` prüft die Kartenstände: Bilder vorhanden und höchstens 3 MB groß, Spielstand im Kapitel, Kapitel in der Chronik, Seite aktuell, keine Kontokennung in den Bildern.

## Nach jedem Kapitel (Claude)

1. Das Kapitel steht in `chronik.html` mit `data-spielzeit-bis`.
2. Hat der Spieler eine Insel umbenannt, kommt sie in `data/karte.json` unter `umbenennungen` (`bereich`, `vorher`, `name`, `ab_ms`, `quelle`).
3. Im Anno-Monitor: `py -3 karte.py --save erster-lauf`. Das Werkzeug zeichnet fehlende Kapitel und schreibt `karte.json` und den Block in `karte.html`. `--neu N` zeichnet Kapitel N neu, `--alle-neu` alle.
4. Die Karte ansehen, dann `node scripts/validate-data.mjs`.
5. Hochladen mit dem Kapitel, nur mit Freigabe des Spielers.
