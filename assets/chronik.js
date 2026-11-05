// AnnoChronik · Weltseite: Register aus data/events.json und Zeile zum Stand der Messdaten.
// Ohne Bibliotheken; die Seite bleibt ohne JavaScript lesbar.
(function () {
  "use strict";

  var ARTEN = { fakt: "Belegt", rekonstruktion: "Abgeleitet" };

  // Spielzeit in Millisekunden → „12:40 h“
  function spielzeit(ms) {
    if (typeof ms !== "number" || !isFinite(ms) || ms < 0) return "–";
    var minuten = Math.floor(ms / 60000);
    var h = Math.floor(minuten / 60);
    var m = minuten % 60;
    return h + ":" + (m < 10 ? "0" : "") + m + " h";
  }

  function datum(text) {
    var t = /^(\d{4})-(\d{2})-(\d{2})/.exec(text || "");
    return t ? Number(t[3]) + "." + Number(t[2]) + "." + t[1] : "–";
  }

  function zahl(n) {
    return typeof n === "number" ? Math.round(n).toLocaleString("de-DE") : "–";
  }

  function zelle(zeile, text, klasse) {
    var td = document.createElement("td");
    if (klasse) td.className = klasse;
    td.textContent = text;
    zeile.appendChild(td);
    return td;
  }

  function quellenLinks(td, quelle) {
    td.textContent = "";
    String(quelle || "").split(/[,;]\s*/).forEach(function (q, i) {
      if (!q) return;
      if (i) td.appendChild(document.createTextNode(" "));
      if (/^Q\d+$/.test(q)) {
        var a = document.createElement("a");
        a.className = "ac-q";
        a.href = "#" + q.toLowerCase();
        a.textContent = q;
        td.appendChild(a);
      } else {
        td.appendChild(document.createTextNode(q));
      }
    });
  }

  function register(eintraege) {
    var tbody = document.getElementById("register-zeilen");
    if (!tbody) return;
    tbody.textContent = "";
    var liste = eintraege.slice().sort(function (a, b) {
      return (a.spielzeit_ms || 0) - (b.spielzeit_ms || 0) || String(a.id).localeCompare(String(b.id));
    });
    if (!liste.length) {
      var leer = document.createElement("tr");
      zelle(leer, "Das Register füllt sich mit dem ersten Kapitel.", "ac-leer").colSpan = 5;
      tbody.appendChild(leer);
      return;
    }
    liste.forEach(function (e) {
      var tr = document.createElement("tr");
      tr.id = e.id;
      zelle(tr, e.game_time_label || spielzeit(e.spielzeit_ms), "ac-zeit");
      zelle(tr, datum(e.recorded), "ac-zeit");
      zelle(tr, ARTEN[e.kind] || e.kind, "ac-art");
      var td = zelle(tr, "");
      var titel = document.createElement("strong");
      titel.textContent = e.title;
      td.appendChild(titel);
      if (e.description) td.appendChild(document.createTextNode(" " + e.description));
      if (e.correction) {
        var k = document.createElement("em");
        k.textContent = " Korrigiert am " + datum(e.correction.date) + ": " + e.correction.note;
        td.appendChild(k);
      }
      quellenLinks(zelle(tr, ""), e.source);
      tbody.appendChild(tr);
    });
  }

  function messdaten(index) {
    var p = document.getElementById("messdaten");
    if (!p || !index || !index.messungen) return;
    p.textContent = "Messdaten: " + zahl(index.messungen) + " Messungen bis " + spielzeit(index.spielzeit_bis_ms) +
      " Spielzeit, zuletzt aufgenommen am " + datum(index.erfasst_bis) + ".";
  }

  function laden(pfad) {
    return fetch(pfad, { cache: "no-cache" }).then(function (r) {
      if (!r.ok) throw new Error(pfad + ": " + r.status);
      return r.json();
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    laden("data/events.json").then(register).catch(function () {
      var tbody = document.getElementById("register-zeilen");
      if (tbody) tbody.innerHTML = '<tr><td class="ac-leer" colspan="5">Das Register war gerade unerreichbar. Bitte die Seite neu laden.</td></tr>';
    });
    laden("data/manifest.json").then(function (manifest) {
      if (manifest && manifest.monitor) return laden(manifest.monitor).then(messdaten);
    }).catch(function () { /* Zeile bleibt beim Ausgangstext */ });
  });
})();
