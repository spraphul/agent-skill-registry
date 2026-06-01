# Optimization Stack Adapter

Use this adapter when implementing search/optimization across prompts, RAG configs, models, and runtime policies.

## Candidate stack choices

- DSPy optimizers for LLM programs/signatures.
- TextGrad/ProTeGi-style textual feedback loops for prompt edits.
- Optuna/Ax/Nevergrad/Ray Tune for multi-objective hyperparameter search.
- Custom Pareto selection when candidate metrics already exist.

## Search variables

Prompt text, examples, retriever type, chunk size, top-k, reranker, context budget, model route, temperature, tool policy, skill decomposition, approval threshold, memory policy.

## Required safeguards

Train/dev/holdout split, regression suite, cost budget, safety blocker checks, changelog, rollback version.
