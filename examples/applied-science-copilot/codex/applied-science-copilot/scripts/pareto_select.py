#!/usr/bin/env python3
"""Select non-dominated candidates from JSONL metrics."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def dominates(a, b, maximize, minimize):
    better_or_equal = True
    strictly_better = False
    for m in maximize:
        if a[m] < b[m]: better_or_equal = False
        if a[m] > b[m]: strictly_better = True
    for m in minimize:
        if a[m] > b[m]: better_or_equal = False
        if a[m] < b[m]: strictly_better = True
    return better_or_equal and strictly_better

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", type=Path)
    ap.add_argument("--maximize", action="append", default=[])
    ap.add_argument("--minimize", action="append", default=[])
    args = ap.parse_args()
    rows = [json.loads(line) for line in args.jsonl.read_text().splitlines() if line.strip()]
    if not args.maximize and not args.minimize:
        raise SystemExit("provide at least one --maximize or --minimize metric")
    frontier = []
    for i, row in enumerate(rows):
        if not any(dominates(other, row, args.maximize, args.minimize) for j, other in enumerate(rows) if i != j):
            frontier.append(row)
    for row in frontier:
        print(json.dumps(row))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
