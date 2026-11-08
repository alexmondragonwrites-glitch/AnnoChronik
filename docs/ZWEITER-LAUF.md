# Antonia Corvina · Zweiter Lauf

Zweite Partie der AnnoChronik, begonnen am 8.11.2026 mit Update 3.0. Erzählt wird sie im Tagebuch der Protagonistin Antonia Corvina. Die Entscheidungen des Briefings stehen in `BRIEFING.md`, Abschnitt „Zweiter Lauf“. Wie weit erzählt ist: `werkstatt/zweiter-lauf/STAND.md` und `werkstatt/AUFGABEN.md`.

Für Kapitel, Ereignisse und Entscheidungen, Tagebuch, Regeln aus dem Auftrag des Spielers und den Datenweg gilt `docs/ERSTER-LAUF.md` sinngemäß, dazu `docs/SCHREIBSTIL.md`. Hier steht, was im zweiten Lauf anders ist. Die Partien bleiben getrennt: Figuren, Orte und Ereignisse des ersten Laufs kommen hier nicht vor.

## Wo was liegt

| Datei | Inhalt |
|---|---|
| `saves/zweiter-lauf/chronik.html` | Die Chronik: Titelblatt, die Protagonistin und ihr Sekretär (Figurenkanon), Steckbrief der Partie, Register, Tagebuch (Kapitel), Inseln und Provinzen, offene Fragen, Quellen, Korrekturen. Handgeschrieben. |
| `lore/antonia-corvina.md`, `lore/marcus-antonius-felix.md`, `lore/welt-antonia-corvina.md` | Charakterdossiers und Weltentwurf des Spielers, verbindlicher Kanon. Ändert nur der Spieler oder eine Sitzung auf seinen Wunsch. |
| `saves/zweiter-lauf/data/` | `meta.json`, `manifest.json`, `events.json` (Register, append-only), `karte.json`, `monitor/` (Messdaten, von `scripts/publish-monitor.py`). |
| `saves/zweiter-lauf/karte.html`, `images/karte/` | Karte, je Kapitel ein Stand, von `karte.py` im Anno-Monitor (siehe `docs/KARTE.md`). |

## Antonia Corvina und ihr Kanon

1. **Kanon von Möglichkeiten trennen.** Festgelegt ist, was die Dossiers festlegen. Offen bleibt, bis der Spieler oder die Partie es klärt: Antonias Kleidung, körperliche Merkmale und Frisur; ob sie ihre Ungeduld überwindet; der Name ihres Förderers; bei Felix Alter, Geburtsort, die Umstände der Freilassung, sein früheres Leben, seine persönlichen Wünsche, Vorlieben und Schwächen.
2. **Ihr Amt ist festgelegt.** Anders als Caesia hat Antonia die außerordentliche kaiserliche Vollmacht, Siedlungen zu gründen, zu verwalten und Gebiete zu befrieden. Die Ernennung einer Frau ist eine bewusst alternative historische Setzung; sie darf so benannt werden. Ihr Mandat gibt weitreichende Befugnisse und nur begrenzte Mittel und Soldaten.
3. **Beginn:** Die Abreise aus Rom und die gemischte Gruppe aus Vertrauten, Fachleuten und politischen Kontakten sind Vorgeschichte. Ihre erste Priorität in Latium ist eine repräsentative römische Siedlung mit durchdachten Straßen, öffentlichen Gebäuden und einem Verwaltungszentrum. Inselwahl, Gründung und alles Weitere erzählt das Tagebuch erst, wenn es im Spiel geschehen ist.
4. **Felix** ist Sekretär und wiederkehrende Stimme des Tagebuchs: praktisch, skeptisch gegenüber politischen Versprechen, loyal. Antonia wahrt Distanz zu ihm. Er bekommt keine verborgenen Interessen, keine heimliche Vergangenheit und keine eigenen politischen Ambitionen, und er ist weder enger Freund noch romantischer Partner.
5. **Dossier als Figurenreferenz:** Die Seite gibt beide Dossiers als Figurenkanon wieder (Etikett „Figurenkanon“, Quellen Q1 und Q2), ihre offenen Punkte stehen unter „Offene Fragen“.

Was ihr Wesen fürs Erzählen hergibt: Sie denkt in Möglichkeiten, Ergebnissen und Beziehungen. Verzögerungen machen sie ungeduldig, Enttäuschungen auch wütend, und mit Abstand sieht sie manches anders. Sie genießt gutes Essen, Theater, Feste und gesellige Abende. Fehler korrigiert sie ohne große Worte und bespricht sie gegebenenfalls mit Felix. Fachliche Kritik nimmt sie unter vier Augen an.

## Die Welt

`lore/welt-antonia-corvina.md` ist verbindlicher Kanon des Spielers. Julia Augusta regiert das Reich; in diesem Lauf ist also von der Kaiserin die Rede. Die Praetoren heißen Dorian Manlius Scaevola, Athr Iorgwyn und Alba Concordia; ihre Beziehungen zu Antonia werden nicht vorweggenommen, und was sie tun, kommt aus den Messungen.

Latium ist der Ausgangspunkt. Was der Entwurf zu Albion und Aegyptus als „Bedeutung für unsere Chronik“ nennt, sind erzählerische Perspektiven und keine Ereignisse. Eine Provinz kommt erst vor, wenn die Partie dort ist. Namen von Städten, ihre Entwicklung, Handelsbeziehungen und Konflikte entstehen im Spiel.

## Erscheinungsbild

Römisch wie der erste Lauf (`assets/roemisch.css`), mit Antonias Farben aus dem Dossier über `data-farbe="dunkelblau"` an `<html>`: Elfenbein als Papier, Dunkelblau für Kopf, Fuß, Links und Figurenkanon, Bronze für Linien und Ornamente, Bordeaux als dezenter Akzent (Initialen des Tagebuchs, Einschnitt im Kapitelkopf). Auf der Karte tragen ihre Inseln und Wohnhäuser Dunkelblau; ein Praetor, dessen Stammfarbe zu nah daran liegt, bekommt eine Ersatzfarbe.

## Anno-Monitor

Weltkennung `anno117-1794145443` aus dem ersten Autosave, Partie-Ordner „Antonia Corvina“. Das Hochlade-Skript findet die Partie über ihren Ordner und trägt `world_id` beim ersten Lauf in `data/monitor-sources.json` und `meta.json` ein. Hochladen nur mit Freigabe des Spielers: `py -3 scripts/publish-monitor.py --save zweiter-lauf`.
