#!/usr/bin/env python3
"""Compute a simple two-proportion A/B experiment readout."""
from __future__ import annotations

import argparse
import json
import math
from statistics import NormalDist


def checked_rate(success: int, n: int, label: str) -> float:
    if n <= 0:
        raise SystemExit(f"{label}-n must be > 0")
    if success < 0 or success > n:
        raise SystemExit(f"{label}-success must be between 0 and {label}-n")
    return success / n


def main() -> int:
    ap = argparse.ArgumentParser(description="Two-sided z-test and Wald CI for a binary control/treatment metric.")
    ap.add_argument("--control-success", type=int, required=True)
    ap.add_argument("--control-n", type=int, required=True)
    ap.add_argument("--treatment-success", type=int, required=True)
    ap.add_argument("--treatment-n", type=int, required=True)
    ap.add_argument("--alpha", type=float, default=0.05)
    args = ap.parse_args()
    if not 0 < args.alpha < 1:
        raise SystemExit("alpha must be between 0 and 1")

    control_rate = checked_rate(args.control_success, args.control_n, "control")
    treatment_rate = checked_rate(args.treatment_success, args.treatment_n, "treatment")
    diff = treatment_rate - control_rate
    pooled = (args.control_success + args.treatment_success) / (args.control_n + args.treatment_n)
    se_null = math.sqrt(pooled * (1 - pooled) * (1 / args.control_n + 1 / args.treatment_n))
    z = diff / se_null if se_null else 0.0
    normal = NormalDist()
    p_value = 2 * (1 - normal.cdf(abs(z)))
    zcrit = normal.inv_cdf(1 - args.alpha / 2)
    se_ci = math.sqrt(
        control_rate * (1 - control_rate) / args.control_n
        + treatment_rate * (1 - treatment_rate) / args.treatment_n
    )
    ci = [diff - zcrit * se_ci, diff + zcrit * se_ci]

    print(
        json.dumps(
            {
                "method": "two_proportion_z_test_wald_ci",
                "assumptions": [
                    "independent observations",
                    "binary outcome",
                    "fixed sample sizes",
                    "no peeking/sequential correction",
                ],
                "control_rate": control_rate,
                "treatment_rate": treatment_rate,
                "absolute_difference": diff,
                "relative_lift": diff / control_rate if control_rate else None,
                "z": z,
                "p_value": p_value,
                "confidence_interval": ci,
                "alpha": args.alpha,
                "statistically_significant": p_value < args.alpha,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
