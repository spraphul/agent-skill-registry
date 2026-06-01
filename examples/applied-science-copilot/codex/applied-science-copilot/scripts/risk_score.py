#!/usr/bin/env python3
"""Score AI system risk with deterministic dimensions."""
from __future__ import annotations

import argparse
import json

DIMENSIONS = [
    "data_sensitivity",
    "decision_impact",
    "autonomy",
    "tool_side_effects",
    "external_exposure",
    "irreversibility",
]


def tier(score: float, blockers: list[str]) -> str:
    if blockers or score >= 4.0:
        return "high"
    if score >= 2.5:
        return "medium"
    return "low"


def main() -> int:
    ap = argparse.ArgumentParser(description="First-pass AI launch risk scoring. Each dimension is 1 low to 5 high.")
    for dim in DIMENSIONS:
        ap.add_argument(f"--{dim.replace('_', '-')}", type=int, required=True, help="1 low to 5 high")
    args = ap.parse_args()
    values = {dim: getattr(args, dim) for dim in DIMENSIONS}
    for dim, value in values.items():
        if value < 1 or value > 5:
            raise SystemExit(f"{dim} must be between 1 and 5")

    score = sum(values.values()) / len(values)
    blockers = []
    if values["data_sensitivity"] >= 4 and values["external_exposure"] >= 4:
        blockers.append("high sensitive-data exposure")
    if values["autonomy"] >= 4 and values["tool_side_effects"] >= 4:
        blockers.append("high-autonomy side-effecting tools")
    if values["decision_impact"] >= 4 and values["irreversibility"] >= 4:
        blockers.append("high-impact hard-to-reverse decisions")

    print(
        json.dumps(
            {
                "dimensions": values,
                "scale": "1=low risk contribution, 5=high risk contribution",
                "mean_score": score,
                "risk_tier": tier(score, blockers),
                "launch_blockers": blockers,
                "required_next_step": "human policy/security review" if blockers else "document mitigations and evidence gaps",
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
