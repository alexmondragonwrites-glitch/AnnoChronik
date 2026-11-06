# AnnoChronik – Briefing

Stand 5.11.2026, 15:30. Freigegeben vom Spieler am 5.11.2026 („Ja, bauen“); das Gerüst steht seit 16:00, siehe `werkstatt/LOG.md`.

## Ziel

Eine öffentliche Chronik der eigenen Anno-117-Partien auf GitHub Pages, aufgebaut wie die Transport Fever Chronicles (`E:\KI-Projekte\Transport-Fever-Chronicles`). Erste Welt ist die neue Partie vom 5.11.2026:

- Profil „Cassandra“, Update 3.0, alle drei Erweiterungen aktiv (Vulkan, Hippodrom, Aegyptus).
- Schwierigkeit „Erfahren“: Baukostenerstattung Hälfte, Startflotte Flaggschiff, Fruchtbarkeiten und Vorkommen normal, Zwischenfälle mittel.
- Praetoren: Tarragon, Athr Iorgwyn, Zara Nitu.

Repo: https://github.com/alexmondragonwrites-glitch/AnnoChronik (öffentlich, am 5.11. noch leer). Seite später: https://alexmondragonwrites-glitch.github.io/AnnoChronik/

## Entschieden (Spieler, 5.11.2026)

| Frage | Antwort |
|---|---|
| Kapitel | nach Meilensteinen im Spiel, Stichtag nach Spielzeit |
| Erzählweise | „Tagebuch der Protagonistin, der Char ich gerade entwickel“ |
| Aussehen | eigenes, römisches Erscheinungsbild |
| Messdaten | geprüft im Repo, sie tragen die Kapitel; eine Datenansicht kann später kommen |

## Was aus den Transport Fever Chronicles übernommen wird

- Statische Seite ohne Framework und Backend, Schriften lokal, keine Anfragen an fremde Server, hell und dunkel, Handy und PC.
- Weltportal `index.html` und je Partie ein eigener Ordner `saves/<welt>/` mit eigener Adresse; Weltregister `data/worlds.json`.
- Je Welt `data/meta.json`, `data/manifest.json`, das Register `data/events.json` (nur anhängen) und `data/monitor/` mit den Messdaten.
- Werkstatt für Claude und Codex: `werkstatt/README.md`, `AUFGABEN.md` (wer woran arbeitet), `LOG.md` (Übergaben, neueste oben), je Welt `STAND.md` und `fakten/`.
- `AGENTS.md` (für alle KI-Sitzungen), `CLAUDE.md` (nur Claude: Wege zum Anno-Monitor), Regeln der Welt in `docs/<WELT>.md`.
- GitHub Actions „Datenqualität“ prüft bei jedem Push Daten und Skripte; ausgeliefert wird über „Deploy from a branch“ (`main`, Ordner `/`).
- Regeln:
  - Belegt, Abgeleitet und Erzählung trennen.
  - Zahlen nur aus Messungen, Faktenblättern, Bildschirmfotos oder Angaben des Spielers.
  - Namen gelten erst nach Bestätigung des Spielers; was er im Spiel benennt, gilt als bestätigt.
  - Veröffentlichten Wortlaut nur zur Korrektur eines Fehlers ändern, mit Eintrag unter „Korrekturen“.
  - Neuladen wird nicht erzählt.
  - Keine Sitzung plant die Zukunft der Welt: Der Spieler spielt, die Chronik folgt.
- Hochladen nur mit Freigabe des Spielers („Ja, hochladen“).

## Was bei Anno anders ist

- **Zeit:** Anno hat kein Kalenderdatum. Die Zeitachse ist die Spielzeit der Partie (Spieluhr `GameTotal`, angegeben als „12:40 h Spielzeit“), daneben steht immer das reale Aufnahmedatum.
- **Weltkennung:** `anno117-<Partie-Kennung>` aus dem ersten Autosave. Vorher kennt der Monitor nur eine vorläufige Live-Welt; ab dem ersten Autosave gehört alles zur Welt des Spielstands (seit 5.11.2026 so im Monitor).
- **Quellen:** Autosaves (beim Spieler etwa alle 5 Minuten) und der Live-Mod (Grundwerte alle 10 s, Details alle 60 s). Erzeugung und Verbrauch, andere Provinzen und die Rivalen stehen nur in den Autosaves.
- **Datenschutz:** Die Messungen enthalten lokale Pfade und den Ordner mit der Kontokennung des Spielers. Das Hochlade-Skript lässt Pfade, Konto und Dateinamen weg; das Prüfskript schlägt an, wenn doch etwas davon im Repo landet.
- **Spielgrafik:** Profilbild, Porträts der Praetoren und Artwork aus dem Spiel kommen nicht auf die öffentliche Seite. Eigene Bildschirmfotos nur, wenn der Spieler sie dafür freigibt.

## Kapitel nach Einschnitten im Spiel

- Ein Kapitel schließt mit einem Einschnitt der Partie, zum Beispiel:
  - die ersten Bewohner einer neuen Bevölkerungsstufe;
  - eine neue Insel oder eine neue Provinz (Latium, Albion, Aegyptus);
  - ein höherer Stadtstatus;
  - ein großes Bauprojekt ist fertig, etwa die Pyramide.
- Claude schlägt den Einschnitt aus dem Faktenblatt vor, der Spieler bestätigt ihn. Will er ein Kapitel früher schließen, gilt sein Wort.
- Jedes Kapitel hat einen Stichtag: die Spielzeit der letzten verwendeten Messung und deren Aufnahmezeit. Der Spieler spielt beim Schreiben weiter.
- Faktenblatt je Kapitel: `werkstatt/<welt>/fakten/kapitel-N.md`, erzeugt aus dem Monitor für den Spielzeitraum des Kapitels. Es enthält Bevölkerung je Stufe und Insel, Geld und Bilanz, Bedürfnisse, Lager, Betriebe, neue Inseln, Stadtstatus und Rivalen.
- In den Texten heißt der Einschnitt, was er ist („die ersten Plebejer“); das Wort „Meilenstein“ meiden (steht auf der Liste der KI-Wörter).

## Tagebuch der Protagonistin

- Jedes Kapitel besteht aus Tagebucheinträgen der Protagonistin in der Ich-Form und einem knappen Bericht. Der Bericht (Belegt) bringt die Kennzahlen des Kapitels mit Spielzeit und Quelle, Abgeleitetes steht als Randnotiz.
- Das Tagebuch ist Erzählung. Gekennzeichnet wird es am Kapitel (Etikett „Tagebuch“ und ein Bezug: welche Messungen); der Text selbst erzählt unmittelbar, ohne Metasprache.
- Was sie über Bewohner, Bauten, Inseln und Geld schreibt, folgt den Messungen. Ihre Gedanken, Begegnungen, Briefe und das Wetter sind Erzählung. Erfundene Menschen und Zitate stehen nur im Tagebuch, nie im Register.
- Formen innerhalb des Tagebuchs wechseln, zum Beispiel:
  - ein eingelegter Brief an den Kaiser oder an die Familie;
  - eine Liste oder eine Notiz am Rand;
  - die Abschrift einer Bauinschrift, eine Opfergabe, eine Rechnung;
  - eine beschriebene Skizze, ein Gespräch am Hafen.
- Formen und wiederkehrende Figuren hält `STAND.md` fest. Die Figuren haben ein Gedächtnis: Bewohner, Händler, die Praetoren als Rivalen. Orte haben Charakter, auch Alltag hat Platz.
- Schreibweise wie in allen Chroniken des Spielers: natürlich und positiv formuliert, ohne Verneinungsfiguren („nicht X, sondern Y“) und KI-Phrasen, mit grep-Prüfung.
- **Datierung (Vorschlag):** Jeder Eintrag bekommt eine Überschrift aus dem Geschehen („Als die ersten Plebejer kamen“), die Spielzeit steht klein am Rand als Quelle. Erfundene Tageszählungen braucht es so keine.
- **Vom Spieler:** der Steckbrief der Protagonistin: Name, Herkunft, Wesen, Stimme und was sie antreibt. Sein Text steht im Wortlaut in `werkstatt/<welt>/protagonistin.md`, so wie die Gründungsgeschichte in Erlental.

## Erscheinungsbild „römisch“

- Leitbild: Bauinschrift und Pergament.
- Schriften, lokal und unter SIL OFL:
  - Capitalis für Titel und Kapitelnummern (Cinzel);
  - EB Garamond im Text (liegt schon in der TF3-Chronik);
  - römische Ziffern für die Kapitel.
- Farben:
  - Pergament und Marmor als Papier, Tinte in Sepia-Schwarz;
  - Terrakotta für Kopf und Fuß, Purpur für Tagebuch und Initialen, Bronze für Linien und Rahmen;
  - im Dunkelmodus Basalt mit Elfenbeinschrift.
- Ornamente als SVG: Mäanderband und Lorbeer; für Kapitel in Aegyptus später Lotus und Papyrus mit Lapislazuli.
- Textarten:
  - Tagebuch auf getöntem Pergament mit Schmuckinitiale;
  - Bericht hell mit Doppellinie und Quellenvermerk;
  - Abgeleitetes als Randnotiz.
- Kontrast nach WCAG AA, geprüft am Handy und am PC, hell und dunkel.

## Aufbau des Repos (Vorschlag)

```text
AnnoChronik/
├── index.html                  # Portal: alle Welten
├── assets/                     # roemisch.css, Schriften, Ornamente, chronik.js (Register, Kapitelnavigation)
├── data/worlds.json            # Weltregister
├── data/monitor-sources.json   # welche Monitor-Welt zu welchem Ordner gehört
├── saves/<welt>/
│   ├── index.html              # leitet auf die Chronik
│   ├── chronik.html            # Titelblatt, Steckbrief, Register, Kapitel, Inseln, Bevölkerung, offene Fragen, Quellen, Korrekturen
│   └── data/                   # meta.json, manifest.json, events.json, monitor/
├── werkstatt/                  # README, AUFGABEN, LOG, <welt>/STAND.md, <welt>/fakten/, <welt>/protagonistin.md
├── docs/                       # ARCHITECTURE.md, MONITOR.md, <WELT>.md
├── scripts/                    # publish-monitor.py, fakten.py, validate-data.mjs, new-save.mjs
├── .github/workflows/validate.yml
├── AGENTS.md, CLAUDE.md, README.md
└── BRIEFING.md                 # diese Datei
```

## Datenweg

1. Der Anno-Monitor schreibt `sessions/*/daten.jsonl` (vollständige Messungen) und `history/welten/<welt>/`.
2. `scripts/publish-monitor.py --save <welt>` nimmt nur die Messungen dieser Weltkennung, lässt Pfade und Konto weg und schreibt `saves/<welt>/data/monitor/`: je Monitorlauf ein Abschnitt und ein kleines `index.json`. Unveränderte Abschnitte bleiben byte-gleich, ein Upload enthält also meist nur den laufenden Abschnitt. Verworfene Abschnitte nach einem Neuladen bleiben als solche markiert.
3. Danach laufen die Prüfskripte, das Skript zeigt die Änderungen und committet und pusht erst nach Bestätigung.
4. Im Anno-Monitor kommt dazu `WEBSITE_AKTUALISIEREN.bat`, wie im TF3-Spielmonitor.

## Erster Bau nach Freigabe

1. Gerüst: Portal, Weltseite mit Titelblatt und leerem Kapitelteil, das römische Design mit Schriften und Ornamenten.
2. Prüfskripte und die Action „Datenqualität“, Werkstatt, Doku, `AGENTS.md` und `CLAUDE.md`.
3. Hochlade-Skript mit Datenschutzfilter, `WEBSITE_AKTUALISIEREN.bat` im Anno-Monitor; der erste Upload der Messdaten nach dem ersten Autosave.
4. Lokal prüfen (Browser, Handy, dunkel), dann Freigabe für den ersten Push. Danach schaltet der Spieler Pages ein: Repo-Einstellungen → Pages → „Deploy from a branch“, `main`, `/`.
5. Kapitel I entsteht nach dem ersten Einschnitt und dem Steckbrief der Protagonistin.

## Karte (Spieler, 6.11.2026)

Wunsch des Spielers: „gibs auch wieder die möglichkeit ener karte? wie brauchen es nicht so auffwendig wie in tf3 aber hübsch sollte sie trtzdem sein eher so wie iene landkkarte“. Darauf eine Probekarte von Latium aus dem Spielstand bei 163:52 min; den Vorschlag hat der Spieler am 6.11.2026 freigegeben („Ja, so bauen“).

- Eigene Kartenseite `saves/erster-lauf/karte.html` mit einem Kartenstand je Kapitel. Knöpfe wählen das Kapitel, ein Klick öffnet die Karte in voller Größe. Kein 3D, keine Kacheln: je Kapitel ein Bild.
- Je Kapitel der letzte Spielstand vor dem Einschnitt; die Kartusche nennt dessen Spielzeit und den Tag der Aufnahme.
- Gezeichnet im Stil der Chronik:
  - Pergament, Wasserlinien an den Küsten, Schummerung, Wald als Baumkronen, Flüsse;
  - Straßen rot wie auf der Tabula Peutingeriana, Häuser und Betriebe als kleine Blöcke;
  - Besitz als Grenzkolorit, Caesia in Purpur, die Praetoren in eigenen Farben;
  - unentdeckte Inseln nur gepunktet umrissen, ohne Namen;
  - Kartusche, Windrose, Maßstab in Feldern.
- Namen wie im Spiel; Umbenennungen des Spielers gelten ab ihrem Zeitpunkt (Lorica, ab 126:05 min Olivaria).
- Quellen: Lage, Bauten, Straßen, Besitz und Entdeckung aus dem Spielstand; Küsten, Höhen, Flüsse und Wald aus den Inseldateien des Spiels. Veröffentlicht wird nur die eigene Zeichnung, keine Spielgrafik; die Inseldaten bleiben lokal beim Anno-Monitor.
- Weitere Provinzen kommen dazu, sobald Caesia dort etwas entdeckt (Albion: bis 165:38 min nichts entdeckt).
- Werkzeug `karte.py` im Anno-Monitor, Doku in `docs/KARTE.md`; hochladen nur mit Freigabe.

## Offen

- Steckbrief der Protagonistin (Spieler).
- Name der Welt und der Chronik: Vorschlag nach der ersten Stadt oder der Startprovinz, bis dahin ein Arbeitstitel.
- Datierung der Tagebucheinträge (Vorschlag oben).
- Startprovinz und Name der ersten Insel kommen aus dem Spiel.
- Ob die Praetoren im Tagebuch auftreten dürfen. Vorschlag: ja, mit ihren Spielnamen; was sie tun, nur nach Messung.
