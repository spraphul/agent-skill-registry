#!/usr/bin/env python3
"""Generate a starter applied-AI PRD markdown."""
from __future__ import annotations
import argparse
from pathlib import Path

SECTIONS = [
    "Problem", "Users and stakeholders", "Current workflow and baseline", "Jobs to improve",
    "Scope and non-goals", "Autonomy and approval boundaries", "Data/context/tool requirements",
    "Success metrics", "Guardrails and unacceptable failures", "Evaluation plan", "Launch plan", "Open questions",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", type=Path, default=Path("prd.md"))
    args = ap.parse_args()
    lines = [f"# {args.title}", ""]
    for section in SECTIONS:
        lines += [f"## {section}", "TODO", ""]
    args.out.write_text("\n".join(lines))
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
