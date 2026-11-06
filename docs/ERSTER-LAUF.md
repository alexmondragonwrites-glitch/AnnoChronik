# Caesia Varilla · Erster Lauf

Erste Partie der AnnoChronik, angelegt am 5.11.2026 mit Update 3.0 und allen drei Erweiterungen; im Spielstand heißt die Partie „Caesia Varilla“, das Profil der Einstellungsübersicht „Cassandra“. Erzählt wird sie im Tagebuch der Protagonistin Caesia Varilla. Ihr Charakterdossier `lore/caesia-varilla.md` ist der verbindliche Kanon des Spielers (Wunsch vom 5.11.2026: „verbindliche Charaktergrundlage“; „Ihre weitere Geschichte entwickeln wir anhand des tatsächlichen Spielverlaufs. das ist der erste lauf“). Wer gerade woran schreibt und wie weit erzählt ist: `werkstatt/erster-lauf/STAND.md` und `werkstatt/AUFGABEN.md`. Die Entscheidungen des Briefings stehen in `BRIEFING.md`.

## Wo was liegt

| Datei | Inhalt |
|---|---|
| `saves/erster-lauf/chronik.html` | Die Chronik: Titelblatt, die Protagonistin (Figurenkanon), Steckbrief der Partie, Register, Tagebuch (Kapitel), Inseln und Provinzen, offene Fragen, Quellen, Korrekturen. Handgeschrieben. |
| `lore/caesia-varilla.md` | Charakterdossier des Spielers, verbindlicher Kanon. Ändert nur der Spieler oder eine Sitzung auf seinen Wunsch. |
| `saves/erster-lauf/data/events.json` | Register, einzige Quelle für die Registertabelle. Append-only. |
| `saves/erster-lauf/data/meta.json` | Protagonistin, Profil, Schwierigkeit, Erweiterungen, Praetoren, Weltkennung im Monitor. |
| `saves/erster-lauf/data/manifest.json` | `latestReport` (Seite der Chronik) und `monitor` (Messdaten). |
| `saves/erster-lauf/data/monitor/` | Messdaten aus dem Anno-Monitor, geschrieben von `scripts/publish-monitor.py`. Nicht von Hand ändern. |
| `werkstatt/erster-lauf/fakten/kapitel-N.md` | Faktenblatt je Kapitel aus dem Monitor. Nicht von Hand ändern. |
| `saves/erster-lauf/karte.html`, `data/karte.json`, `images/karte/` | Karte von Latium, je Kapitel ein Stand, gezeichnet von `karte.py` im Anno-Monitor (siehe `docs/KARTE.md`). Den Block in `karte.html` und die Bilder nicht von Hand ändern; Umbenennungen in `karte.json` von Hand. |

## Caesia Varilla und ihr Kanon

Aus dem Dossier gelten für die Chronik (Leitlinien des Spielers):

1. **Kanon von Möglichkeiten trennen.** Festgelegt sind Steckbrief, Wesen, Familie und Verlobung in den Teilen, die das Dossier festlegt, und die Ereignisse der Nacht der Flucht. Was es offen nennt, bleibt offen, bis der Spieler oder die Partie es klärt: Mutter, Vater (endgültiger Name, wahre Rolle; der Name „Lucius Caesius Varus“ ist nur ein Vorschlag), Retter und seine Beweggründe, wer die Villa anzündete, Name und Tod des Verlobten, die Piratenverbindung (eine Vermutung), Startinsel und Landungsort, Caesias politische Zukunft.
2. **Keine vorbestimmte Heldin.** Ob und wie sie zur Anführerin wird, ihre Entscheidungen und Konflikte ergeben sich aus dem tatsächlichen Spielverlauf.
3. **Kein Amt behaupten.** Eine formelle Statthalterschaft einer Frau wäre 117 n. Chr. außergewöhnlich; die Chronik nennt sie weder Statthalterin noch gibt sie ihr ein anderes Amt, solange die Geschichte das nicht ergibt.
4. **Ton:** menschlich, differenziert, beobachtend; keine pathetischen Heldensprüche.
5. **Beginn:** Rom und Flucht sind Vorgeschichte (Abschnitt „Die Protagonistin“). Inselwahl, Landung, Gründung und alles Weitere erzählt das Tagebuch erst, wenn es im Spiel geschehen ist.
6. **Das Dossier ist Figurenreferenz,** kein fertiges Kapitel. Die Seite gibt es als Figurenkanon wieder (Etikett „Figurenkanon“, Quelle Q4), mit seinen offenen Punkten unter „Offene Fragen“.

Was ihr Wesen fürs Erzählen hergibt: Sie rechnet, zählt und prüft gern. Ihre Einträge dürfen Vorräte, Bewohner, Waren und Geld in ihre Rechnungen und Listen nehmen, genau mit den gemessenen Zahlen. Unsicherheit zeigt sich bei ihr als Frage, die sich prüfen lässt.

## Kapitel nach Einschnitten im Spiel

Entscheidung des Spielers vom 5.11.2026: Kapitel enden mit Meilensteinen der Partie. Anno hat kein Kalenderdatum, deshalb trägt jedes Kapitel einen Stichtag in Spielzeit.

- Ein Kapitel schließt mit einem Einschnitt der Partie, etwa:
  - den ersten Bewohnern einer neuen Bevölkerungsstufe;
  - einer neuen Insel oder Provinz (Latium, Albion, Aegyptus);
  - einem höheren Stadtstatus;
  - einem fertigen großen Bauwerk.
- Claude schlägt den Einschnitt aus dem Faktenblatt vor, der Spieler bestätigt. Will er früher schließen, gilt sein Wort.
- Stichtag: Spielzeit der letzten verwendeten Messung und deren Aufnahmezeit. Der Spieler spielt beim Schreiben weiter.
- In den Texten heißt der Einschnitt, was er ist („die ersten Plebejer“). Das Wort „Meilenstein“ meiden.

Aufbau eines Kapitels: `<article class="ac-kapitel" id="kapitel-N" data-spielzeit-bis="…">` in `#kapitel`, mit

1. Kopf: römische Kapitelnummer, Titel, Spielzeitraum („0:00 bis 3:20 h Spielzeit“) und Tag der Aufnahme.
2. Bericht (`div.ac-bericht`, Etikett „Belegt“): Kennzahlen des Kapitels mit Quelle (`a.ac-q`). Nur Zahlen, die im Faktenblatt oder in den Messdaten stehen.
3. Tagebuch (`div.ac-tagebuch`, Etikett „Tagebuch“): Caesias Einträge, je Eintrag eine Überschrift aus dem Geschehen und die Spielzeit klein am Rand (`span.ac-rand`). Jahreszahlen nur, wo der Kanon sie gibt (117 n. Chr. zu Beginn); erfundene Tageszählungen gibt es keine.
4. Abgeleitetes als Randnotiz (`p.ac-randnotiz`, Etikett „Abgeleitet“).
5. Registereinträge in `data/events.json` für das Belegte und Abgeleitete des Kapitels.
6. Kartenstand: im Anno-Monitor `py -3 karte.py --save erster-lauf`, nachdem das Kapitel mit `data-spielzeit-bis` in der Chronik steht (siehe `docs/KARTE.md`).

## Ereignisse und Entscheidungen im Spiel

Wunsch des Spielers vom 5.11.2026 („nehmen wir sowas auch mit auf?“, zum Ereignis „Ein Libertus grüßt dich“): Ereignisse mit einer Entscheidung gehören in die Chronik.

- Seit 5.11.2026 erfasst der Anno-Monitor Entscheidungen selbst: Der Spielstand führt jede beendete Entscheidung mit der gewählten Folge, die Texte (Titel, Wahlmöglichkeiten, Kosten, Wirkung) kommen aus den Spieldaten, das Spielprotokoll gibt den Moment des Ereignisfensters. Die Chronikzeile steht in den Messdaten (`art: entscheidung`, Quelle Q3).
- Bildschirmfotos aus dem Spiel (Taste im Spiel) ordnet der Monitor der Entscheidung zu; sie zeigen den Wortlaut und bleiben beim Spieler, weil sie Spielgrafik zeigen. Der Spieltext wird zusammengefasst, nicht abgeschrieben; die Namen der Wahlmöglichkeiten dürfen stehen.
- Ins Register (`kind: fakt`, `category: entscheidung`): Anlass, die Wahlmöglichkeiten, die Wahl und ihr Ergebnis (Kosten, Waren, Ziel). Dazu die Spielzeit aus den Messungen davor und danach, wenn das Bild keine zeigt.
- Ebenso aus dem Monitor: Erkundung (entdeckte Inseln je Provinz) und Inselnahmen von Caesia und den Praetoren. Das Register übernimmt davon, was ein Kapitel braucht.
- Im Tagebuch erzählt Caesia, wie sie entschieden hat und warum, in ihrer Stimme und nach ihrem Wesen. Nennt das Spiel sie dabei mit einem Titel (beim Libertus „Praetor“), hält die Chronik das als Anrede fest; ein Amt folgt daraus erst, wenn die Geschichte es ergibt.

## Das Tagebuch

- Ich-Form, in Caesias Stimme nach dem Dossier.
- Was sie über Bewohner, Bauten, Inseln, Waren und Geld schreibt, folgt den Messungen. Gedanken, Begegnungen, Briefe, Wetter und Alltag sind Erzählung. Erfundene Menschen und Zitate stehen nur im Tagebuch, nie im Register; wer wiederkehrt, kommt in `STAND.md`.
- Gekennzeichnet wird am Kapitel (Etikett „Tagebuch“, Bezug auf die Messungen). Im Text selbst steht keine Metasprache wie „in dieser erfundenen Szene“.
- Formen innerhalb des Tagebuchs wechseln: datierter Eintrag, eingelegter Brief, Liste, Rechnung, Notiz am Rand, Abschrift einer Bauinschrift, Opfergabe, beschriebene Skizze, Gespräch am Hafen. Dieselbe Form höchstens zweimal hintereinander. Formen und wiederkehrende Figuren in `STAND.md` nachhalten.
- Figuren haben ein Gedächtnis: der Kapitän, die Männer an Bord, später Bewohner und Händler, die Praetoren als Rivalen (mit ihren Spielnamen; was sie tun, nur nach Messung). Orte haben Charakter, Alltag hat Platz.
- Schreibweise wie in allen Chroniken des Spielers: natürlich und positiv formuliert. Verneinungsfiguren („nicht X, sondern Y“, „kein …“, „niemand …“) und KI-Phrasen meiden (zeugt von, markiert, geprägt, spürbar, Herzstück, Wendepunkt, bemerkenswert, weise Schlusssätze, Dreierreihen). Neue Abschnitte mit `grep -n -w -E "nicht|kein|keine|nie|niemand|nichts|sondern|ohne"` prüfen.
- Neuladen, Rücksprünge und verworfene Abschnitte kommen in keiner Geschichte vor.

## Erscheinungsbild „römisch“

Leitbild Bauinschrift und Pergament (`assets/roemisch.css`, Klassen mit `ac-`).

- Schriften lokal unter SIL OFL: Cormorant in Versalien für Titel und Kapitelnummern, EB Garamond im Text mit Mediävalziffern; in Versalzeilen, Tabellen und Kennzahlen Versalziffern.
- Farben als Variablen: Pergament (`--ac-paper`), Bericht (`--ac-paper-2`), Tagebuch (`--ac-paper-3`), Tinte (`--ac-ink`), Terrakotta für Kopf und Fuß (`--ac-terra`), Purpur für Tagebuch, Figurenkanon und Initialen (`--ac-purpur`), Bronze für Linien und Ornamente (`--ac-bronze`, für kleine Schrift `--ac-bronze-text`). Im Dunkelmodus Basalt und Elfenbein.
- Textarten: Bericht (`.ac-bericht`, Bronze-Doppellinie), Figurenkanon (`.ac-kanon`, Purpur-Doppellinie), Tagebuch (`.ac-tagebuch`, getöntes Pergament mit Schmuckinitiale), Randnotiz (`.ac-randnotiz`).
- Ornamente als SVG-Masken aus `scripts/ornamente.py`: Lorbeerkranz (`.ac-lorbeer`) über den Titeln, Mäanderband (`.ac-maeander`) unter Überschriften, in Kopf und Fuß; ❦ schließt jeden Abschnitt. Für Kapitel in Aegyptus später Lotus und Papyrus.

## Regeln aus dem Auftrag des Spielers

1. Belegtes, Abgeleitetes, Figurenkanon und Erzähltes trennen.
2. Keine Bevölkerungszahlen, Geldwerte, Mengen, Bauzeiten oder Handelswege erfinden. Fehlendes bleibt offen.
3. Spielzeit und Tag der Aufnahme immer getrennt nennen.
4. Namen von Inseln, Städten und Figuren erst nach Bestätigung; was der Spieler im Spiel vergibt oder im Dossier festlegt, gilt als bestätigt. Umbenannte Inseln führt der Monitor mit dem Namen aus dem Spiel.
5. Spielgrafik (Profilbild, Porträts der Praetoren, Artwork) kommt nicht auf die Seite.
6. Widersprüche benennen und nachvollziehbar korrigieren.

## Anno-Monitor

Weltkennung `anno117-<Partie-Kennung>` aus dem ersten Autosave; bis dahin `world_id: null` in `data/monitor-sources.json`, und das Hochlade-Skript sucht die Partie über ihren Ordner „Caesia Varilla“ (seit dem ersten Autosave eingetragen: `anno117-1793890256`). Hochladen: `WEBSITE_AKTUALISIEREN.bat` im Anno-Monitor oder `py -3 scripts/publish-monitor.py --save erster-lauf`, nur mit Freigabe des Spielers. Einzelheiten: `docs/MONITOR.md`.
