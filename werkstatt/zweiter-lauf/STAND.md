# Antonia Corvina · Zweiter Lauf · Stand

Stand 8.11.2026 (Claude). Kapitel I bis III geschrieben; nächste freie Quellennummer: **Q9** (Q1 und Q2 die Figurendossiers, Q3 der Weltentwurf, Q4 der Monitor, Q5 das Spielprotokoll, Q6 Angabe des Spielers und Bildschirmfoto, Q7 Bildschirmfotos bei 36:24 und 42:51 bis 43:34 min, Q8 Angabe des Spielers zur zweiten Insel und Bildschirmfoto bei 111:08 min). Nächste freie Registernummer: `zweiter-lauf-0053`.

## Figuren und Welt

- **Antonia Corvina:** `lore/antonia-corvina.md`, verbindlicher Kanon. Kaiserlich beauftragte Verwalterin und Siedlungsgründerin, 36 Jahre, ehrgeizig, pragmatisch, ungeduldig, gesellig. Das Amt ist hier festgelegt, als bewusst alternative historische Setzung.
- **Marcus Antonius Felix:** `lore/marcus-antonius-felix.md`, Freigelassener und persönlicher Sekretär. Realist, loyal, ohne verborgene Motive; weder enge persönliche Freundesfigur noch romantischer Partner.
- **Welt:** `lore/welt-antonia-corvina.md`. Kaiserin Julia Augusta, Latium als Ausgangspunkt, Albion und Aegyptus als mögliche Schauplätze. Die Abschnitte zur Bedeutung für die Chronik sind Perspektiven, keine Ereignisse.
- Offen und nur vom Spieler oder aus der Partie zu klären: siehe „Offene Fragen“ in der Chronik.

## Partie

- Partie-Ordner „Antonia Corvina“, Weltkennung `anno117-1794145443`, Seed 565, angelegt am 8.11.2026 um 14:08, Spielstand-Version 80. Erster Autosave vom Monitor gelesen um 14:44 (0:00 min).
- Aus dem ersten Autosave: Kaiserin Julia Augusta (`SetupStartEmperor` 31722), Praetoren Dorian (31099), Athr Iorgwyn (31102), Concordia (31104), Startprovinz Latium. Die vollen Namen Dorian Manlius Scaevola und Alba Concordia stammen aus dem Weltentwurf.
- Start mit 15.000 Denaren.
- Noch offen: Schwierigkeit und Erweiterungen, dafür das Bildschirmfoto der Spieleinstellungen abwarten. `world_id` trägt `publish-monitor.py` beim ersten Lauf ein.

## Daten

- Karte: `saves/zweiter-lauf/karte.html`, noch ohne Stand. Nach jedem Kapitel im Anno-Monitor `py -3 karte.py --save zweiter-lauf` laufen lassen (siehe `docs/KARTE.md`).
- Der Monitor sichert seit dem 8.11.2026 jeden gelesenen Spielstand, aber erst ab seinem nächsten Start; der laufende Monitor stammt von 13:58.

## Erzählt

**Kapitel I „Erythia“** (`#kapitel-1` in `saves/zweiter-lauf/chronik.html`): 0:00 bis 28:19 min Spielzeit, aufgenommen am 8.11.2026 von 14:44 bis 15:32. Einschnitt: die erste Siedlung, Erythia wird Kleiner Vicus (28:19 min; Spieler: „so die erste siedlung steht“, „Ja, Kapitel I“). Bericht, acht Tagebucheinträge, Randnotiz, Register `-0001` bis `-0019`, neu Q5 und Q6, eine neue offene Frage (Caecilias Vertrag). Kartenstand I aus dem Spielstand bei 27:05 min. Online seit `3c8d0b7`.

- Gültiger Verlauf: 0:00 bis 9:21 min (aufgenommen 14:44 bis 14:54, gespeichert als „Antonia Corvina 1“), dann ab 15:09:57 weiter von diesem Stand. Alles dazwischen gehört zu verworfenen Abschnitten und bleibt aus der Chronik.
- Die Monitorzeile „Begegnung mit einem Rivalen (Dorian)“ bei 19:01 min ist eine Wiederholung nach dem Laden. Die Entscheidung fiel bei 1:55 min (Fenster 14:49:07, im Spielstand schon bei 2:26 und 9:21 min). Das Fenster bei 19:01 min (27 s) gehört zum Libertus (Abgeleitet: Bretter 0 → 16, Kasse −646 zwischen 18:57 und 19:30 min).
- Status laut Live: Außenposten bis 27:19 min, Kleiner Vicus ab 28:19 min. Wohnhäuser nach Live (bei 27:05 min Spielstand 40, Live bei 27:19 min 64).
- Rivalen bei 27:05 min (Attribut Bevölkerung): Dorian 21, Athr Iorgwyn 103, Concordia 119. Aquae Serius ist bei 27:05 min noch unentdeckt und deshalb auf der Karte gepunktet.

**Kapitel II „Die Villa“** (`#kapitel-2`): 28:19 bis 66:00 min, aufgenommen am 8.11.2026 von 15:32 bis 16:12. Einschnitt: der Große Vicus (62:15 min); Stichtag ist der Spielstand bei 66:00 min, damit die Karte aktuell ist (Spieler: „Ja, Kapitel II“). Bericht, acht Tagebucheinträge, Randnotiz, Register `-0020` bis `-0037`, neu Q7, eine offene Frage (Concordias Lieferung). Kartenstand II aus dem Spielstand bei 66:00 min. Online seit `cb58395`.

- Zeitpunkte aus dem Spielstand (`LastDecayTime` der Wirkungen): Dorians „Schlechter Eindruck“ bei 1:55,2 min, „Kleiner Außenposten“ (Einwohnerstufe 2) bei 40:29,4 min, Concordias „Guter Anfang“ bei 43:19,6 min.
- Kasse: +1.248 um 37 min (Caecilias Fracht, Abgeleitet), −1.675 bei 52:13 min (Villa, Bretter 24 → 0), −1.544 bei 61:15 und −1.258 bei 63:16 min (Bauten, im Kapitel unerklärt).
- Bilanz: bei 53:13 min von +61 auf +198 (Spezialisten, Abgeleitet; die Villa war laut Protokoll um 15:58 und 15:59 geöffnet). Posten „Bereichseffekte und Spezialisten“ von 52 (28:19 min) auf 479 (66:00 min). „Villa des Praetors“ im Live-Mod ist die Kategorie Kulturbauten.
- Betriebe am Stichtag nach dem Spielstand (44); die Live-Messung kurz davor zählt weniger, weil sie Baustellen auslässt.
- Das erste Heiligtum und Concordias Geschenk liegen nach 66:00 min (im Spielstand bei 66:00 min noch ohne, bei 75 min erledigt). Die Plebejer haben bei 66:00 min Heiligtum 0 %, Merkur-Lugus ist aber schon Schutzgottheit.

**Kapitel III „Mithraeum“** (`#kapitel-3`): 66:00 bis 150:33 min, aufgenommen am 8.11.2026 von 16:12 bis 17:46. Einschnitt: Mithraeum, die zweite Insel (150:19 min laut Spielprotokoll; Spieler: „und die zweite insel ist am start“, „Ja, Kapitel III“). Bericht, neun Tagebucheinträge, Randnotiz, Register `-0038` bis `-0052`, neu Q8, offene Frage „Der verrückte Koch“ statt Concordias Lieferung. Kartenstand III aus dem Spielstand bei 150:26 min. Online seit `d44cb0e`.

- Diplomatie laut Spielprotokoll: Concordia bietet bei 69:42 min ein kleines Geschenk an (`OfferGift_Small`), einen Geldbetrag zeigt die Kasse dabei nicht. Dorian trägt direkt nach der Inselnahme einen Nichtangriffspakt (Aktion 31737) und einen Handelsvertrag (31739) an, um 17:46:31; gelöst um 17:46:42 und 17:46:47. Der Spielstand bei 150:26 min führt den Handelsvertrag, der bei 155:27 min beide. Athr Iorgwyn und die Piraten sind weiter unentdeckt.
- Siedlungsrechte: Kasse 47.964 (149:27) → 178 (150:33); das Fenster war schon um 120, 143 und 148 min offen. Grundsteuer seitdem 300.
- Feuer: 96:42 bis 100:31 min, Vigiles, 7 Liberti-Wohnhäuser und 2 weitere Gebäude. „Brandstifter“ bei Dorian und Athr Iorgwyn (Diplomatie) hat damit nichts zu tun, das ist die niedrige Brandsicherheit.
- Kasse springt mehrmals weit über die Bilanz (+2.683 bei 67:17, +1.588 bei 76:47, +1.424 bei 100:38, +2.253 bei 103:38, +3.441 bei 114:34, +3.846 bei 146:27 min). Wahrscheinlich Lieferverträge, einzeln nicht zugeordnet.
- Im Monitor heißt die Fracht je Partei „Verlorene Fracht von …“; Kisten waren bei Dorian bei 94:51 und 99:55 min an Bord.

**Stoff für Kapitel IV** (ab 150:33 min, nur Beobachtetes): Mithraeum wächst (drei Holzfäller, drei Sägewerke, Sardinenhütte, Haferhof, Breistand bis 157:25 min), die Kasse fällt kurz ins Minus, „Leere Kassen“ bis 155:27 min erledigt; Athr Iorgwyn nimmt Insel 9218 (151:10 min); „Der verrückte Koch“ offen; Lieferung für Dorian offen.

## Tagebuch

- Vorspiel „Eine Insel, die Dorian uns nahm“ am 8.11.2026 ergänzt (Spielerangabe und Bildbelege, Rekonstruktion klar markiert). Nach Spielerbestätigung: Dorians Insel heißt Musculeum, Antonia nahm Kurs auf Erythia.
- **Formen Kapitel I:** Gespräch (Dorian), Notiz am Rand (Wer schon da ist), Eintrag (Der Strand), Rechnung (Felix rechnet), Gespräch (Eine Audienz), Eintrag (In der Taberna), Brief an die Kaiserin, Entwurf einer Inschrift (Für den Platz).
- **Antonias Stimme:** Vergangenheitsform, urban, sie denkt in Menschen und Wirkungen. Ungeduld zeigt sich an Handlungen (Platz abgesteckt, Baumeister vor seinen Leuten angefahren, später Wein geschickt). Sie rechnet nicht selbst; die Zahlen bringt Felix. Anrede durch Felix: „Domina“.
- **Formen Kapitel II:** Notiz am Rand (Plus null), Gespräch am Hafen (Eine Kiste für Caecilia), Eintrag (Vier Häuser), Gespräch (Alba Concordia), Opfer (Merkur-Lugus), Liste (Wer in der Villa wohnt), Gespräch (Das erste Brot), Eintrag (Großer Vicus).
- **Formen Kapitel III:** eingelegter Brief von Concordia (Eine Gabe aus Aquae Serius), Notiz am Rand (Ein Koch), Gespräch (Brutus oder Gaius), Gespräch am Hafen (Dorians Kisten), Eintrag (Sieben Häuser), Eintrag (Lugnasad), Gespräch (Merypath), Notiz am Rand (Tausendneun), Brief an die Kaiserin.
- **Wiederkehrende Figuren** (Namen erst mit dem Spieler, außer Namen aus dem Spiel):
  - Felix: legt die Kasse vor, führt die Liste der Kontakte (Spalte „was wir von ihnen wollen und sie von uns“), wartet mit der Laterne, siegelt;
  - der Baumeister: fragt erst, wenn die Träger außer Hörweite sind; bekam nach dem Anfahren einen Krug Wein;
  - der Libertus mit dem Karren (400 Denare für 20 Bretter);
  - der Wirt der Taberna; ein Mann vom Haferhof;
  - Dorian Manlius Scaevola: rief von der Bordwand herüber; Antonia nickte einmal;
  - der Mann vom Haferhof wohnt seit Kapitel II in einem der vier ersten Plebejerhäuser; der Wirt brachte das erste Brot selbst und stiftete Salz fürs Opfer; der Baumeister zimmerte den Altar aus Brettern und wollte sie zurück;
  - der Steuermann (Caecilias Kiste, hob die Schultern); Alba Concordia und ihr Priester, der zum Himmel sah;
  - in der Villa: Troucotouto (Subiudex, ließ beide Seiten eines Zaunstreits zahlen, schlichtet Streit, bevor er anfängt), Menander von Nikomedes (Haruspex, liest immer Gutes), Actorius Maximinus (Nummularius, sitzt abends mit Felix über den Büchern), Brutus Julius Lupus (fragte, woran es am meisten fehlt; sein Zwilling Gaius reiste mit Reisegeld ab);
  - Merypath, Gromaticus-Vermesser auf dem Flaggschiff (fand Mithraeum); der Hauptmann der Vigiles (Feuer); der Libertus mit dem Karren schwört auf einen Koch am Hafen.
- **Offene Fäden:** wer in Rom Dorian etwas schuldet (Felix sieht die Briefe durch); der Platz für die Verwaltung ist abgesteckt, die Straße vom Hafen dorthin gewünscht, das Forum nur erzählt; der Brief an die Kaiserin ohne Kasse; der Entwurf der Inschrift liegt bei den Briefen; die Villa steht auf dem abgesteckten Platz; Antonia will die Ziegel im nächsten Brief an die Kaiserin erwähnen; Caecilia hat eine eigene Zeile in Felix’ Liste; neben Concordias Namen steht ein Fragezeichen (was sie für ihre Gabe will); der Koch steht auf Felix’ Liste; Antonia hat Dorians Kisten „mit einem Gruß“ zurückbringen lassen und hat jetzt Verträge mit ihm; die Kaiserin kennt die Kasse weiterhin nicht.
