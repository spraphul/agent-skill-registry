#!/usr/bin/env python3
"""Generate a starter project plan JSON."""
from __future__ import annotations
import argparse
import json
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--out", type=Path, default=Path("project_plan.json"))
    args = ap.parse_args()
    plan = {
        "name": args.name,
        "workstreams": ["product", "data", "model_or_rag", "evals", "platform", "observability", "governance"],
        "milestones": ["M0 discovery", "M1 baseline", "M2 eval harness", "M3 prototype", "M4 canary", "M5 launch"],
        "risks": [],
        "acceptance_criteria": [],
    }
    args.out.write_text(json.dumps(plan, indent=2) + "\n")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
