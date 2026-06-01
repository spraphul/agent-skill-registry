# OpenAI and Anthropic Adapter

Use this adapter when building against frontier model APIs directly.

## Workflow

1. Verify current official docs for model capabilities, tool-use syntax, structured outputs, batching, files, evals, tracing, and safety controls.
2. Define model routes by task risk, latency, context size, modality, and cost.
3. Use structured outputs for downstream evals and trace assertions where possible.
4. Keep tool schemas narrow and separate draft from commit actions.
5. Track prompt/model/version in every run.

## Required artifacts

- Model routing table
- Tool schema and risk tier
- Structured output schema
- Eval harness
- Cost/latency budget
- Fallback and rollback policy
