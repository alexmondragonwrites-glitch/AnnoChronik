// AnnoChronik · neue Partie anlegen: Ordner, Seiten, Daten und Einträge in den Registern.
// node scripts/new-save.mjs --id neue-partie --name "Neue Partie" --partie "Profilname" [--started JJJJ-MM-TT]
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
if (!/^[a-z0-9-]+$/.test(id || "") || !name) {
  console.error('Aufruf: node scripts/new-save.mjs --id kennung --name "Name" [--partie "Profilname"] [--started JJJJ-MM-TT]');
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

schreiben(join(basis, "index.html"), `<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${html(name)} · AnnoChronik</title>
<meta http-equiv="refresh" content="0; url=chronik.html">
<link rel="canonical" href="chronik.html">
</head>
<body><p><a href="chronik.html">Zur Chronik „${html(name)}“</a></p></body>
</html>
`);

schreiben(join(basis, "chronik.html"), `<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${html(name)} · AnnoChronik</title>
<link rel="stylesheet" href="../../assets/roemisch.css">
<script src="../../assets/chronik.js" defer></script>
</head>
<body>
<header class="ac-kopf">
  <div class="ac-kopf-innen"><a class="ac-marke" href="../../">AnnoChronik</a>
    <nav aria-label="Abschnitte"><a href="#register">Register</a><a href="#kapitel">Kapitel</a><a href="#quellen">Quellen</a></nav></div>
  <div class="ac-maeander" aria-hidden="true"></div>
</header>
<main data-welt="${id}">
  <section class="ac-titelblatt" aria-labelledby="titel">
    <p class="ac-oben">Anno 117 · Pax Romana</p>
    <div class="ac-lorbeer" aria-hidden="true"></div>
    <h1 id="titel">${html(name)}</h1>
    <p class="ac-zeile">Begonnen am ${Number(t)}.${Number(m)}.${j}</p>
    <div class="ac-maeander" aria-hidden="true"></div>
  </section>
  <p class="ac-messdaten" id="messdaten" aria-live="polite">Die Messdaten beginnen mit dem ersten Autosave der Partie.</p>
  <section class="ac-abschnitt" id="register" aria-labelledby="register-titel">
    <h2 id="register-titel"><span class="ac-nr">I</span>Register</h2>
    <div class="ac-maeander" aria-hidden="true"></div>
    <div class="ac-tabelle-rahmen"><table class="ac-register">
      <thead><tr><th scope="col">Spielzeit</th><th scope="col">Aufnahme</th><th scope="col">Art</th><th scope="col">Ereignis</th><th scope="col">Quelle</th></tr></thead>
      <tbody id="register-zeilen"><tr><td class="ac-leer" colspan="5">Das Register lädt …</td></tr></tbody>
    </table></div>
  </section>
  <section class="ac-abschnitt" id="kapitel" aria-labelledby="kapitel-titel">
    <h2 id="kapitel-titel"><span class="ac-nr">II</span>Kapitel</h2>
    <div class="ac-maeander" aria-hidden="true"></div>
  </section>
  <section class="ac-abschnitt" id="quellen" aria-labelledby="quellen-titel">
    <h2 id="quellen-titel"><span class="ac-nr">III</span>Quellen</h2>
    <div class="ac-maeander" aria-hidden="true"></div>
    <ol class="ac-quellen"></ol>
  </section>
</main>
<footer class="ac-fuss"><div class="ac-maeander" aria-hidden="true"></div>
  <div class="ac-fuss-innen"><p><a href="../../">AnnoChronik</a> · Chroniken eigener Partien in Anno 117: Pax Romana.</p>
  <p>Eine private Fan-Chronik, unabhängig von Ubisoft. Anno ist eine Marke von Ubisoft Entertainment.</p></div>
</footer>
</body>
</html>
`);

schreiben(join(basis, "data", "meta.json"), json({
  id, name, name_status: "Arbeitstitel", game: "Anno 117: Pax Romana", status: "laufend", started,
  monitor: { partie, world_id: null },
}));
schreiben(join(basis, "data", "manifest.json"), json({ latestReport: "chronik.html", monitor: null }));
schreiben(join(basis, "data", "events.json"), "[]\n");
schreiben(join(ROOT, "werkstatt", id, "STAND.md"), `# ${name} · Stand\n\nAngelegt am ${started}. Noch kein Kapitel; nächste freie Quellennummer: Q1.\n`);

const weltenPfad = join(ROOT, "data", "worlds.json");
const welten = JSON.parse(readFileSync(weltenPfad, "utf8"));
welten.push({ id, name, path: `saves/${id}/`, page: "chronik.html", status: "laufend", started, description: "" });
writeFileSync(weltenPfad, json(welten), "utf8");
const quellenPfad = join(ROOT, "data", "monitor-sources.json");
const quellen = JSON.parse(readFileSync(quellenPfad, "utf8"));
quellen.push({ save: id, name, partie, world_id: null });
writeFileSync(quellenPfad, json(quellen), "utf8");
console.log(`Angelegt: saves/${id}/ und werkstatt/${id}/, eingetragen in data/worlds.json und data/monitor-sources.json.`);
