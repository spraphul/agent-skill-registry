# Experiment Analysis

Use this module after offline or online experiments.

## Analysis workflow

1. Restate hypothesis, unit, exposure, randomization, primary metric, and guardrails.
2. Check data quality: sample ratio mismatch, logging gaps, duplicate exposure, bot/test traffic, missing outcomes.
3. Report primary metric effect size and uncertainty.
4. Report guardrails and safety metrics.
5. Analyze heterogeneous effects only if preplanned or clearly exploratory.
6. Compare practical significance against cost and operational risk.
7. Decide: ship, canary more, iterate, rollback, or no-op.

## AI-specific analysis

- Offline eval improved but online metric did not: inspect task mix, retrieval context, human workflow, latency, trust, and UI adoption.
- Online metric improved but safety guardrail worsened: block or restrict rollout.
- Average improved but segment regressed: decide whether segment is launch-blocking.
- Cost per successful task worsened: optimize route/cache/context or reject.

## Output

Produce an experiment readout with decision, caveats, and follow-up experiments.
