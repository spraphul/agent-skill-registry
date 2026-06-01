# Pareto-Front Optimization

Use when there are competing objectives such as accuracy, groundedness, cost, latency, safety, and autonomy.

Procedure:

1. Define objectives and hard constraints.
2. Choose search variables: model, prompt, retriever config, reranker, context budget, tool policy, skill route, approval threshold.
3. Generate candidates with random/Bayesian/evolutionary/LLM-guided search.
4. Evaluate each candidate on the same suite.
5. Compute non-dominated candidates.
6. Present the Pareto frontier and pick an operating point with stakeholder rationale.

Do not collapse to a single weighted score until after showing the frontier.
