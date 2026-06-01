#!/usr/bin/env python3
"""Cluster eval failures by tags and rough failure reason."""
from __future__ import annotations
import argparse, collections, json
from pathlib import Path

def key(row):
    tags = row.get("failure_tags") or row.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    reason = row.get("failure_reason") or row.get("error") or "unspecified"
    return tuple(sorted(tags)) or (reason[:80],)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", type=Path)
    args = ap.parse_args()
    clusters = collections.defaultdict(list)
    for line in args.jsonl.read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        clusters[key(row)].append(row.get("case_id", row.get("id", "unknown")))
    for k, ids in sorted(clusters.items(), key=lambda item: len(item[1]), reverse=True):
        print(json.dumps({"cluster": list(k), "count": len(ids), "case_ids": ids[:20]}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
