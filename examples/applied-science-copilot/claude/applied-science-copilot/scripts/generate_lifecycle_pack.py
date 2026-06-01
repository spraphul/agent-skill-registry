#!/usr/bin/env python3
"""Generate a starter applied-science artifact pack for a product."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

MD_SECTIONS = {
    "prd.md": ["Problem", "Users", "Workflow", "Jobs to improve", "Non-goals", "Metrics", "Guardrails", "Launch plan"],
    "dataset_card.md": ["Motivation", "Composition", "Collection", "Labeling", "Splits", "Quality checks", "Risks", "Maintenance"],
    "model_card.md": ["Model details", "Intended use", "Data", "Evaluation", "Performance", "Risks", "Operational constraints"],
    "risk_review.md": ["Map", "Measure", "Manage", "Govern", "Blockers", "Approvals"],
    "experiment_readout.md": ["Hypothesis", "Design", "Primary metric", "Guardrails", "Result", "Decision", "Caveats"],
    "offline_online_reconciliation.md": ["Observed disagreement", "Hypotheses", "Evidence", "Eval changes", "Rollout decision"],
}

JSON_ARTIFACTS = {
    "project_plan.json": {
        "workstreams": ["product", "data", "model_or_rag", "evals", "platform", "observability", "governance"],
        "milestones": ["M0 discovery", "M1 baseline", "M2 eval harness", "M3 prototype", "M4 canary", "M5 launch"],
        "risks": [],
        "acceptance_criteria": []
    },
    "monitoring_spec.json": {
        "signals": ["quality", "groundedness", "tool_success", "cost", "latency", "safety", "user_outcome"],
        "dashboards": [],
        "alerts": [],
        "retention": "TODO",
        "redaction": "TODO"
    },
    "release_gate.json": {
        "must_pass": ["privacy", "approval_compliance", "no_forbidden_tool_calls"],
        "thresholds": [],
        "rollback": "TODO",
        "decision": "pending"
    }
}


def write_md(path: Path, title: str, sections: list[str]) -> None:
    lines = [f"# {title}", ""]
    for section in sections:
        lines += [f"## {section}", "TODO", ""]
    path.write_text("\n".join(lines))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--out-dir", type=Path, default=Path("applied_science_artifacts"))
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for filename, sections in MD_SECTIONS.items():
        title = f"{args.name}: {filename.removesuffix('.md').replace('_', ' ').title()}"
        write_md(args.out_dir / filename, title, sections)
    for filename, payload in JSON_ARTIFACTS.items():
        body = {"name": args.name, **payload}
        (args.out_dir / filename).write_text(json.dumps(body, indent=2) + "\n")
    print(f"wrote artifact pack to {args.out_dir}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
