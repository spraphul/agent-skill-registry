#!/usr/bin/env python3
"""Profile a CSV for basic data quality issues without external dependencies."""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


def infer_type(values: list[str]) -> str:
    sample = [v for v in values if v != ""][:100]
    if not sample:
        return "empty"

    def all_cast(fn) -> bool:
        try:
            for value in sample:
                fn(value)
            return True
        except Exception:
            return False

    if all_cast(int):
        return "integer"
    if all_cast(float):
        return "number"
    lowered = {v.lower() for v in sample}
    if lowered <= {"true", "false", "yes", "no", "0", "1"}:
        return "boolean_like"
    return "string"


def main() -> int:
    ap = argparse.ArgumentParser(description="Profile CSV missingness, duplicates, cardinality, primitive types, and top values.")
    ap.add_argument("csv_path", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    with args.csv_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fields = list(reader.fieldnames or [])

    duplicate_count = len(rows) - len({tuple((field, row.get(field, "")) for field in fields) for row in rows})
    columns = []
    for field in fields:
        values = [(row.get(field) or "").strip() for row in rows]
        non_empty = [value for value in values if value]
        counter = Counter(non_empty)
        missing = len(values) - len(non_empty)
        columns.append(
            {
                "name": field,
                "inferred_type": infer_type(values),
                "count": len(values),
                "missing": missing,
                "missing_rate": missing / len(values) if values else 0,
                "unique": len(set(non_empty)),
                "unique_rate": len(set(non_empty)) / len(non_empty) if non_empty else 0,
                "top_values": counter.most_common(5),
            }
        )

    report = {
        "csv_path": str(args.csv_path),
        "rows": len(rows),
        "columns": len(fields),
        "duplicate_rows": duplicate_count,
        "column_profiles": columns,
    }
    output = json.dumps(report, indent=2)
    if args.out:
        args.out.write_text(output + "\n")
        print(f"wrote {args.out}")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
