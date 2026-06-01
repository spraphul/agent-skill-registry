#!/usr/bin/env python3
"""Generate an offline/online metric reconciliation diagnosis."""
from __future__ import annotations

import argparse
import json


def direction(delta: float, threshold: float) -> str:
    if delta > threshold:
        return "up"
    if delta < -threshold:
        return "down"
    return "flat"


def main() -> int:
    ap = argparse.ArgumentParser(description="Triage disagreement between offline eval deltas and online metric deltas.")
    ap.add_argument("--offline-delta", type=float, required=True)
    ap.add_argument("--online-delta", type=float, required=True)
    ap.add_argument("--threshold", type=float, default=0.0)
    args = ap.parse_args()
    if args.threshold < 0:
        raise SystemExit("threshold must be >= 0")

    offline = direction(args.offline_delta, args.threshold)
    online = direction(args.online_delta, args.threshold)
    diagnosis = {
        ("up", "up"): "consistent_positive",
        ("up", "flat"): "offline_improved_online_flat",
        ("up", "down"): "offline_improved_online_regressed",
        ("flat", "up"): "offline_flat_online_improved",
        ("flat", "down"): "offline_flat_online_regressed",
        ("down", "up"): "offline_regressed_online_improved",
        ("down", "flat"): "offline_regressed_online_flat",
        ("down", "down"): "consistent_negative",
    }.get((offline, online), "flat_or_inconclusive")
    hypotheses = {
        "offline_improved_online_flat": ["offline suite not representative", "UX/adoption bottleneck", "latency/cost side effects", "traffic mix mismatch"],
        "offline_improved_online_regressed": ["guardrail regression", "workflow metric mismatch", "segment harm", "production context/tool mismatch"],
        "offline_flat_online_improved": ["offline metric misses product value", "human workflow improved", "evaluate new metric"],
        "offline_flat_online_regressed": ["online guardrail/latency/cost regression", "offline eval blind spot", "segment or traffic mismatch"],
        "offline_regressed_online_improved": ["offline eval misaligned", "check safety before trusting online lift"],
        "offline_regressed_online_flat": ["offline regression may not affect users", "inspect task mix and guardrails before rollout"],
        "consistent_positive": ["verify guardrails and segments", "consider rollout"],
        "consistent_negative": ["rollback or iterate"],
    }.get(diagnosis, ["collect more evidence"])
    print(
        json.dumps(
            {
                "offline_delta": args.offline_delta,
                "online_delta": args.online_delta,
                "threshold": args.threshold,
                "offline_direction": offline,
                "online_direction": online,
                "diagnosis": diagnosis,
                "hypotheses": hypotheses,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
