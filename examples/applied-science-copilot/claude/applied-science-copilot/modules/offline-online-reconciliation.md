# Offline/Online Metric Reconciliation

Use this module when offline evals, human review, and online product metrics disagree.

## Reconciliation matrix

- Offline up, online up: validate no guardrail regression; consider rollout.
- Offline up, online flat/down: offline suite may not match workflow, traffic mix, UX, latency, or user trust.
- Offline flat/down, online up: offline metric may miss product value; check safety and segments.
- Offline up, online safety down: block release and add must-pass cases.

## Diagnosis checklist

- Dataset representativeness
- Label/rubric mismatch
- Traffic distribution shift
- Context/retrieval mismatch between eval and prod
- Tool/API state mismatch
- UI or workflow adoption issue
- Latency/cost side effects
- Human trust and override behavior
- Segment-specific regressions

## Output

Produce a reconciliation report: disagreement type, hypotheses, evidence, next eval changes, and rollout decision.

## Utility

Use `scripts/reconcile_metrics.py` for a quick directional offline/online disagreement diagnosis. Treat it as triage, not proof.
