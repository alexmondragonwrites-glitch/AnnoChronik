// AnnoChronik · neue Partie anlegen: Ordner, Seiten (Chronik und Karte), Daten und Einträge in den Registern.
// node scripts/new-save.mjs --id neue-partie --name "Neue Partie" --partie "Profilname" [--started JJJJ-MM-TT]
//   [--untertitel "Zweiter Lauf"] [--figur "Name der Figur"] [--farbe dunkelblau]
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const args = Object.fromEntries(process.argv.slice(2).reduce((paare, a, i, alle) => {
  if (a.startsWith("--")) paare.push([a.slice(2), alle[i + 1] && !alle[i + 1].startsWith("--") ? alle[i + 1] : true]);
  return paare;
}, []));

const id = args.id;
const name = args.name;
const partie = args.partie || name;
const started = args.started || new Date().toISOString().slice(0, 10);
const untertitel = typeof args.untertitel === "string" ? args.untertitel : "";
const figur = typeof args.figur === "string" ? args.figur : "";
const farbe = typeof args.farbe === "string" ? args.farbe : "";
if (!/^[a-z0-9-]+$/.test(id || "") || !name || (farbe && !/^[a-z]+$/.test(farbe))) {
  console.error('Aufruf: node scripts/new-save.mjs --id kennung --name "Name" [--partie "Profilname"] [--started JJJJ-MM-TT] [--untertitel "Zweiter Lauf"] [--figur "Name"] [--farbe dunkelblau]');
  process.exit(2);
}
const basis = join(ROOT, "saves", id);
if (existsSync(basis)) {
  console.error(`saves/${id} gibt es schon.`);
  process.exit(3);
}

const json = (obj) => JSON.stringify(obj, null, 2) + "\n";
const schreiben = (pfad, text) => {
  mkdirSync(dirname(pfad), { recursive: true });
  writeFileSync(pfad, text, "utf8");
};
const html = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const [j, m, t] = started.split("-");
const titel = html(untertitel ? `${name} · ${untertitel}` : name);
const oben = `Anno 117 · Pax Romana${untertitel ? ` · ${html(untertitel)}` : ""}`;
const wurzel = `<html lang="de"${farbe ? ` data-farbe="${html(farbe)}"` : ""}>`;
const fuss = `<footer class="ac-fuss"><div class="ac-maeander" aria-hidden="true"></div>
  <div class="ac-fuss-innen"><p><a href="../../">AnnoChronik</a> · Chroniken eigener Partien in Anno 117: Pax Romana.</p>
  <p>Eine private Fan-Chronik, unabhängig von Ubisoft. Anno ist eine Marke von Ubisoft Entertainment.</p></div>
</footer>`;
const abschnitt = (kennung, nr, ueberschrift, inhalt = "") => `  <section class="ac-abschnitt" id="${kennung}" aria-labelledby="${kennung}-titel">
    <h2 id="${kennung}-titel"><span class="ac-nr">${nr}</span>${ueberschrift}</h2>
    <div class="ac-maeander" aria-hidden="true"></div>
${inhalt}  </section>`;

schreiben(join(basis, "index.html"), `<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${titel} · AnnoChronik</title>
<meta http-equiv="refresh" content="0; url=chronik.html">
<link rel="canonical" href="chronik.html">
</head>
<body><p><a href="chronik.html">Zur Chronik „${titel}“</a></p></body>
</html>
`);

schreiben(join(basis, "chronik.html"), `<!doctype html>
${wurzel}
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${titel} · AnnoChronik</title>
<link rel="stylesheet" href="../../assets/roemisch.css">
<script src="../../assets/chronik.js" defer></script>
</head>
<body>
<header class="ac-kopf">
  <div class="ac-kopf-innen"><a class="ac-marke" href="../../">AnnoChronik</a>
    <nav aria-label="Abschnitte"><a href="#register">Register</a><a href="#kapitel">Kapitel</a><a href="karte.html">Karte</a><a href="#quellen">Quellen</a></nav></div>
  <div class="ac-maeander" aria-hidden="true"></div>
</header>
<main data-welt="${id}">
  <section class="ac-titelblatt" aria-labelledby="titel">
    <p class="ac-oben">${oben}</p>
    <div class="ac-lorbeer" aria-hidden="true"></div>
    <h1 id="titel">${html(name)}</h1>
    <p class="ac-zeile">Begonnen am ${Number(t)}.${Number(m)}.${j}</p>
    <div class="ac-maeander" aria-hidden="true"></div>
  </section>
  <p class="ac-messdaten" id="messdaten" aria-live="polite">Die Messdaten beginnen mit dem ersten Autosave der Partie.</p>
${abschnitt("register", "I", "Register", `    <div class="ac-tabelle-rahmen"><table class="ac-register">
      <thead><tr><th scope="col">Spielzeit</th><th scope="col">Aufnahme</th><th scope="col">Art</th><th scope="col">Ereignis</th><th scope="col">Quelle</th></tr></thead>
      <tbody id="register-zeilen"><tr><td class="ac-leer" colspan="5">Das Register lädt …</td></tr></tbody>
    </table></div>
`)}
${abschnitt("kapitel", "II", "Kapitel")}
${abschnitt("inseln", "III", "Inseln und Provinzen")}
${abschnitt("fragen", "IV", "Offene Fragen")}
${abschnitt("quellen", "V", "Quellen", `    <ol class="ac-quellen"></ol>
`)}
${abschnitt("korrekturen", "VI", "Korrekturen")}
</main>
${fuss}
</body>
</html>
`);

schreiben(join(basis, "karte.html"), `<!doctype html>
${wurzel}
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Karte · ${titel} · AnnoChronik</title>
<meta name="description" content="Karte der Partie ${titel}, je Kapitel ein Stand, gezeichnet aus dem Spielstand.">
<link rel="stylesheet" href="../../assets/roemisch.css">
<script src="../../assets/karte.js" defer></script>
</head>
<body>
<header class="ac-kopf">
  <div class="ac-kopf-innen"><a class="ac-marke" href="../../">AnnoChronik</a>
    <nav aria-label="Abschnitte"><a href="chronik.html">Chronik</a><a href="chronik.html#kapitel">Kapitel</a><a href="chronik.html#register">Register</a><a href="karte.html" aria-current="page">Karte</a></nav></div>
  <div class="ac-maeander" aria-hidden="true"></div>
</header>
<main data-welt="${id}">
  <section class="ac-titelblatt" aria-labelledby="titel">
    <p class="ac-oben">${oben}</p>
    <div class="ac-lorbeer" aria-hidden="true"></div>
    <h1 id="titel">Die Karte</h1>
    <p class="ac-unter">Die Provinz zum Ende jedes Kapitels</p>
    <div class="ac-maeander" aria-hidden="true"></div>
  </section>
  <p class="ac-hinweis">Jede Karte zeigt die Provinz so, wie sie im letzten Spielstand vor dem Ende eines Kapitels aussieht. Mit den Ziffern wählst du das Kapitel; ein Klick auf die Karte öffnet sie in voller Größe.</p>
  <section class="ac-karte-buehne" aria-label="Kartenstände">
    <!-- KARTE:ANFANG (von Anno-Monitor/karte.py geschrieben, nicht von Hand ändern) -->
    <p class="ac-hinweis">Die erste Karte entsteht mit dem ersten Kapitel.</p>
    <!-- KARTE:ENDE -->
  </section>
  <section class="ac-abschnitt" id="zeichen" aria-labelledby="zeichen-titel">
    <h2 id="zeichen-titel">Zeichen der Karte</h2>
    <div class="ac-maeander" aria-hidden="true"></div>
    <!-- ZEICHEN:ANFANG (von Anno-Monitor/karte.py geschrieben, nicht von Hand ändern) -->
    <p class="ac-hinweis">Die Zeichen erscheinen mit der ersten Karte.</p>
    <!-- ZEICHEN:ENDE -->
    <p class="ac-schluss" aria-hidden="true">❦</p>
  </section>
  <section class="ac-abschnitt" id="entstehung" aria-labelledby="entstehung-titel">
    <h2 id="entstehung-titel">Wie die Karte entsteht</h2>
    <div class="ac-maeander" aria-hidden="true"></div>
    <div class="ac-bericht">
      <span class="ac-etikett">Belegt</span>
      <ul>
        <li><b>Aus dem Spielstand:</b> Lage und Drehung jeder Insel, Wohnhäuser, Betriebe und Lager, Straßen, wem eine Insel gehört und welche Inseln schon entdeckt sind.</li>
        <li><b>Aus den Inseldaten des Spiels:</b> Küsten, Höhen, Flüsse und Wald. Der Wald folgt der Vorlage der Insel; wo gebaut ist, fehlt er.</li>
        <li><b>Namen</b> wie im Spiel. Inseln, die der Spieler umbenannt hat, tragen den neuen Namen ab der Umbenennung.</li>
      </ul>
      <p class="ac-quelle">Gezeichnet für die Chronik vom Anno-Monitor auf dem Rechner des Spielers: Pergament, Wasserlinien, Schummerung, Farben und Schrift. Bilder aus dem Spiel sind nicht verwendet. Jede Karte nennt die Spielzeit ihres Spielstands und den Tag der Aufnahme.</p>
    </div>
    <p class="ac-schluss" aria-hidden="true">❦</p>
  </section>
</main>
${fuss}
</body>
</html>
`);

schreiben(join(basis, "data", "meta.json"), json({
  id, name, ...(untertitel ? { lauf: untertitel } : {}), name_status: "Arbeitstitel", game: "Anno 117: Pax Romana", status: "laufend", started,
  ...(figur ? { protagonistin: { name: figur } } : {}),
  ...(farbe ? { farbe } : {}),
  monitor: { partie, world_id: null },
}));
schreiben(join(basis, "data", "manifest.json"), json({ latestReport: "chronik.html", monitor: null }));
schreiben(join(basis, "data", "events.json"), "[]\n");
schreiben(join(basis, "data", "karte.json"), json({
  schema: 1,
  hinweis: "Von Anno-Monitor/karte.py erzeugt: je Kapitel ein Kartenstand nach dem letzten Spielstand vor dem Einschnitt. Umbenennungen trägt ein, wer ein Kapitel schreibt; sie gelten ab ab_ms.",
  umbenennungen: [],
  staende: [],
}));
schreiben(join(ROOT, "werkstatt", id, "STAND.md"), `# ${untertitel ? `${name} · ${untertitel}` : name} · Stand\n\nAngelegt am ${started}. Noch kein Kapitel; nächste freie Quellennummer: Q1.\n`);

const weltenPfad = join(ROOT, "data", "worlds.json");
const welten = JSON.parse(readFileSync(weltenPfad, "utf8"));
welten.push({ id, name, ...(untertitel ? { untertitel } : {}), path: `saves/${id}/`, page: "chronik.html", status: "laufend", started, description: "" });
writeFileSync(weltenPfad, json(welten), "utf8");
const quellenPfad = join(ROOT, "data", "monitor-sources.json");
const quellen = JSON.parse(readFileSync(quellenPfad, "utf8"));
quellen.push({ save: id, name: untertitel || name, partie, world_id: null });
writeFileSync(quellenPfad, json(quellen), "utf8");
console.log(`Angelegt: saves/${id}/ und werkstatt/${id}/, eingetragen in data/worlds.json und data/monitor-sources.json.`);
