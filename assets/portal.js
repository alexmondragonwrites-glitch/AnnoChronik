// AnnoChronik · Portal: Partien aus data/worlds.json. Die Karten im HTML bleiben ohne JavaScript stehen.
(function () {
  "use strict";

  function datum(text) {
    var t = /^(\d{4})-(\d{2})-(\d{2})/.exec(text || "");
    return t ? Number(t[3]) + "." + Number(t[2]) + "." + t[1] : "";
  }

  function karte(w) {
    var a = document.createElement("a");
    a.className = "ac-welt";
    a.href = w.path + (w.page || "chronik.html");
    var status = document.createElement("span");
    status.className = "ac-status";
    status.textContent = w.status === "abgeschlossen"
      ? "abgeschlossen" + (w.ended ? " am " + datum(w.ended) : "")
      : (w.untertitel ? w.untertitel + " · seit " : "läuft seit ") + datum(w.started);
    var h3 = document.createElement("h3");
    h3.textContent = w.name;
    var p = document.createElement("p");
    p.textContent = w.description || "";
    var mehr = document.createElement("p");
    mehr.className = "ac-mehr";
    mehr.textContent = "Zur Chronik";
    a.append(status, h3, p, mehr);
    return a;
  }

  document.addEventListener("DOMContentLoaded", function () {
    var ziel = document.getElementById("welten-liste");
    if (!ziel) return;
    fetch("data/worlds.json", { cache: "no-cache" })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (welten) {
        if (!Array.isArray(welten) || !welten.length) return;
        ziel.textContent = "";
        welten.forEach(function (w) { ziel.appendChild(karte(w)); });
      })
      .catch(function () { /* statische Karten bleiben */ });
  });
})();
