// AnnoChronik · Datenprüfung: Weltregister, Manifeste, Register, Messdaten, Quellenanker und Datenschutz.
// Aufruf: node scripts/validate-data.mjs   (ohne Pakete; läuft auch in der GitHub-Prüfung)
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const fehler = [];
const meldung = (datei, text) => fehler.push(`${datei}: ${text}`);

// wie scripts/monitor_daten.py: Laufwerkspfade, Benutzer- und Dokumentenordner, Kontoordner, GUID-Kennungen
const PRIVAT = /(?<![A-Za-z])[A-Za-z]:[\\/]|\/(?:Users|home)\/|\baccounts\b|Dokumente|Documents|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/i;
const KONTO = /[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|accounts[\\/]/i;
const TAG = /^\d{4}-\d{2}-\d{2}$/;

function lesen(pfad) {
  return readFileSync(join(ROOT, pfad), "utf8");
}

function json(pfad) {
  try {
    return JSON.parse(lesen(pfad));
  } catch (e) {
    meldung(pfad, `kein gültiges JSON (${e.message})`);
    return null;
  }
}

function dateien(ordner) {
  const voll = join(ROOT, ordner);
  if (!existsSync(voll)) return [];
  return readdirSync(voll).flatMap((name) => {
    if (name === ".git" || name === "node_modules" || name === "__pycache__" || name === ".publish-cache") return [];
    const rel = ordner ? `${ordner}/${name}` : name;
    return statSync(join(ROOT, rel)).isDirectory() ? dateien(rel) : [rel];
  });
}

// 1. Weltregister
const welten = json("data/worlds.json");
const ids = new Set();
if (!Array.isArray(welten) || !welten.length) meldung("data/worlds.json", "braucht mindestens eine Welt");
for (const w of welten || []) {
  const wo = `data/worlds.json (${w.id})`;
  if (!/^[a-z0-9-]+$/.test(w.id || "")) meldung(wo, "Kennung nur aus Kleinbuchstaben, Ziffern und Bindestrich");
  if (ids.has(w.id)) meldung(wo, "Kennung doppelt");
  ids.add(w.id);
  for (const feld of ["name", "path", "status", "started"]) if (!w[feld]) meldung(wo, `Feld ${feld} fehlt`);
  if (w.path !== `saves/${w.id}/`) meldung(wo, `path muss saves/${w.id}/ sein`);
  if (w.started && !TAG.test(w.started)) meldung(wo, "started im Format JJJJ-MM-TT");
  if (!["laufend", "abgeschlossen"].includes(w.status)) meldung(wo, "status ist laufend oder abgeschlossen");
  for (const seite of ["index.html", w.page || "chronik.html"]) {
    if (!existsSync(join(ROOT, w.path || "", seite))) meldung(wo, `${w.path}${seite} fehlt`);
  }
}

// 2. Je Welt: meta, manifest, Register, Messdaten, Quellenanker
for (const id of ids) {
  const basis = `saves/${id}`;
  const meta = json(`${basis}/data/meta.json`);
  if (meta && meta.id !== id) meldung(`${basis}/data/meta.json`, `id ist ${meta.id}, erwartet ${id}`);
  const manifest = json(`${basis}/data/manifest.json`);
  if (manifest) {
    if (!manifest.latestReport || !existsSync(join(ROOT, basis, manifest.latestReport))) {
      meldung(`${basis}/data/manifest.json`, "latestReport zeigt auf keine vorhandene Seite");
    }
    if (manifest.monitor && !existsSync(join(ROOT, basis, manifest.monitor))) {
      meldung(`${basis}/data/manifest.json`, `monitor ${manifest.monitor} fehlt`);
    }
  }

  const seiten = dateien(basis).filter((d) => d.endsWith(".html"));
  const anker = new Set(seiten.flatMap((s) => [...lesen(s).matchAll(/id="(q\d+)"/g)].map((m) => m[1])));
  for (const s of seiten) {
    for (const m of lesen(s).matchAll(/href="#(q\d+)"/g)) {
      if (!anker.has(m[1])) meldung(s, `Quellenverweis #${m[1]} ohne Eintrag unter Quellen`);
    }
  }

  const ereignisse = json(`${basis}/data/events.json`);
  const eids = new Set();
  if (!Array.isArray(ereignisse)) meldung(`${basis}/data/events.json`, "muss eine Liste sein");
  for (const e of ereignisse || []) {
    const wo = `${basis}/data/events.json (${e.id})`;
    if (!new RegExp(`^${id}-\\d{4}$`).test(e.id || "")) meldung(wo, `id im Format ${id}-NNNN`);
    if (eids.has(e.id)) meldung(wo, "id doppelt");
    eids.add(e.id);
    if (!["fakt", "rekonstruktion"].includes(e.kind)) meldung(wo, "kind ist fakt (Belegt) oder rekonstruktion (Abgeleitet); Erzähltes gehört ins Tagebuch");
    for (const feld of ["category", "title", "description", "source"]) {
      if (typeof e[feld] !== "string" || !e[feld].trim()) meldung(wo, `Feld ${feld} fehlt`);
    }
    if (!TAG.test(e.recorded || "")) meldung(wo, "recorded (Tag der Aufnahme) im Format JJJJ-MM-TT");
    const zeitOk = Number.isInteger(e.spielzeit_ms) && e.spielzeit_ms >= 0;
    if (!zeitOk && !e.game_time_label) meldung(wo, "spielzeit_ms (ganze Zahl ≥ 0) oder game_time_label nötig");
    for (const q of String(e.source || "").match(/Q\d+/g) || []) {
      if (!anker.has(q.toLowerCase())) meldung(wo, `Quelle ${q} steht unter Quellen der Chronik nicht`);
    }
    if (e.correction && (!TAG.test(e.correction.date || "") || !e.correction.note)) meldung(wo, "correction braucht date und note");
  }

  // Karte: je Kapitel ein Kartenstand (von Anno-Monitor/karte.py), Bilder unter images/karte/
  const kartePfad = `${basis}/data/karte.json`;
  const karte = existsSync(join(ROOT, kartePfad)) ? json(kartePfad) : null;
  if (karte) {
    if (karte.schema !== 1) meldung(kartePfad, "schema 1 erwartet");
    for (const u of karte.umbenennungen || []) {
      if (!Number.isInteger(u.bereich) || !u.name || !Number.isInteger(u.ab_ms)) meldung(kartePfad, "Umbenennung braucht bereich, name und ab_ms");
    }
    const kartenseite = existsSync(join(ROOT, basis, "karte.html")) ? lesen(`${basis}/karte.html`) : null;
    if (!kartenseite) meldung(kartePfad, `${basis}/karte.html fehlt`);
    const chronikSeite = existsSync(join(ROOT, basis, "chronik.html")) ? lesen(`${basis}/chronik.html`) : "";
    for (const s of karte.staende || []) {
      const wo = `${kartePfad} (${s.id})`;
      if (!/^kapitel-\d+$/.test(s.id || "")) meldung(wo, "id im Format kapitel-N");
      for (const f of ["von_ms", "bis_ms", "spielstand_ms"]) if (!Number.isInteger(s[f])) meldung(wo, `${f} fehlt`);
      if (!(s.spielstand_ms > s.von_ms && s.spielstand_ms <= s.bis_ms)) meldung(wo, "der Spielstand liegt nicht im Kapitel");
      if (!TAG.test(s.aufgenommen || "")) meldung(wo, "aufgenommen im Format JJJJ-MM-TT");
      if (!chronikSeite.includes(`id="${s.id}"`)) meldung(wo, "Kapitel fehlt in chronik.html");
      if (kartenseite && !kartenseite.includes(`id="${s.id}"`)) meldung(`${basis}/karte.html`, `Kartenstand ${s.id} fehlt; karte.py erneut laufen lassen`);
      if (!Array.isArray(s.karten) || !s.karten.length) meldung(wo, "braucht mindestens eine Karte");
      for (const k of s.karten || []) {
        for (const bild of [k.bild, k.klein]) {
          if (!/^images\/karte\/[a-z0-9-]+\.webp$/.test(bild || "")) {
            meldung(wo, `Bildpfad ${bild} unerwartet`);
            continue;
          }
          const voll = join(ROOT, basis, bild);
          if (!existsSync(voll)) meldung(wo, `${bild} fehlt`);
          else if (statSync(voll).size > 3 * 1024 * 1024) meldung(wo, `${bild} ist größer als 3 MB`);
        }
      }
    }
  }

  const index = manifest && manifest.monitor ? json(`${basis}/${manifest.monitor}`) : null;
  if (index) {
    const ordner = dirname(`${basis}/${manifest.monitor}`);
    let summe = 0;
    for (const t of index.tage || []) {
      const tag = json(`${ordner}/${t.datei}`);
      if (!tag) continue;
      if ((tag.messungen || []).length !== t.messungen) meldung(`${ordner}/${t.datei}`, "Zahl der Messungen passt nicht zu index.json");
      if ((tag.ereignisse || []).length !== t.ereignisse) meldung(`${ordner}/${t.datei}`, "Zahl der Ereignisse passt nicht zu index.json");
      summe += t.messungen;
    }
    if (summe !== index.messungen) meldung(`${ordner}/index.json`, `messungen ${index.messungen}, in den Tagen ${summe}`);
    if (index.stand && !existsSync(join(ROOT, ordner, index.stand))) meldung(`${ordner}/index.json`, `stand ${index.stand} fehlt`);
    if (meta && meta.monitor && meta.monitor.world_id && meta.monitor.world_id !== index.world_id) {
      meldung(`${basis}/data/meta.json`, "monitor.world_id passt nicht zu den Messdaten");
    }
  }
}

// 3. Monitor-Quellen gehören zu bekannten Welten
for (const q of json("data/monitor-sources.json") || []) {
  if (!ids.has(q.save)) meldung("data/monitor-sources.json", `Welt ${q.save} steht nicht im Weltregister`);
  if (q.world_id !== null && !/^anno117-[\w-]+$/.test(q.world_id || "")) meldung("data/monitor-sources.json", `world_id ${q.world_id} unbekannten Formats`);
}

// 4. Datenschutz: Daten ohne Pfade und Konten; im ganzen Repo keine Kontokennung
const alle = dateien("");
for (const d of alle.filter((d) => d.endsWith(".json") && (d.startsWith("data/") || /^saves\/[^/]+\/data\//.test(d)))) {
  const text = lesen(d);
  const m = PRIVAT.exec(text);
  if (m) meldung(d, `enthält etwas wie einen Pfad oder eine Kontokennung („${m[0]}“)`);
}
const MUSTERDATEIEN = new Set(["scripts/validate-data.mjs", "scripts/monitor_daten.py"]); // definieren die Muster selbst
for (const d of alle.filter((d) => /\.(json|html|md|js|mjs|py|css|txt|yml)$/.test(d) && !MUSTERDATEIEN.has(d))) {
  const m = KONTO.exec(lesen(d));
  if (m) meldung(d, `enthält eine Kontokennung oder einen Kontoordner („${m[0]}“)`);
}
for (const d of alle.filter((d) => /^saves\/[^/]+\/images\/.+\.(webp|png|jpe?g)$/i.test(d))) {
  const m = KONTO.exec(readFileSync(join(ROOT, d)).toString("latin1"));
  if (m) meldung(d, `Bild enthält eine Kontokennung oder einen Kontoordner („${m[0]}“), etwa in den Metadaten`);
}

if (fehler.length) {
  console.error(`Datenprüfung: ${fehler.length} Fehler`);
  for (const f of fehler) console.error("  - " + f);
  process.exit(1);
}
console.log(`Datenprüfung ok: ${ids.size} Welt(en), ${alle.length} Dateien geprüft.`);
