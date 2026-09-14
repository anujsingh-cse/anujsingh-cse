#!/usr/bin/env python3
"""Render assets/revised.svg — a library-style date stamp for the colophon.

The only dynamic element on the page: the date advances daily via CI.
No network, no fake data. Stdlib only.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "revised.svg"

STAMP = """<svg xmlns="http://www.w3.org/2000/svg" width="170" height="64" viewBox="0 0 170 64" role="img" aria-label="revised {date}">
  <style>
    text {{ font: 11px ui-monospace, SFMono-Regular, Consolas, monospace; letter-spacing: 2.5px; }}
    .ink {{ fill: #a13d2d; }}
    .frame {{ fill: none; stroke: #a13d2d; stroke-width: 2; }}
    @media (prefers-color-scheme: dark) {{
      .ink {{ fill: #e07a5f; }}
      .frame {{ stroke: #e07a5f; }}
    }}
  </style>
  <g transform="rotate(-4 85 32)" opacity="0.92">
    <rect x="3" y="3" width="164" height="58" rx="6" class="frame"/>
    <text x="85" y="28" text-anchor="middle" class="ink">REVISED</text>
    <text x="85" y="48" text-anchor="middle" class="ink" font-size="13">{date}</text>
  </g>
</svg>
"""


def main() -> int:
    try:
        stamp_date = date.today().strftime("%d %b %Y").upper()
        svg = STAMP.format(date=stamp_date)
    except Exception as e:  # noqa: BLE001
        print(f"colophon: render failed: {e}", file=sys.stderr)
        return 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(svg, encoding="utf-8")
    print(f"colophon: wrote {OUT} ({stamp_date})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
