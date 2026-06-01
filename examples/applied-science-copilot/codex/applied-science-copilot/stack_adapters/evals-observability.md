# Evals and Observability Adapter

Use this adapter when choosing or wiring eval/monitoring stacks such as RAGAS, DeepEval, Braintrust, LangSmith, Phoenix, Langfuse, or OpenTelemetry/OpenInference.

## Stack selection

- RAGAS/DeepEval: fast local or CI-style metric suites for RAG and LLM outputs.
- Braintrust: experiment tracking, datasets, scorers, and eval management.
- LangSmith: LangChain/LangGraph tracing, datasets, and evals.
- Phoenix/Arize: OpenInference tracing, span analysis, evals, and observability.
- Langfuse: tracing, prompt management, datasets, evals, and production observability.
- OpenTelemetry/OpenInference: portable trace conventions when avoiding vendor lock-in.

## Minimum telemetry

Capture task id, user/tenant-safe metadata, model, prompt/skill version, retrieval query/chunks/scores, tool calls, approvals, output, costs, latency, failure tags, and human labels.

## Required artifacts

- Eval dataset definition
- Scorer/rubric definitions
- Trace schema
- Dashboard dimensions
- Alert thresholds
- Release gate mapping
