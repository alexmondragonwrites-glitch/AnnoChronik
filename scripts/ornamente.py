"""Ornamente der AnnoChronik als SVG-Masken erzeugen (römisch: Lorbeerkranz, Mäanderband; keltisch: Knotenring, Knotenband).

Die Seite färbt sie per Stylesheet ein (`mask-image`), deshalb sind sie hier einfarbig schwarz.
Aufruf: py -3 scripts/ornamente.py
"""

from __future__ import annotations

import math
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"


def _zahl(x: float) -> str:
    return f"{x:.1f}".rstrip("0").rstrip(".")


def lorbeer() -> str:
    """Offener Kranz aus zwei Zweigen, unten zusammengebunden (200 × 110)."""
    mx, my, r = 100.0, 38.0, 62.0
    teile: list[str] = []
    for seite in (-1, 1):                       # links, rechts (gespiegelt)
        punkte = []
        for i in range(0, 41):
            w = math.radians(96 + i * 2.75)         # von unten nach außen und oben
            punkte.append((mx + seite * -r * math.cos(w), my + r * math.sin(w)))
        d = "M" + " L".join(f"{_zahl(x)} {_zahl(y)}" for x, y in punkte)
        teile.append(f'<path d="{d}" fill="none" stroke="#000" stroke-width="2.2" stroke-linecap="round"/>')
        for n, k in enumerate(range(3, 41, 4)):
            w = math.radians(96 + k * 2.75)
            px, py = mx + seite * -r * math.cos(w), my + r * math.sin(w)
            tx, ty = seite * -(-math.sin(w)), math.cos(w)      # Wuchsrichtung entlang des Zweigs
            for aussen in (True, False):
                drehen = math.radians(38 if aussen else -38) * seite
                dx = tx * math.cos(drehen) - ty * math.sin(drehen)
                dy = tx * math.sin(drehen) + ty * math.cos(drehen)
                laenge = 11.5 - n * 0.35
                cx, cy = px + dx * laenge * 0.92, py + dy * laenge * 0.92
                grad = math.degrees(math.atan2(dy, dx))
                teile.append(f'<ellipse cx="{_zahl(cx)}" cy="{_zahl(cy)}" rx="{_zahl(laenge)}" ry="{_zahl(laenge * 0.36)}" '
                             f'transform="rotate({_zahl(grad)} {_zahl(cx)} {_zahl(cy)})"/>')
        w = math.radians(96 + 40 * 2.75)
        px, py = mx + seite * -r * math.cos(w), my + r * math.sin(w)
        tx, ty = seite * -(-math.sin(w)), math.cos(w)
        cx, cy = px + tx * 8, py + ty * 8
        teile.append(f'<ellipse cx="{_zahl(cx)}" cy="{_zahl(cy)}" rx="9" ry="3.2" '
                     f'transform="rotate({_zahl(math.degrees(math.atan2(ty, tx)))} {_zahl(cx)} {_zahl(cy)})"/>')
    teile.append(f'<path d="M86 101 Q100 92 114 101 M93 96 L100 108 L107 96" fill="none" stroke="#000" '
                 f'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="112" viewBox="0 0 200 112">'
            + "".join(teile) + "</svg>\n")


def maeander() -> str:
    """Laufender Mäander als Kachel (20 × 20), waagrecht zu wiederholen."""
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20">'
            '<path d="M0 19H20M2 19V1H18V13H8V7H12" fill="none" stroke="#000" stroke-width="2" '
            'stroke-linecap="square"/></svg>\n')


def _abstand(px: float, py: float, punkte: list[tuple[float, float]]) -> float:
    return min(math.hypot(px - x, py - y) for x, y in punkte)


def _konturen(mitte: dict[int, list[tuple[float, float]]], oben, breite: float, strich: float, luecke: float,
              geschlossen: bool) -> list[list[tuple[float, float]]]:
    """Beide Ränder jedes der zwei Stränge als Linienzüge (Knotenwerk mit Kontur).

    `oben(i, j)` sagt, ob Strang i am Punkt j an der nächsten Kreuzung oben liegt. Liegt er unten, bleibt
    um das obere Band eine Lücke (`luecke`), so dass es über dem unteren zu liegen scheint."""
    linien = []
    for i, pts in mitte.items():
        anderer, m = mitte[1 - i], len(pts)
        for seite in (-1, 1):
            zuege, zug, anfang = [], [], 0
            for j in range(m):
                if geschlossen:
                    (x0, y0), (x1, y1) = pts[j - 1], pts[(j + 1) % m]
                else:
                    (x0, y0), (x1, y1) = pts[max(j - 1, 0)], pts[min(j + 1, m - 1)]
                laenge = math.hypot(x1 - x0, y1 - y0)
                nx, ny = -(y1 - y0) / laenge, (x1 - x0) / laenge
                versatz = seite * (breite + strich) / 2
                px, py = pts[j][0] + nx * versatz, pts[j][1] + ny * versatz
                if not oben(i, j) and _abstand(px, py, anderer) < breite / 2 + strich + luecke:
                    if len(zug) > 1:
                        zuege.append((anfang, j - 1, zug))
                    zug = []
                    continue
                if not zug:
                    anfang = j
                zug.append((px, py))
            if len(zug) > 1:
                zuege.append((anfang, m - 1, zug))
            if geschlossen and len(zuege) > 1 and zuege[0][0] == 0 and zuege[-1][1] == m - 1:
                zuege[0] = (zuege[-1][0], zuege[0][1], zuege[-1][2] + zuege[0][2])   # über den Anfang hinweg verbinden
                zuege.pop()
            linien += [z for _, _, z in zuege]
    return linien


def _pfad(linien: list[list[tuple[float, float]]]) -> str:
    return " ".join("M" + " L".join(f"{_zahl(x)} {_zahl(y)}" for x, y in zug) for zug in linien)


def knotenband() -> str:
    """Zweisträngiges Flechtband als Kachel (24 × 14), waagrecht zu wiederholen.

    Zwei Bänder mit Kontur kreuzen sich zweimal je Kachel, abwechselnd oben und unten. An den Kachelrändern
    liegen sie am weitesten auseinander, deshalb schließen die Kacheln ohne Naht aneinander."""
    w, mitte_y, hub = 24.0, 7.0, 4.3
    breite, strich, luecke = 2.6, 1.1, 0.9
    xs = [-1.5 + (w + 3.0) * k / 150 for k in range(151)]
    mitte = {i: [(x, mitte_y + (hub if i == 0 else -hub) * math.cos(2 * math.pi * x / w)) for x in xs] for i in (0, 1)}

    def oben(i: int, j: int) -> bool:
        k = round((xs[j] - w / 4) / (w / 2))          # Kreuzungen bei w/4 + k·w/2
        return i == k % 2

    linien = _konturen(mitte, oben, breite, strich, luecke, geschlossen=False)
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="24" height="14" viewBox="0 0 24 14">'
            f'<path d="{_pfad(linien)}" fill="none" stroke="#000" stroke-width="{_zahl(strich)}" '
            'stroke-linejoin="round"/></svg>\n')


def knotenring() -> str:
    """Ring aus zwei verflochtenen Bändern (120 × 120), innen und außen von einer feinen Linie gefasst.

    Bewusst ohne Triskele oder anderes Zeichen: Aelwens Herrschaftssymbol steht noch nicht fest."""
    c, r, hub, n = 60.0, 40.0, 7.5, 7
    breite, strich, luecke = 4.6, 1.8, 1.6
    m = 480
    winkel = [2 * math.pi * k / m for k in range(m)]
    mitte = {i: [(c + (r + (hub if i == 0 else -hub) * math.cos(n * t)) * math.cos(t),
                  c + (r + (hub if i == 0 else -hub) * math.cos(n * t)) * math.sin(t)) for t in winkel] for i in (0, 1)}

    def oben(i: int, j: int) -> bool:
        k = round((n * winkel[j] - math.pi / 2) / math.pi)   # Kreuzungen bei n·θ = π/2 + kπ
        return i == k % 2

    linien = _konturen(mitte, oben, breite, strich, luecke, geschlossen=True)
    rahmen = "".join(f'<circle cx="{_zahl(c)}" cy="{_zahl(c)}" r="{_zahl(rr)}"/>'
                     for rr in (r + hub + breite / 2 + strich + 3.4, r - hub - breite / 2 - strich - 3.4))
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" viewBox="0 0 120 120">'
            f'<g fill="none" stroke="#000" stroke-linejoin="round"><path d="{_pfad(linien)}" stroke-width="{_zahl(strich)}"/>'
            f'<g stroke-width="{_zahl(strich * 0.75)}">{rahmen}</g></g></svg>\n')


def main() -> int:
    dateien = {"lorbeer.svg": lorbeer(), "maeander.svg": maeander(), "knotenband.svg": knotenband(), "knotenring.svg": knotenring()}
    for name, svg in dateien.items():
        (ASSETS / name).write_text(svg, encoding="utf-8")
    print(", ".join(dateien), "geschrieben")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
