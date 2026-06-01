# DSPy Adapter

Use DSPy when the AI system can be represented as typed modules/signatures with task metrics and examples.

## Good fit

- Multi-step LLM pipelines where prompt text should be compiled/tuned instead of hand-edited.
- Prompt/program optimization with train/dev sets.
- GEPA/MIPRO-style optimization over module instructions, demos, and traces.

## Workflow

1. Define module signatures and outputs.
2. Build representative train/dev/holdout examples.
3. Define metric functions that reflect product success, not just string match.
4. Start with a simple baseline program.
5. Try BootstrapFewShot/MIPRO-style optimizers for examples/instructions.
6. Try GEPA-style reflective Pareto optimization when traces reveal compound-system failures.
7. Compare against hand-authored baseline and report cost/latency.

## Required artifacts

- DSPy signature/module plan
- Dataset split
- Metric function spec
- Optimizer choice record
- Pareto or candidate comparison report
