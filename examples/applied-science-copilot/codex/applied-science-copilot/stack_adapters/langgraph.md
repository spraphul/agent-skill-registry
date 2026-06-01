# LangGraph Adapter

Use LangGraph when the system needs durable, inspectable agent orchestration: state, branching, persistence, human-in-the-loop, retries, and replay.

## Good fit

- Bounded agents with explicit state machines.
- Workflows with approvals, handoffs, retries, or long-running execution.
- Systems requiring traceability and replay.

## Workflow

1. Define state schema.
2. Define nodes for planner, tools, validators, approvals, and finalizers.
3. Define edges and stop conditions.
4. Add persistence/checkpointing where replay or recovery matters.
5. Add human approval nodes for high-risk transitions.
6. Emit traces with node, input, output, tool calls, and policy decisions.

## Required artifacts

- State machine diagram/spec
- Node/edge table
- Tool and permission map
- Approval policy
- Eval trace assertions
