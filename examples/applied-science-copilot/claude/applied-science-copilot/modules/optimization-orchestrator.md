# Optimization Orchestrator

Use this module when improving prompts, skills, RAG, models, tools, agents, datasets, or product workflows.

## Diagnostic first

Classify the failure before choosing a lever:

- Product/PRD mismatch
- Missing or poor data
- Bad labels or eval mismatch
- Retrieval/context failure
- Prompt/instruction failure
- Skill routing or skill contract failure
- Tool schema/authorization/result failure
- Model capability or adaptation failure
- Latency/cost bottleneck
- Safety/governance failure

## Optimization levers

- PRD/scope revision
- Dataset creation or relabeling
- Prompt optimization: APE, OPRO, ProTeGi, TextGrad, DSPy, GEPA
- Skill optimization: triggers, preconditions, constraints, examples, output contracts, tool permissions
- RAG optimization: chunking, metadata, retrievers, rerankers, query rewriting, context packing
- Training/adaptation: SFT, LoRA/QLoRA, preference optimization, distillation, reward modeling
- Agent/runtime optimization: planning, memory, tools, approvals, retries, handoffs
- Pareto optimization: quality/cost/latency/safety frontier

## Optimization loop

1. Gather traces/evals.
2. Cluster failures.
3. Pick candidate levers.
4. Generate candidate changes.
5. Evaluate on train/dev/holdout and adversarial suites.
6. Compare against baseline and Pareto frontier.
7. Select release candidate or continue search.
8. Update artifacts, changelog, release gate, and rollback.

## Never skip

- Holdout evaluation
- Regression suite
- Cost/latency comparison
- Safety/governance blocker checks
- Versioned decision record
