# Dataset Creation and Evaluation Harness

Use this module for train/dev/test construction, golden cases, replay evals, adversarial suites, and release gates.

## Dataset design

Choose data sources based on task:

- Human-labeled production cases
- Synthetic cases generated from explicit schemas
- Self-Instruct/Evol-Instruct-style instruction expansion
- Failure replay cases from logs/traces
- Adversarial/red-team cases
- Pairwise preference data
- Tool/retriever simulation fixtures

Every dataset needs:

- Schema
- Source/provenance
- Split policy
- Labeling rubric
- Leakage/decontamination checks
- Diversity coverage
- Hard-negative strategy
- Human QA plan

## Evaluation harness

Layer the harness:

1. Unit/component evals: prompts, retriever, tools, parsers, schemas.
2. End-to-end golden workflow cases.
3. Edge and adversarial cases.
4. Trace assertions: required tools, forbidden tools, approval gates, citations, data boundaries.
5. Cost/latency budgets.
6. Regression and canary suites.

## Output metrics

Track at minimum:

- Task success / answer quality
- Groundedness and citation support
- Retrieval recall/precision where applicable
- Tool correctness and side-effect compliance
- Safety/privacy/governance violations
- Cost, latency, and reliability
- Human review disagreement

## Deliverables

- Dataset plan
- Eval suite specification
- Judge/rubric design
- CI gate plan
- Release threshold and blocker list
