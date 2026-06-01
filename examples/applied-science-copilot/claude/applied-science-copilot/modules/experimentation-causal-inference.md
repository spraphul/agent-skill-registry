# Experimentation and Causal Inference

Use this module for A/B tests, online experiments, policy evaluation, rollout decisions, and causal claims.

## Experiment workflow

1. Define hypothesis and causal mechanism.
2. Define unit of randomization and analysis.
3. Choose primary metric, guardrails, and heterogeneous effects of interest.
4. Pre-register exposure, exclusions, stopping rule, and analysis plan.
5. Estimate sample size/power or use sequential/Bayesian design deliberately.
6. Add CUPED or covariate adjustment when valid.
7. Monitor guardrails without p-hacking the primary outcome.
8. Report effect size, uncertainty, practical significance, and rollout decision.

## AI-specific guardrails

- Safety/privacy incidents
- Bad tool calls or approval bypass
- Cost per successful task
- Latency/retry degradation
- Human override/rework rate
- Customer reopen/escalation rate

## Do not claim

- Causality from offline eval alone.
- Win from peeking without sequential correction.
- Product success from answer preference when workflow metrics degrade.
