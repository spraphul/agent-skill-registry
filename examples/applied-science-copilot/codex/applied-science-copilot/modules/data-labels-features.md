# Data, Labels, and Features

Use this module when creating or auditing datasets, labels, features, logs, or context sources.

## Data workflow

1. Define prediction/decision unit and grain.
2. Inventory data sources and production availability.
3. Define schema, provenance, freshness, permissions, retention, and leakage risks.
4. Choose labeling strategy: expert labels, user feedback, weak labels, synthetic labels, pairwise preferences, replay labels.
5. Define splits by time/entity/domain to avoid leakage.
6. Add data quality checks and label QA.
7. Define dataset card/datasheet.

## Labeling rubric

A strong rubric includes positive/negative definitions, edge cases, abstain labels, examples, adjudication policy, inter-annotator checks, and escalation path.

## Feature/context checks

- Available at inference time?
- Stable over rollout horizon?
- Permissioned and tenant-safe?
- Decontaminated from eval/test labels?
- Observable in traces?
