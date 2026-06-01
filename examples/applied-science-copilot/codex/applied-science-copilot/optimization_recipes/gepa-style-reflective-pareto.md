# GEPA-Style Reflective Pareto Optimization

Use when a compound LLM system has traces and a measurable eval suite.

Loop:

1. Sample task trajectories with inputs, outputs, tool calls, errors, and judge feedback.
2. Reflect on failures in natural language.
3. Propose prompt/skill/program mutations targeted to observed failures.
4. Evaluate candidates per instance and globally.
5. Maintain a Pareto frontier of candidates that cover different examples/objectives.
6. Merge complementary lessons only after regression checks.
7. Select deployment candidate by release constraints, not raw score alone.

Track quality, cost, latency, safety, groundedness, and maintainability.
