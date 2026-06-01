# Dataset Cards, Datasheets, and Data Quality

Use this module when documenting or auditing datasets. Anchor the work in Datasheets for Datasets and data-centric AI practice.

## Dataset card sections

- Motivation: why the dataset exists and what decisions it supports.
- Composition: records, fields, labels, demographics/segments, sensitive attributes, missingness.
- Collection: source systems, time window, consent/permissions, sampling, instrumentation.
- Labeling: rubric, annotators, adjudication, quality checks, inter-annotator agreement.
- Preprocessing: filters, deduplication, transformations, normalization, redaction.
- Splits: train/dev/test/holdout policy, leakage prevention, temporal/entity/domain splits.
- Intended use: supported tasks, unsupported uses, known limitations.
- Risks: bias, privacy, security, distribution shift, contamination, representativeness.
- Maintenance: owner, refresh cadence, deprecation, monitoring signals.

## Data quality checks

- Schema validity
- Null/missingness profile
- Duplicate/entity leakage checks
- Label distribution and class imbalance
- Segment coverage
- Temporal coverage
- Outlier and impossible-value checks
- Train/test contamination checks
- PII/secrets scan
- Provenance and license checks

## Output

Produce a dataset card, quality checklist, and remediation plan before training or eval use.
