#!/usr/bin/env python3
"""List local design references from awesome-design-md."""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parents[1] / "references" / "brands"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="List local DESIGN.md references.")
    parser.add_argument("query", nargs="?", help="Optional case-insensitive filter.")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="Path to design-md root.")
    parser.add_argument("--paths", action="store_true", help="Print absolute DESIGN.md paths.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser()
    if not root.exists():
        print(f"missing: {root}")
        return 1

    query = args.query.lower() if args.query else None
    entries = []
    for design_file in sorted(root.glob("*/DESIGN.md")):
        name = design_file.parent.name
        if query and query not in name.lower():
            continue
        entries.append((name, design_file))

    if not entries:
        print("no matching design references")
        return 0

    for name, design_file in entries:
        if args.paths:
            print(f"{name}\t{design_file}")
        else:
            print(name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
