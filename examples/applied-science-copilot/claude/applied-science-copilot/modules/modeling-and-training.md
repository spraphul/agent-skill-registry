# Modeling and Training

Use this module when selecting or training models, including classical ML, deep learning, retrieval models, rerankers, LLM adaptation, and multimodal models.

## Decision order

1. Confirm the failure requires modeling/training rather than PRD, data, retrieval, prompt, tool, or UX change.
2. Choose model family based on task structure and constraints.
3. Define training data, objective, validation set, and baseline.
4. Select adaptation method: classical ML, embedding/reranker training, SFT, LoRA/QLoRA, preference optimization, distillation, reward model, RL, or prompt-only.
5. Define offline eval, stress eval, and online experiment plan.
6. Track reproducibility: data version, code version, hyperparameters, model ID, random seeds, compute, and environment.

## Method selection

- Classical ML: tabular/log/ranking problems with structured labels and explainability needs.
- Embedding/reranker training: retrieval failures and domain-specific relevance.
- SFT/LoRA/QLoRA: behavior requires learned transformations or domain style from examples.
- DPO/IPO/KTO/ORPO/GRPO: preference data exists and behavior quality matters beyond supervised targets.
- Distillation: cost/latency or deployment constraints require smaller models.
- RL/tool-use training: only when traces and reward signals are mature.

## Required outputs

- Model/training decision record
- Dataset and objective spec
- Baseline comparison
- Training/eval plan
- Reproducibility record
- Deployment and rollback plan
