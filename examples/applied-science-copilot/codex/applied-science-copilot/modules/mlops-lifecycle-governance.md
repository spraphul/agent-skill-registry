# MLOps Lifecycle and Governance

Use this module for production lifecycle management: model/skill/prompt/data registry, release, monitoring, retraining, audits, and retirement.

## Lifecycle stages

1. Map: use case, risk tier, stakeholders, data, intended use.
2. Measure: evals, benchmarks, fairness/safety/privacy checks, robustness.
3. Manage: controls, approvals, monitoring, incident response, rollback.
4. Govern: ownership, policies, audit logs, model/data/skill cards, compliance evidence.

## Registry artifacts

- Product charter
- Dataset card/datasheet
- Model card
- Prompt/skill card
- Tool card
- Eval harness record
- Release gate
- Monitoring spec
- Incident/postmortem record

## Maintenance loop

- Monitor drift, quality, cost, latency, safety, and business outcomes.
- Refresh evals with production failures.
- Trigger retraining or artifact updates only after diagnosis.
- Version every artifact and keep rollback path.
- Retire stale models/prompts/skills/tools.
