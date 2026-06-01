# Prior Art and Method Map

Use this module when the task requires method selection, SOTA awareness, or research-backed design.

## Workflow

1. Restate the applied task and decision to be made.
2. Search current primary sources when methods/tools may have changed.
3. Build a method map with: method, best use case, required data, optimization signal, compute/cost profile, failure modes, maturity, and implementation path.
4. Convert the method map into a decision record and experiment plan.

## Initial method families to consider

For seed URLs and method anchors, read `../references/seed-methods-and-stacks.md` and then verify current primary sources.


| Family | Methods / references to check | Use when | Watch-outs |
| --- | --- | --- | --- |
| Prompt candidate generation | APE, OPRO, meta-prompting | Need quick prompt alternatives over a labeled dev set | Can overfit small evals; needs holdout and regression |
| Textual-gradient optimization | ProTeGi, TextGrad | Need natural-language feedback to guide edits to prompts/components | Feedback quality dominates; validate on held-out cases |
| Evolutionary prompt optimization | PromptBreeder, GEPA | Need iterative prompt/program improvement from traces | Track budget, diversity, and regressions |
| Pareto reflective optimization | GEPA-style Pareto frontier, multi-objective HPO | Need quality/cost/latency/safety tradeoff search | Avoid scalarizing too early; report frontier not just winner |
| DSPy-style compilation | BootstrapFewShot, COPRO, MIPRO/MIPROv2, GEPA | LLM pipeline has signatures/modules and task metrics | Requires representative train/dev examples |
| RAG optimization | chunking, metadata, hybrid search, rerankers, query rewriting, context packing | Failures are retrieval/context groundedness issues | Need retrieval-level labels or trace assertions |
| Preference optimization | RLHF/PPO, DPO, IPO, KTO, ORPO, GRPO, SimPO | Need behavior/style alignment from preference data | Expensive; ensure problem is not context/prompt/tool issue first |
| Dataset evolution | Self-Instruct, Evol-Instruct, rejection sampling, distillation | Need labeled/synthetic data expansion | Must include filtering, decontamination, diversity, and human QA |
| Multi-objective search | Optuna, Ax, NSGA-II/III, Bayesian optimization, bandits | Need tuneable configs across multiple metrics | Need constraints and budget-aware stopping |

## Deliverables

- Prior-art map
- Method shortlist
- Decision record
- Minimal experiment plan
- Risks and evidence gaps

## Applied science lifecycle references

When the task is not primarily optimization, map it to product discovery, data/labels/features, modeling/training, experimentation, lifecycle governance, and operations before selecting algorithms.
