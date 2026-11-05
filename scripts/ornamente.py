"""Ornamente der AnnoChronik als SVG-Masken erzeugen (Lorbeerkranz, Mäanderband).

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


def main() -> int:
    (ASSETS / "lorbeer.svg").write_text(lorbeer(), encoding="utf-8")
    (ASSETS / "maeander.svg").write_text(maeander(), encoding="utf-8")
    print("lorbeer.svg und maeander.svg geschrieben")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
