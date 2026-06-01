# Seed References: Methods and Stacks

Use this as a starting map, not as frozen truth. For implementation decisions, fetch current primary docs/papers before selecting a method.

## Prompt and compound-system optimization

- GEPA / Genetic-Pareto reflective prompt evolution: https://arxiv.org/abs/2507.19457 and DSPy docs https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/optimizers/GEPA/overview.md
- TextGrad / automatic differentiation via text: https://arxiv.org/abs/2406.07496 and https://textgrad.com/
- OPRO / Optimization by PROmpting: https://arxiv.org/abs/2309.03409
- APE / Automatic Prompt Engineer: https://arxiv.org/abs/2211.01910
- ProTeGi / prompt optimization with textual gradients: https://arxiv.org/abs/2305.03495 and https://aclanthology.org/2023.emnlp-main.494/
- PromptBreeder / self-referential prompt evolution: https://arxiv.org/abs/2309.16797
- DSPy optimizers and teleprompters: research current DSPy docs before use.

## Dataset creation and training/adaptation

- Self-Instruct: https://arxiv.org/abs/2212.10560
- Evol-Instruct / WizardLM: https://arxiv.org/abs/2304.12244
- DPO: https://arxiv.org/abs/2305.18290
- IPO: verify current references before use.
- KTO: verify current references before use.
- ORPO: verify current references before use.
- GRPO: verify current references before use.
- LoRA/QLoRA/SFT/distillation/reranker training: choose only after diagnosing that non-training levers are insufficient.

## Multi-objective and Pareto optimization

- Optuna multi-objective studies and Pareto front trials: https://optuna.readthedocs.io/
- Ax multi-objective optimization and Pareto frontier recipes: https://ax.dev/docs/recipes/multi-objective-optimization/
- Nevergrad/Ray Tune/NSGA-style evolutionary search: verify current docs and match to budget.

## Evaluation, observability, and RAG stacks

- RAGAS metrics: https://docs.ragas.io/
- DeepEval: https://deepeval.com/
- Arize Phoenix: https://arize.com/docs/phoenix/
- LangSmith: https://docs.smith.langchain.com/
- Langfuse: https://langfuse.com/docs
- Braintrust: https://www.braintrust.dev/docs
- OpenTelemetry/OpenInference tracing: verify current instrumentation docs for chosen stack.

## Use policy

1. Prefer primary papers/docs over blogs.
2. Re-check docs for active frameworks before implementation.
3. Convert references into task-specific experiments, not blind recommendations.
4. Track exact versions, commits, model IDs, and eval datasets in every optimization record.
