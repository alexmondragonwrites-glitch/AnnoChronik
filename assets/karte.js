// AnnoChronik · Kartenseite: Kapitelwahl ohne Neuladen.
// Ohne JavaScript stehen alle Kartenstände untereinander, die Ziffern springen dann zum Kapitel.
(function () {
  "use strict";

  var wahl = document.querySelector(".ac-karte-wahl");
  var staende = Array.prototype.slice.call(document.querySelectorAll(".ac-karte-stand"));
  if (!wahl || !staende.length) return;
  var links = Array.prototype.slice.call(wahl.querySelectorAll("a[data-stand]"));
  document.documentElement.classList.add("ac-karte-js");

  function vorhanden(id) {
    return staende.some(function (f) { return f.id === id; });
  }

  function zeigen(id) {
    if (!vorhanden(id)) id = staende[staende.length - 1].id;
    staende.forEach(function (f) { f.classList.toggle("ist-aktiv", f.id === id); });
    links.forEach(function (a) {
      if (a.getAttribute("data-stand") === id) a.setAttribute("aria-current", "true");
      else a.removeAttribute("aria-current");
    });
    return id;
  }

  links.forEach(function (a, i) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var id = zeigen(a.getAttribute("data-stand"));
      if (history.replaceState) history.replaceState(null, "", "#" + id);
    });
    a.addEventListener("keydown", function (e) {
      var ziel = e.key === "ArrowRight" ? links[i + 1] : e.key === "ArrowLeft" ? links[i - 1] : null;
      if (!ziel) return;
      e.preventDefault();
      ziel.focus();
      ziel.click();
    });
  });

  window.addEventListener("hashchange", function () { zeigen(location.hash.slice(1)); });
  zeigen(location.hash.slice(1));
})();
