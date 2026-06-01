# Model Cards and Model Reporting

Use this module when documenting a trained model, model route, prompt/model artifact, or release candidate. Anchor the artifact in Model Cards for Model Reporting.

## Model card sections

- Model details: owner, version, architecture/provider, date, license, intended deployment.
- Intended use: tasks, users, autonomy level, domains, non-goals.
- Training/adaptation data: sources, filters, limitations, sensitive data treatment.
- Evaluation data: suites, splits, metrics, segments, adversarial/stress tests.
- Performance: aggregate and segment results, uncertainty, cost, latency.
- Ethical/safety considerations: privacy, fairness, misuse, harmful failure modes.
- Operational constraints: required context, tools, permissions, monitoring, fallback.
- Caveats and recommendations: when not to use, human oversight, rollback path.

## Applied AI extension

For LLM/RAG/agent systems, also document prompt version, retrieval/index version, tool permissions, skill versions, eval harness version, and release gate result.
