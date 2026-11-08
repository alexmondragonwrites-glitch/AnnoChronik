# Werkstatt-Log

Übergaben und Reviews, neueste oben. Nur ergänzen.

## 2026-11-08 – Zweiter Lauf: Antonia Corvina (Claude)

- Spieler: „Ich werd ein neues Anno Spiel beginnen gleich“; eigene Chronik mit neuer Figur und Tagebuch, Titel „Name · Zweiter Lauf“, Caesia läuft weiter. Freigabe „Ja, so bauen“; danach die Dossiers von Antonia Corvina und ihrem Sekretär Marcus Antonius Felix. Abgelegt in `lore/antonia-corvina.md` und `lore/marcus-antonius-felix.md`, Wortlaut des Spielers, nur als Markdown gegliedert.
- Dazu der Weltentwurf des Spielers (Kaiserin Julia Augusta, die drei Provinzen, drei Praetoren): `lore/welt-antonia-corvina.md`, ohne die Quellenvermerke und Bildreste aus dem Einfügen.
- Neu: `saves/zweiter-lauf/` (Chronik mit Figuren- und Weltkanon, Kartenseite, Daten), `docs/ZWEITER-LAUF.md`, `werkstatt/zweiter-lauf/STAND.md`, Eintrag im Portal und in `AGENTS.md`. Der erste Autosave (14:44) bestätigt Partie-Ordner „Antonia Corvina“, Kaiserin Julia Augusta, die Praetoren Dorian, Athr Iorgwyn, Concordia und Latium als Startprovinz; Weltkennung `anno117-1794145443`.
- Farben aus dem Dossier: Dunkelblau, Elfenbein, Bronze, Bordeaux als dezenter Akzent. `data-farbe="dunkelblau"` an `<html>` setzt sie in `assets/roemisch.css`, hell und dunkel.
- Werkzeuge:
  - `karte.py`: Name und Farbe je Chronik aus `meta.json`, Zeichen der Karte aus den Daten, Praetoren weichen der Farbe der Figur aus (Ersatzfarbe), lange Kartuschenzeilen bleiben im Rahmen.
  - Bereichsnummern je Provinz: Latium endet auf 64·n + 1, Albion + 2, Aegyptus + 4. Deshalb fehlten in Albion Namen und Besitz. Geprüft an allen drei Provinzen: Jede Fläche im Gitter hat ihren Bereich und umgekehrt.
  - `new-save.mjs`: neue Optionen `--untertitel`, `--figur`, `--farbe`; legt Kartenseite und `karte.json` mit an.
- Erster Lauf: Karten von Kapitel VII und VIII neu gezeichnet, Albion jetzt mit Namen und Besitz. Die Zahl „19 von 19“ auf der Karte zählt Inseln ohne Deko-Inseln, der Monitor (26) zählt sie mit.
- Geprüft: `validate-data.mjs`, `test-monitor-daten.py`, `test_karte.py` (15 Tests); Browser: Chronik, Kartenseite und Portal, 375 px ohne waagrechtes Scrollen, dunkel, keine Konsolenfehler.
- Hochgeladen auf Freigabe („Ja, hochladen“): `ff7c671`.

## 2026-11-07 – Kapitel VII „Nach Albion“ und VIII „Bögen und Ruder“ (Claude, Nebensitzung)

- Spieler: „nächsten story denke ich agueduct und die ersten legionäre die ausgebildet werden plus tireme.“ Vorgeschlagen waren zwei Kapitel (VII bis Runlet, VIII bis zu den ersten Legionären) oder eines; Spieler: „Zwei Kapitel“.
- Quellen: der Monitor mit der Nachlese (Q3, Q10 bis 221:51 min), die Spielstände und das Spielprotokoll (Q6). Die Entscheidungszeiten in Kapitel VII stammen aus der Notiz der Nachlese.
- Kapitel VII (189:06 bis 231:01 min):
  - drittes Feuer, Öl, Beton und Equites;
  - Adlerstandarten (40.000 Denare); Tarragon siedelt mit Erlaubnis in Albion (Antica), Zara Nitu nimmt Calculus;
  - Athr Iorgwyn gegrüßt, Wein und Theater, Aegyptus;
  - Runlet bei 230:29 min.
  - Register `-0076` bis `-0088`.
- Kapitel VIII (231:01 bis 271:27 min):
  - Runlet wächst;
  - Voada von den Scáthach an Roms Herrschaft erinnert; Gnade für einen Wanderer;
  - Trireme (Werft 243:42 bis 255:28, Angriffe), Legionäre (Forschung 264:19, Ausheben, Militärgebäude ab 270:09) und Aquädukt (Zisterne ab 271:09, Infofenster), alle drei als Abgeleitet;
  - Brief „Wasser“ mit der Aqua Traiana;
  - Register `-0089` bis `-0100`.
- Karten mit `karte.py`: VII nach dem Spielstand bei 223:00 min, weil das Spiel die Stände bei 228:13 und 233:43 min überschrieben hat; VIII nach dem Spielstand bei 271:27 min. Die Spielstände sind gesichert in `Anno-Monitor/_sicherung/2026-11-07_kapitel/`. Auf den Albion-Karten fehlen Namen und Besitz (Werkzeug); dafür ist eine Sitzung vorgeschlagen.
- Geprüft:
  - `validate-data.mjs`, `test-monitor-daten.py`, HTML-Aufbau, Q-Anker;
  - Wortprüfung ohne Fund;
  - Browser: 8 Kapitel, 100 Registerzeilen, Karten VII und VIII, 375 px, dunkel, keine Konsolenfehler;
  - Einträge am Stück gelesen.
- Hochgeladen auf Freigabe („Ja, hochladen“): `5a63c5a`.

## 2026-11-07 – Messdaten nach der Nachlese (Claude, Nebensitzung)

- Die Sitzung monitor-live-zeilen-aus hat die Live-Zeilen vom 6.11., 15:18 bis 16:23, aus dem Spielprotokoll in den Monitor übernommen: 60 Live-Messungen von 165:38 bis 221:51 min und Autosave 33 (181:04 min). Die Zuordnung der drei Entscheidungen bei 220:40 min bleibt „seit 201:09“ (Variante A): Die Reihenfolge der Fenster hätte zwei Zeiten falsch gesetzt; die Belege dafür stehen für Kapitel VII in der Notiz der Nachlese.
- Messdaten neu erzeugt (`publish-monitor.py --no-push`), mit der Sitzung vom 7.11. ab 6:15: 341 Messungen bis 271:27 min, ohne Neuladen.
- Veröffentlichte Zeilen, die sich ändern:
  - berichtigt: Krankheit auf Beneventum (177:23, eingedämmt bis 182:44 min, Medici) statt „die Art steht nicht im Zeitplan“; Feuer auf Olivaria bei 207:15 min statt des Zeitraums;
  - Sammelzeilen der Spielstände entfallen zugunsten minutengenauer Live-Zeilen, darunter „Equites erstmals beobachtet (207 Bewohner)“ bei 222:13 min.
- `chronik.html`: Eintrag unter „Korrekturen“ (7. November 2026); bei Q10 der Satz, dass die Live-Zeilen jetzt auch in den Messdaten stehen.
- Geprüft: `validate-data.mjs`, `test-monitor-daten.py`, keine Pfade oder Dateinamen in den Messdaten, Seite im Browser (5 Korrekturen, Messdaten 294 bzw. jetzt 341, keine Konsolenfehler).
- Hochgeladen auf Freigabe („Ja, hochladen“): `441e821` (Messdaten), `ac9f841` (Korrektur).
- Spieler danach: „nächsten story denke ich agueduct und die ersten legionäre die ausgebildet werden plus tireme.“ Kapitel VII ist noch offen.

## 2026-11-06 – Kapitel VI „Öl und Krüge“ und Berichtigung von Kapitel V (Claude, Nebensitzung)

- Spieler: „lleider vergessen den monitor laufen zu lassen hoffe trotzdem was brauchbares dabei“. Gespielt hatte er von 15:18 bis 16:24, bei 165:38 bis 223:00 min, ohne Neuladen; der Monitor lief erst ab 16:23.
- Nachgelesen, nur aus Kopien:
  - Der Live-Mod schreibt ins Spielprotokoll. Mit dem Leser des Monitors (`quelle_lua._json_aus_zeile`, `aus_lua`) kamen 61 Messungen von 165:38 bis 222:13 min heraus (neue Quelle Q10).
  - Dazu die Spielstände bei 165:38, 181:04, 201:09, 220:40, 221:51 und 223:00 min (neue Quelle Q11), gelesen mit `spielstand.lies` und den Ereignisfunktionen in `messung.py`.
- Vorgeschlagen: die ersten Equites (189:06 min), daneben bis zum Speichern (223:00 min). Spieler: „Erste Equites“.
- Kapitel VI (146:09 bis 189:06 min): Bericht, sieben Tagebucheinträge mit einem Brief an die Mutter (Erinnerung an den Scherbenhügel am Tiber), Randnotiz, Register `erster-lauf-0062` bis `-0075`, eine offene Frage. Kartenstand VI mit `karte.py` aus dem Spielstand bei 181:04 min.
- Befunde:
  - Harz, Töpfer, Olivenzüchter und Pressen bringen Amphoren und Öl.
  - Ein Angriff um 152:09 min, danach ein Kriegsschiff weniger, die Werft baut Ersatz (Abgeleitet).
  - Litugenus trägt dieselbe Gegenstandskennung wie zuvor der unterschriebene Vertrag; daher vermutlich der Lohn für das Geleit.
  - Krankheit bei 177:23 min (Medici).
  - Die Villa auf Olivaria (Abgeleitet).
- Kapitel V berichtigt, mit den Werten der Monitor-Sitzung:
  - Zeitachse „133:58 bis 135:11 min“, im Bericht Auslösezeit, zweite Custodia und Lagerhaus;
  - die Ableitung zu den Unruhen aus der Randnotiz gestrichen, ebenso die offene Frage nach ihrem Beginn;
  - Eintrag unter „Korrekturen“, Register `-0061`.
  - Im Korrektureintrag der Monitor-Sitzung ist der letzte Satz auf „Kapitel V ist im nächsten Eintrag berichtigt“ geändert.
- Geprüft:
  - `validate-data.mjs`, `test-monitor-daten.py`, HTML-Aufbau, Q-Anker und Wortprüfung;
  - Browser: 6 Kapitel, 75 Registerzeilen, Karte mit Stand VI, 375 px ohne waagrechtes Scrollen, dunkel, keine Konsolenfehler;
  - Einträge am Stück gelesen.
- Hochgeladen auf Freigabe („Ja, hochladen“):
  - `637aee5`: Messdaten, 233 Messungen bis 233:43 min, mit der berichtigten Zeile der Unruhen;
  - `0eaaca4`: Kapitel VI, Berichtigung von Kapitel V und Kartenstand VI, mit den vorbereiteten Änderungen der Monitor-Sitzung.
- Offen:
  - Die Sitzung monitor-live-zeilen-aus baut die Nachlese der Live-Zeilen von 15:18 bis 16:23 in den Monitor. Danach die Messdaten neu erzeugen und mit Freigabe hochladen; dann im Quellensatz von Kapitel VI vermerken, dass die Werte ab 165:38 min auch in den Messdaten stehen.
  - Seit 16:31 hat der Spieler mit Monitor weitergespielt: Runlet in Albion bei 230:29 min (siehe `STAND.md`).

## 2026-11-06 – Ausbruchszeit der Unruhen (Claude, Monitor-Sitzung)

- Anlass: Die Chronikzeile des Monitors vom Autosave bei 135:16 min nannte als Ausbruch der Unruhen 120:12 min (Befund aus Kapitel V).
- Befund im Spielstand:
  - Die Zahl der Zwischenfälle ist bis 130:07 min 1, bei 135:16 min 3.
  - `IncidentTriggerTime` im Zeitplan ist nur ein Rechenwert. Er wird alle 3 s neu bestimmt. Rückt er in die Vergangenheit, löst der Zeitplan sofort aus, der Wert bleibt.
  - Belegt ist die Auslösezeit je Zwischenfall-Asset und Teilnehmer (`MetaIncidentManager/IncidentsTriggerTimerMap`): zweites Feuer 133:57 min, Unruhen 133:58 min.
  - Das `fx_riot` um 10:48:46 ist das Infofenster eines betroffenen Betriebs.
- Anno-Monitor: Leser, Chronik und Test umgestellt; Chronikzeile berichtigt (Feld `korrigiert`, Sicherung daneben).
- Hier lokal, nicht hochgeladen:
  - `data/monitor/tag-2026-11-06.json` neu erzeugt; nur Text und `ausbruch_ms` der Unruhen-Zeile ändern sich;
  - Eintrag unter „Korrekturen“ in `chronik.html`;
  - Befund in `STAND.md` (Kapitel V).
  - Kapitel V selbst blieb unverändert: Bericht und offene Frage nennen die alte Zeile; ob sie ergänzt werden, entscheidet der Spieler.
- Geprüft: `validate-data.mjs`, `test-monitor-daten.py`, HTML-Aufbau; im Anno-Monitor 44 Tests grün.
- Die Kartenzeile der Karten-Sitzung in `chronik.html` ist seit `8e3795a` online; offen ist dort nur noch die Korrektur.

## 2026-11-06 – Karte von Latium (Claude)

- Spieler: „gibs auch wieder die möglichkeit ener karte? wie brauchen es nicht so auffwendig wie in tf3 aber hübsch sollte sie trtzdem sein eher so wie iene landkkarte“. Probekarte vorgelegt, Vorschlag freigegeben: „Ja, so bauen“ (`BRIEFING.md`, Abschnitt Karte).
- Neu:
  - `saves/erster-lauf/karte.html` mit Kapitelwahl (`assets/karte.js`), Zeichen und „Wie die Karte entsteht“;
  - `data/karte.json`, Bilder in `images/karte/` (je Kapitel etwa 0,6 bis 0,7 MB in voller Größe und 0,15 MB für die Seite);
  - Doku `docs/KARTE.md`, Zeile und Kapitelschritt in `docs/ERSTER-LAUF.md`, Link „Karte“ im Kopf von `chronik.html`.
  - Das Werkzeug `karte.py` liegt im Anno-Monitor, nicht im Repo.
- Kartenstände I–V nach den Spielständen bei 16:32, 43:47, 74:59, 125:17 und 140:26 min. Für Kapitel IV der Session Backup genau am Einschnitt, gesichert aus der Nebensitzung von Kapitel V.
- Befunde:
  - Inselnamen ändern sich mit der Inselnahme: Agathea (140:26 min, ohne Besitzer) heißt ab 155:55 min Zibanitu (Zara Nitu). Die Karte von Kapitel V zeigt deshalb Agathea.
  - Olivaria steht als Umbenennung in `karte.json` (ab 126:05 min), weil der Spielstand weiter Lorica führt.
- `validate-data.mjs` prüft jetzt auch die Karte (Bilder vorhanden und höchstens 3 MB, Spielstand im Kapitel, Seite aktuell, keine Kontokennung in Bildern); die Action prüft `assets/karte.js`.
- Geprüft:
  - `validate-data.mjs` (auch mit einem fehlenden Bild als Gegenprobe) und `test-monitor-daten.py`;
  - im Anno-Monitor `test_karte.py`, 8 Tests;
  - Browser: Kapitelwahl, Link aus der Chronik, volle Größe, 375 px ohne waagrechtes Scrollen, dunkel, keine Konsolenfehler.
- Hochgeladen auf Freigabe („Ja, hochladen“): `8e3795a`.

## 2026-11-06 – Kapitel V „Olivaria“ (Claude, Nebensitzung)

- Inselname: Der Spieler wollte Lorica wegen Harz und Oliven umbenennen und wählte aus fünf Vorschlägen (Olivetum, Olivaria, Olea, Pinetum, Resina) „Olivaria denke ich“. Eingetragen in `werkstatt/erster-lauf/STAND.md`, hochgeladen auf Freigabe als `89f7593` (dabei die Uhrzeit im Kopf des Stands berichtigt). Im Spiel umbenannt zu Beginn der nächsten Sitzung, live ab 126:05 min.
- Spieler: „so ich denke es ist wieder was pasiert.“ (gespielt 10:36 bis 11:18 und 11:25 bis 11:28, 125:17 bis 165:38 min, ohne Neuladen). Vorgeschlagen: die ersten Plebejer auf Olivaria (146:09 min), daneben Kleiner Vicus auf Olivaria (138:08 min) oder bis zum Speichern (163:52 min). Spieler: „Erste Plebejer“.
- Befunde:
  - Unruhen: Die Monitor-Chronik (Autosave bei 135:16 min) nennt als Ausbruch 120:12 min. Der Session Backup bei 125:17 min zählt aber nur einen Zwischenfall, und das Spielprotokoll zeigt die Unruhen-Meldung um 10:48:46, zwischen 134:07 und 135:07 min. Im Bericht als Widerspruch benannt, dazu eine offene Frage; der Monitor-Sitzung gemeldet.
  - Zweites Feuer von 133:57 bis 138:52 min (Vigiles), ein Gebäude, dessen Kennung der Katalog nicht kennt.
  - Tarragons Lieferung verschwindet zwischen 130:07 und 135:16 min aus dem Auftragsbuch; zwischen 131:06 und 132:07 min steigt die Kasse um 3.432 Denare. Steht als vermutlich bezahlt (Abgeleitet).
  - Die Hafengebäude kosten von 138:08 bis 143:08 min 100 statt 64, danach stehen zwei Kriegsschiffe in den Ausgaben, wie vor dem ersten (Abgeleitet: die Werft baute).
  - Geleitbefehl zwischen 144:08 und 145:09 min (Spielprotokoll), Vertrag „Valeria beschützen“ ab 145:36 min.
  - Zweite Inseln der Praetoren mit Namen aus dem Spielstand: Caer Morgan (Athr Iorgwyn, Albion), Zibanitu (Zara Nitu, Latium).
- `chronik.html`: Kapitel V mit Bericht (Kennzahlen, Zeitachse, Quellen Q3, Q6 und neu Q9), sieben Tagebucheinträgen und Randnotiz; Verweis im Inhalt; Inselliste mit Olivaria („bis 125:17 min Lorica“), Caer Morgan und Zibanitu; zwei offene Fragen. Register `erster-lauf-0049` bis `-0060`.
- Schreibweise nach `SCHREIBSTIL.md`, ohne Brief und ohne Erinnerung an Rom; Einträge am Stück gelesen.
- Geprüft:
  - `validate-data.mjs`, `test-monitor-daten.py` und der HTML-Aufbau;
  - Wortprüfung: zwei sachliche Verneinungen in Bericht und Randnotiz, im Tagebuch keine;
  - Browser: 5 Kapitel, 60 Registerzeilen, 375 px ohne waagrechtes Scrollen, dunkel, keine Konsolenfehler.
- Hochgeladen auf Freigabe („Ja, hochladen“): `a404828` (Messdaten, 213 Messungen bis 165:38 min) und `6272304` (Kapitel V).

## 2026-11-06 – Kapitel IV „Lorica“ (Claude, Nebensitzung)

- Spieler: „so gespielt ersten neuen schiffe seife und die erste neue insel“ (gespielt 8:14 bis 8:54, 86:30 bis 125:17 min, ohne Neuladen; der Monitor lief seit 7:59 mit Zwischenfällen und Gegenständen). Vorgeschlagen und bestätigt: Kapitel IV endet mit Lorica, der ersten neuen Insel („Ja, bis Lorica“). Während des Schreibens: „vllt auch mal den vergleich zu rom zu dem was sie jetzt durchmachen muss? und die erste seife?“, umgesetzt als Brief „Die erste Seife“.
- Befunde:
  - Lorica ist Insel 9665 in Latium. Das Spielprotokoll zeigt um 8:53:57 die Inselnahme direkt nach dem Fenster der Siedlungsrechte (`OMSettlementRights`), danach Speichern und Spielende.
  - Die Kasse fällt von 48.321 (124:36 min) auf 152 (Spielstand 125:17 min), die Grundsteuer steigt auf 300. Die rund 48.000 Denare für die Siedlungsrechte stehen als Abgeleitet.
  - Koch („Courage und Konfit-enz“): Münzen geschenkt. Der Schritt nach „Die Sohle kosten“ fehlt im Spielstand, also urteilte der Libertus allein (Abgeleitet). Pallas oleum verschwindet mit dem Auftrag.
  - „Villa des Praetors“ ist im Live-Mod die Kategorie Kulturbauten; die Verdopplung bei 121:36 min fällt mit „Tutorial: Gästehaus“ zusammen.
- `chronik.html`: Kapitel IV mit Bericht (Kennzahlen, Zeitachse, Quellen Q3, Q6), sieben Tagebucheinträgen und Randnotiz; Lorica unter „Inseln und Provinzen“; offene Frage zu den Einheiten (98 → 49 bei 104:33 min); Verweis im Inhalt. Register `erster-lauf-0037` bis `-0048`.
- Schreibweise nach `SCHREIBSTIL.md`; der Vergleich mit Rom nur im Brief, über die Mutter nichts festgelegt („unser Garten“). Einträge am Stück gelesen.
- Geprüft:
  - `validate-data.mjs` und `test-monitor-daten.py`;
  - Wortprüfung im neuen Text ohne Fund;
  - Browser per Seitentext: 4 Kapitel, 48 Registerzeilen, 375 px ohne waagrechtes Scrollen, dunkel, keine Konsolenfehler. Bildschirmfotos schlugen fehl, das Fenster lag im Hintergrund.
- Hochgeladen auf Freigabe („Ja, hochladen“): `9f866e3` (Messdaten, 160 Messungen bis 125:17 min) und `996cbe5` (Kapitel IV).

## 2026-11-06 – Kapitel III „Eisen und Segel“ (Claude, Nebensitzung)

- Spieler am Morgen: „haben sich neue geschichten ergeben?“. Er hatte von 5:42 bis 6:05 weitergespielt (64:55 bis 86:29 min, ohne Neuladen). Vorgeschlagen war als Einschnitt die Kleine Gemeinde (75:22 min, Aufnahme 6.11. 5:54); Spieler: „ja und achte dann auf unseren neuen schreibregeln SCHREIBSTIL.md“ (`docs/SCHREIBSTIL.md`, `68b2181`).
- Auf Nachfrage entschieden: Beim Piraten Caeso Regulus Syracus denkt Caesia nicht an ihren Vater (Vermutung bleibt unberührt); das Feuer hat es gegeben. Die Monitor-Sitzung fand es danach im Spielstand; selbst nachgelesen in Autosave 14 bis 16: ausgebrochen bei 71:07 min, gelöscht bis 74:53 min von den Vigiles, sechs Liberti- und zwei Plebejer-Wohnhäuser betroffen, bisher der einzige Zwischenfall. Die zweite Stadtwache (73:34 min) entstand noch während des Feuers.
- `chronik.html`: Kapitel III mit Bericht (Kennzahlen, Zeitachse, Quellen Q3, Q6, neu Q8), acht Tagebucheinträgen und Randnotiz; Verweis im Inhalt; offene Frage zum Bevölkerungssprung (74:35 bis 74:59 min um 161 bei gleich vielen Häusern).
- Schreibweise nach `SCHREIBSTIL.md`: ruhige, verbundene Sätze, keine Schlusspointen, weniger Rechnungen und Zahlen als in I und II, eine beiläufige Erinnerung an Rom. Die Einträge am Stück gelesen; einen abgehackten Einzelsatz in „Eisen“ verbunden. Kapitel I und II enthalten noch Muster, die die Regel meint; sie bleiben bis zu einer Freigabe des Spielers (Tafel unter „Offen“).
- Register `erster-lauf-0025` bis `-0036`: Leder und Sandalen, „Der verrückte Koch“ (Auftraggeber der Libertus aus Kapitel I), Segel und Hafengebäude, erste abgeschlossene Forschung, mehr Plebejer als Liberti, Tarragons Kisten, Eisen und Waffen, der Pirat, das Feuer, Essenzialistin und Pallas oleum, Kleine Gemeinde; als Abgeleitet Bevölkerung fast verdoppelt und neun Waffen ausgegeben.
- Geprüft: `validate-data.mjs`, `test-monitor-daten.py`, Wortprüfung und Kontrastmuster ohne Fund im neuen Text, Browser bei 1280 und 375 px, hell und dunkel.
- Hochgeladen auf Freigabe („Ja, hochladen“): `818b436` (Zwischenfälle im Messdaten-Skript, Monitor-Sitzung; mit Zustimmung des Spielers mitgenommen), `4d6145c` (Messdaten, 113 Messungen bis 86:29 min, neue Tagesdatei 6.11.) und `6695e44` (Kapitel III).
- Für eine Prüfung durch Codex: Die Feuerdaten stehen erst nach dem nächsten Neustart des Monitors in den Messdaten; bis dahin belegt sie Q8 (nachgelesener Autosave). Status, Wohnhäuser, Geldposten, Attribute, Lager und Praetoren liegen nur in den vollständigen Messungen.

## 2026-11-05 – Kapitel II „Brot und Ziegel“ (Claude, Nebensitzung)

- Spieler: „ich denke wir haben genug für ein kapitel 2 🙂 oder?“. Vorgeschlagen war als Einschnitt der nächste Stadtstatus, der Große Vicus (47:25 min Spielzeit, Aufnahme 17:20), als Alternative das erste Heiligtum (38:35 min). Spieler: „Beim Großen Vicus“, danach „Ja, hochladen“.
- Quellen wie in Kapitel I: Monitor-Chronik, vollständige Messungen der Läufe ab 15:09, 16:29 und 17:09, Spielprotokolle. Neu ist Q7: Autosave 4 (21:44), Autosave 8 (36:24) und „Caesia Varilla 1“ (38:35), als Kopie mit `spielstand.lies` des Monitors gelesen, schreibend nichts am Monitor. Daraus stammen die Schutzgottheit (leer bei 36:24, Ceres 7,6 bei 38:35), die Forschung (leer bei 21:44, „Attraktive Märkte“ bei 36:24), das Auftragsbuch (Vertrag „Verlorene Fracht“ von Zara Nitu bei 36:24 und 38:35) und Kisten an Bord des Flaggschiffs.
- `chronik.html`:
  - Kapitel II mit Bericht (Kennzahlen, Zeitachse, Quellen Q3, Q6, Q7), neun Tagebucheinträgen und Randnotiz;
  - Q7 unter Quellen, eine offene Frage zum Ausgang von Zara Nitus Vertrag, Verweis im Inhalt.
- Register `erster-lauf-0013` bis `-0024`: Zara Nitu gegrüßt, Villa des Praetors, Brot, Stadtwache, erste Forschung, Vertrag „Verlorene Fracht“, Ceres und erstes Heiligtum, Garum, Beneventum wieder vor Umbra, Gaius Julius Lupus, Großer Vicus; als Abgeleitet, dass Liberti zu Plebejern wurden, während die Häuser bei 68 blieben.
- `roemisch.css` ergänzt: Trennlinie zwischen Kapiteln, Bauinschrift im Tagebuch (schmal mit engerem Abstand).
- Befund beim Schreiben: Bei der Bevölkerung lag Zara Nitu nur in den Spielständen bei 36:24 und 38:35 min vor Caesia, vorher und bei 43:47 min lag Beneventum vorn. Die Bilanz der ersten Live-Messung nach dem Laden um 17:09 (+656) ist ein Ladewert und steht in keinem Text.
- Geprüft:
  - `validate-data.mjs` und `test-monitor-daten.py`;
  - Wortprüfung im neuen Text ohne Fund (der einzige Treffer steht in der Korrektur der Monitor-Sitzung);
  - Browser bei 1280 und 375 px, hell und dunkel, ohne Konsolenfehler und ohne waagrechtes Scrollen.
- Hochgeladen auf Freigabe („Ja, hochladen“): `ef48cca` (Kapitel II, Register, CSS, `STAND.md`). Die Messdaten bis 1:04 h lagen schon online (`e3214ee`).
- Für eine Prüfung durch Codex:
  - Kurzwerte, Bedürfnis- und Betriebszeilen sowie Erkundung und die Zeilen ab 43:47 min stehen in `saves/erster-lauf/data/monitor/tag-2026-11-05.json`.
  - Status, Wohnhäuser, Geldposten, Attribute und Praetoren liegen nur in den vollständigen Messungen beim Spieler, die Angaben vor 43:47 min zu Ceres, Forschung und Auftragsbuch in Q7.

## 2026-11-05 – Spezialisten und Gegenstände aus dem Monitor (Claude)

- Spieler: „haben wir auch spezialisten und items drin?“, danach „Ja, einbauen“.
- Im Anno-Monitor:
  - Katalog Schema 5 mit 760 Items (Name, Art, Seltenheit, Preis) und 126 Gebäuden und Schiffen mit Plätzen für Items.
  - Der Spielstand-Leser verfolgt die eigenen Stücke mit Ort: Lager einer eigenen Insel, eingesetzt in einem Gebäude, an Bord eines eigenen Schiffs. Treibende Fracht zählt nicht.
  - Chronikzeilen „Neuer Spezialist: …“, Ortswechsel, „Abgegeben (verkauft, verbraucht oder übergeben): …“.
  - Belohnungen von Entscheidungen tragen jetzt Item-Namen. Gesprächsschritte („Sprich mit …“) einer Entscheidung, deren Wahl feststeht, bekommen keine eigene Zeile mehr.
  - Seltenheit im Wortlaut des Spiels (Mythic heißt „heroisch“).
- Hier:
  - `scripts/monitor_daten.py` übernimmt `items` in `stand.json` (guid, ort, insel, objekt, provinz) und die Felder `item`, `item_id` der Chronikzeilen.
  - Namen stehen unter `namen.items`, `namen.item_seltenheit` und `namen.objekte`.
  - Neuer Test in `test-monitor-daten.py`, Beschreibung in `docs/MONITOR.md`.
- Hinweis aus Kapitel I erledigt: „1 71438“ ist der Spezialist Gaius Julius Lupus, Vermögensfachmann (episch).
  - Die Zeile in der Monitor-Chronik ist beim Spieler berichtigt, mit Vermerk `korrigiert`; die alte Datei liegt daneben.
  - Korrektur in `chronik.html` unter „Korrekturen“; `werkstatt/erster-lauf/STAND.md` nachgezogen.
  - Im Spielstand bei 48:21 min sitzt Gaius schon in der Villa des Praetors auf Beneventum. Die zwei Kisten aus „Verlorene Fracht“ treiben bei 50:47 min noch im Meer.
- Geprüft:
  - Anno-Monitor: 39 Tests grün, darunter Autosave 9 und 11 als feste Testkopien.
  - Hier: `test-monitor-daten.py` (7 Tests) und `validate-data.mjs`.
  - Stand aus dem echten Autosave 11 ohne private Funde.
- Noch nicht hochgeladen: wartet auf die Freigabe des Spielers, zusammen mit den neuen Messdaten.
- Nachtrag: Hochgeladen auf Freigabe („Ja, hochladen“) als `c778e0d` und `e3214ee` (Messdaten, 84 Messungen bis 1:04 h Spielzeit); „Datenqualität“ und Pages für `e3214ee` grün, live geprüft (84 Messungen, Korrektur sichtbar, Register mit 12 Zeilen, ohne Konsolenfehler). Der Monitor lief dabei noch ohne Items; sie kommen nach seinem Neustart mit dem nächsten Upload. Die Tagebuch-Sitzung (Kapitel II, „In Arbeit“) hat dazu eine Nachricht bekommen.

## 2026-11-05 – Kapitel I „Zwanzig Bretter“ (Claude, Nebensitzung)

- Auftrag über die Monitor-Sitzung: Kapitel I als Tagebuch der Protagonistin mit Bericht. Vorgeschlagen war als Einschnitt die erste Bevölkerungsstufe, die ersten Plebejer (19:33 min Spielzeit, Aufnahme 16:34), als Alternative das erste Heiligtum (38:35 min). Spieler: „Bei den Plebejern“.
- Ohne Faktenblatt geschrieben (das Skript ist offen, `scripts/` lag bei der Monitor-Sitzung), direkt aus dem Anno-Monitor: Kurzwerte und Chronik der Welt, vollständige Messungen der Läufe ab 15:09 und 16:29, die Spielprotokolle vom 5.11. und das Bildschirmfoto vom Libertus. Welche Werte nur in den vollständigen Messungen stehen, sagt die Quellenzeile des Berichts.
- `chronik.html`:
  - Kapitel I mit Kopf, Bericht (Kennzahlen, Zeitachse, Quellen Q3, Q5 und neu Q6 Spielprotokoll), neun Tagebucheinträgen und Randnotiz „Abgeleitet“;
  - „Inseln und Provinzen“ mit Beneventum, Hortia Poenitentium, Umbra und Werddon;
  - Verweis auf das Kapitel im Inhalt.
- Register `erster-lauf-0004` bis `-0012`: Inselnahmen der drei Praetoren, erste Liberti, Kleiner Vicus, Bilanz im Plus, Tarragon respektvoll gegrüßt, die ersten Plebejer; als Abgeleitet, dass Zara Nitu vor Caesia Plebejer hatte.
- `roemisch.css` ergänzt: Kapitelkopf, Zeitachse, Einträge und Formen des Tagebuchs.
- Geprüft:
  - `validate-data.mjs` und `test-monitor-daten.py`;
  - Wortprüfung (Verneinungen, KI-Wörter) ohne Fund im neuen Text;
  - Browser bei 1280 und 375 px, hell und dunkel, ohne Konsolenfehler und ohne waagrechtes Scrollen.
  - Beim Gegenlesen zwei Lagerangaben im Tagebuch an die Messungen angepasst (25 Bretter beim ersten Gang, 6 bei der Zählung mit dem Kleinen Vicus).
- Hochgeladen auf Freigabe („Ja, hochladen“): `b3e3a10` (Messdaten, 72 Messungen bis 55:22 min, Skriptstand `067fbfb` der Monitor-Sitzung) und `21d4859` (Kapitel I). „Datenqualität“ für `21d4859` grün.
- Für eine Prüfung durch Codex:
  - Spielzeiten und Kurzwerte stehen in `saves/erster-lauf/data/monitor/tag-2026-11-05.json`.
  - Status, Wohnhäuser, Lager, Betriebe am Stichtag, Geldposten und die Zahlen der Praetoren liegen nur in den vollständigen Messungen beim Spieler.
  - Die Zeiten der Inselnahmen und Ereignisfenster kommen aus dem Spielprotokoll und sind zwischen die Messungen davor und danach eingeordnet.
- Hinweis an die Monitor-Sitzung: Bei „Zwillinge in der Zwickmühle“ (47:25 bis 48:21 min) steht als Belohnung „1 71438“, der Name fehlt im Katalog.

## 2026-11-05 – Ereignisse automatisch aus dem Monitor (Claude)

- Spieler: „können wir die ereignisse nicht irgenwie erfassen anders?“, danach „Ja, einbauen“.
- Im Anno-Monitor:
  - Entscheidungen aus dem Spielstand (QuestManager), mit Titel, Wahl, Kosten und Wirkung aus den Spieldaten;
  - Erkundung (DiscoveryManager, entdeckte Inseln je Provinz);
  - aus dem Spielprotokoll Inselnahmen von Spieler und Praetoren, Ereignisfenster (genaue Spielzeit der Entscheidung) und Bildschirmfotos.
  - Am echten Lauf geprüft: Libertus (Vorrat gekauft), „Begegnung mit einem Rivalen“ (Tarragon, respektvoll gegrüßt), Latium bis 12 entdeckte Inseln, Inselnahmen von Tarragon (Hortia Poenitentium), Zara Nitu (Umbra) und Athr Iorgwyn (Werddon).
- Hier: `publish-monitor.py` lässt Ereignisfenster und Bildschirmfotos weg (`monitor_daten.oeffentlich`), neue Felder in den Ereignissen; `docs/MONITOR.md`, `docs/ERSTER-LAUF.md`. Wirksam, sobald der Spieler den Monitor neu startet.

## 2026-11-05 – Erste Insel und erste Entscheidung im Register (Claude)

- Hochgeladen auf Freigabe („Ja, hochladen“): `a6e5341` (Partie-Name, Korrektur im Steckbrief), `0321ce3` (erste Messdaten, 8 Messungen bis 5:36 min). „Datenqualität“ und Pages grün, live geprüft.
- Spieler schickte zwei Bildschirmfotos vom Ereignis „Ein Libertus grüßt dich“ mit der Frage „nehmen wir sowas auch mit auf? geht das?“. Eingetragen (lokal): Register `erster-lauf-0002` (erste eigene Insel Beneventum, Q3) und `erster-lauf-0003` (Bretter gekauft, Q5 und Q3), Q5 unter Quellen, Startprovinz im Steckbrief, Landungsort unter „Offene Fragen“, Regeln unter „Ereignisse und Entscheidungen im Spiel“ in `docs/ERSTER-LAUF.md`. Der Monitor zeigt den Kauf im Geld (17.684 bei 4:38 min, 17.009 bei 5:36 min), die Entscheidung selbst nicht; Probe dazu auf der Tafel.

## 2026-11-05 – Partie-Name korrigiert, Datenweg mit der echten Partie geprüft (Claude)

- Erster Autosave der Partie um 15:52: Im Spielstand heißt sie „Caesia Varilla“ (Partie-Ordner und Firmenname), Weltkennung `anno117-1793890256`, Seed 6949, drei Erweiterungen, Praetoren Tarragon, Athr Iorgwyn, Zara Nitu. „Cassandra“ ist das Profil der Einstellungsübersicht. `data/monitor-sources.json` und `meta.json` stehen jetzt auf `partie: "Caesia Varilla"`; mit „Cassandra“ hätte das Hochlade-Skript die Welt nie gefunden.
- Chronik: Steckbrief der Partie mit „Name im Spielstand: Caesia Varilla“ (Q3), dazu ein Eintrag unter „Korrekturen“, weil dort seit dem ersten Push „Profil im Spiel: Cassandra“ stand.
- `publish-monitor.py --save erster-lauf --no-push`: Weltkennung gefunden und eingetragen, 3 Messungen, Stand aus Live (1:38 min Spielzeit, Geld 20.000, noch ohne eigene Insel), Prüfung auf Privates bestanden. Schwierigkeit und Erweiterungen kommen jetzt auch bei einem Live-Stand aus dem Spielstand. Nicht hochgeladen.

## 2026-11-05 – Caesia Varilla als Protagonistin, Chronik „Erster Lauf“ (Claude)

- Spieler: „Bitte berücksichtige die Datei lore/caesia-varilla.md als verbindliche Charaktergrundlage für unsere AnnoChronik. Baue Caesia als Protagonistin in die Website ein. Ihre weitere Geschichte entwickeln wir anhand des tatsächlichen Spielverlaufs. das ist der erste lauf“. Das Dossier hat er selbst hochgeladen (`6977952`); das Gerüst setzt darauf auf.
- Chronik heißt jetzt „Caesia Varilla · Erster Lauf“ unter `saves/erster-lauf/` (vorher Arbeitstitel „Cassandra“, `saves/cassandra/`); „Cassandra“ bleibt als Profil im Spiel und als Partie-Ordner für den Monitor. Umbenannt: Werkstattordner, `docs/ERSTER-LAUF.md`, Registerkennung `erster-lauf-0001`.
- Neuer Abschnitt I „Die Protagonistin“ (Etikett „Figurenkanon“, Stil `.ac-kanon`, Quelle Q4): Steckbrief, Wesen, Familie, Verlobung und die Nacht der Flucht als Vorgeschichte, nah am Dossier. Offenes steht unter „Offene Fragen“; der vorgeschlagene Name des Vaters erscheint auf der Seite nicht, weil er noch nicht festgelegt ist. Kein Amt, keine Statthalterschaft.
- Leitlinien des Dossiers in `docs/ERSTER-LAUF.md` übernommen. Versalziffern in den Versalzeilen (Ziffernart wurde von der font-Kurzschreibweise zurückgesetzt). Prüfungen grün, Browser hell und dunkel, 375 px.
- Freigabe zum Hochladen: „die seite kann dann auch live geschaltet werden“, Pages hatte der Spieler eingeschaltet.

## 2026-11-05 – Gerüst angelegt (Claude)

- Auftrag des Spielers: das Repo „gleich aufsetzen wie das TF3 Git dann mit Pages“; erste Partie ist seine neue Partie vom 5.11.2026 (Profil Cassandra). Vorher Briefing mit vier Antworten (`BRIEFING.md`): Kapitel nach Meilensteinen, Tagebuch der Protagonistin, römisches Design, Messdaten im Repo.
- Angelegt: Portal `index.html`, `saves/erster-lauf/` mit Chronikseite (Titelblatt, Steckbrief der Partie, Register, Tagebuch, Inseln und Provinzen, offene Fragen, Quellen Q1 bis Q3, Korrekturen), `data/worlds.json`, `data/monitor-sources.json`, Design `assets/roemisch.css` mit Lorbeer und Mäander (`scripts/ornamente.py`), Schriften EB Garamond und Cormorant (SIL OFL, aus der TF3-Chronik).
- Datenweg: `scripts/publish-monitor.py` liest den Anno-Monitor, schreibt `saves/erster-lauf/data/monitor/` (je Aufnahmetag eine Datei, `stand.json`, `index.json`) ohne Pfade, Dateinamen und Kontokennung; `scripts/monitor_daten.py` mit Tests. Probelauf an der alten Partie „Alexandra Lupara“ (nur lokal, nichts geschrieben): 14 Messungen, 92 Chronikzeilen, umbenannte Insel richtig, keine privaten Funde.
- Prüfungen: `scripts/validate-data.mjs` (Weltregister, Manifeste, Register, Quellenanker, Messdaten, Datenschutz), Action „Datenqualität“.
- Offen: siehe `AUFGABEN.md`.
