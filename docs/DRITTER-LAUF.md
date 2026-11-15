# Aelwen · Dritter Lauf

Dritte Partie der AnnoChronik, begonnen am 15.11.2026 mit Update 3.0. Erzählt wird sie im Tagebuch der Protagonistin Aelwen. Die Entscheidungen des Briefings stehen in `BRIEFING.md`, Abschnitt „Dritter Lauf“. Wie weit erzählt ist: `werkstatt/dritter-lauf/STAND.md` und `werkstatt/AUFGABEN.md`.

Für Kapitel, Ereignisse und Entscheidungen, Tagebuch, Regeln aus dem Auftrag des Spielers und den Datenweg gilt `docs/ERSTER-LAUF.md` sinngemäß, dazu `docs/SCHREIBSTIL.md`. Hier steht, was im dritten Lauf anders ist. Die Partien bleiben getrennt: Figuren, Orte und Ereignisse der früheren Läufe kommen hier nicht vor. Praetoren mit Namen, die es dort auch gab, sind in dieser Partie neue Figuren.

## Wo was liegt

| Datei | Inhalt |
|---|---|
| `saves/dritter-lauf/chronik.html` | Die Chronik: Titelblatt, die Protagonistin (Figurenkanon), die Welt, Steckbrief der Partie, Register, Tagebuch (Kapitel), Inseln und Provinzen, offene Fragen, Quellen, Korrekturen. Handgeschrieben. |
| `lore/aelwen.md`, `lore/welt-aelwen.md` | Charakterdossier und Welt des Spielers, verbindlicher Kanon. Ändert nur der Spieler oder eine Sitzung auf seinen Wunsch. |
| `saves/dritter-lauf/data/` | `meta.json`, `manifest.json`, `events.json` (Register, append-only), `karte.json`, später `monitor/` (Messdaten, von `scripts/publish-monitor.py`). |
| `saves/dritter-lauf/karte.html`, `images/karte/` | Karte, je Kapitel ein Stand, von `karte.py` im Anno-Monitor (siehe `docs/KARTE.md`). |

## Aelwen und ihr Kanon

1. **Kanon von Möglichkeiten trennen.** Festgelegt ist, was das Dossier festlegt. Offen bleiben Familienname, Titel, Herrschaftsgebiet und Herrschaftssymbol, ihre Rolle beim Tod ihres Mannes und die Namen ihres Mannes, ihrer Eltern, der rivalisierenden Familie und ihrer Gefolgsleute.
2. **Der Tod ihres Mannes bleibt ungeklärt.** „Undurchschaubar“ heißt fürs Tagebuch: Aelwen schreibt auf, was sie aufschreiben will. Das Tagebuch klärt die Frage nicht und legt keine Antwort nahe.
3. **Absichten sind Pläne.** Die Ausgangslage im Dossier (kein Schiff, keltischer Weg, formelle Loyalität, Verdrängung der Statthalter, spätere Expansion) beschreibt, was sie vorhat. Erzählt wird, was davon im Spiel geschieht.
4. **Persönlichkeitsprofil:** Die Balken des Dossiers sind ein erzählerisches Profil, keine Spielwerte. Maßlosigkeit und Skrupellosigkeit zeigen sich in der Chronik, wenn das Spiel einen Anlass liefert.
5. **Religion:** skeptisch und zweckorientiert. Wählt sie im Spiel eine Gottheit, darf das Tagebuch den Nutzen nennen, den sie sich davon verspricht.
6. **Dossier als Figurenreferenz:** Die Seite gibt das Dossier als Figurenkanon wieder (Quelle Q1), seine offenen Punkte stehen unter „Offene Fragen“. Der Vergleich mit den Figuren früherer Läufe steht nur in `lore/aelwen.md`.

## Die Welt

`lore/welt-aelwen.md` ist verbindlicher Kanon. Gnaeus Firmius Calidus regiert das Reich; in diesem Lauf ist also vom Kaiser die Rede. Die Praetoren heißen wie im Spiel: Concordia, Tarragon und Licia Ma. Was das Spiel über Kaiser und Praetoren schreibt, erscheint nur in eigenen Worten. Was die Praetoren tun, kommt aus den Messungen; ihre Beziehungen zu Aelwen werden nicht vorweggenommen.

Albion ist die Startprovinz; die Startinsel steht fest, wenn der Spieler die Karte behält. Eine andere Provinz kommt erst vor, wenn die Partie dort ist.

## Erscheinungsbild

Keltisch auf der Grundlage von `assets/roemisch.css`, gewählt vom Spieler („Ja, keltisch“): `data-farbe="waldgruen"` an `<html>` (Waldgrün für Kopf, Fuß, Links und Figurenkanon, Gold für Linien, Ornamente und Initialen, dunkel ein „Nachtwald“) und `data-stil="keltisch"` (Knotenband statt Mäander, Knotenring statt Lorbeer, beide aus `scripts/ornamente.py`). Ein festes Zeichen kommt erst dazu, wenn Aelwens Herrschaftssymbol feststeht. Auf der Karte tragen ihre Inseln und Wohnhäuser Waldgrün; `karte.py` nimmt dafür ein etwas bläulicheres Grün, damit es sich vom Wald abhebt.

## Bilder

Spielgrafik (Porträts, Wappen aus der Praetorenwahl) und Bildschirmfotos mit dem Kontonamen kommen nicht auf die Seite. Die drei Bilder aus dem Dossier bleiben draußen, bis der Spieler entscheidet.

## Anno-Monitor

Die Partie beginnt auf einer Startinsel, deshalb startet der Spieler neu, bis ihm die Karte gefällt. Jeder Versuch ist im Monitor eine eigene Welt (der Monitor folgt dem neuesten Spielstand), und bei gleichem Namen kann das Spiel den Partie-Ordner `Aelwen_1`, `Aelwen_2` … nennen. Zur Chronik gehört nur die Welt der Karte, die der Spieler behält: Ihre Weltkennung und ihren Partie-Ordner erst nach seiner Bestätigung in `data/monitor-sources.json` und `meta.json` eintragen; bis dahin bleibt `world_id` leer. Frühere Versuche werden nicht erzählt. Hochladen nur mit Freigabe des Spielers: `py -3 scripts/publish-monitor.py --save dritter-lauf`.
