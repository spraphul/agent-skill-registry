#!/usr/bin/env python3
"""Generate a starter JSONL eval harness from a compact spec."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

DEFAULT_CASES = [
    ("golden", "Nominal success case with permitted evidence and expected output."),
    ("edge", "Ambiguous or boundary case requiring clarification or escalation."),
    ("adversarial", "Prompt injection, poisoned context, forbidden action, or policy bypass attempt."),
    ("tool_failure", "Retriever/tool/API failure requiring graceful recovery."),
    ("privacy", "Tenant/PII/secrets boundary case that must not leak data."),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--out", default="eval_cases.jsonl", type=Path)
    ap.add_argument("--metric", action="append", default=[])
    args = ap.parse_args()
    metrics = args.metric or ["task_success", "groundedness", "policy_compliance", "cost_latency"]
    with args.out.open("w", encoding="utf-8") as f:
        for i, (kind, description) in enumerate(DEFAULT_CASES, start=1):
            row = {
                "case_id": f"{args.task}_{kind}_{i:03d}",
                "task": args.task,
                "case_type": kind,
                "description": description,
                "input": "TODO",
                "expected_behavior": ["TODO"],
                "forbidden_behavior": [],
                "metrics": metrics,
                "required_trace_assertions": [],
            }
            f.write(json.dumps(row) + "\n")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
