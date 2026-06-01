# Contributing

Contributions are welcome. This registry should stay useful, searchable, and agent-neutral.

## Add a skill

1. Add or update an entry in `registry.json`.
2. Validate the entry against `schemas/skill-entry.schema.json`.
3. Confirm the linked repository includes clear install/use instructions.
4. Prefer permissive/open licenses for public reuse.

## Entry guidelines

- Use stable lowercase slugs for `id`.
- Keep descriptions concise and concrete.
- Declare compatibility honestly: `codex`, `claude`, or both.
- Include platform-specific entrypoints when possible.
- Add tags that describe capabilities, not marketing claims.

## Quality bar

A listed skill should include enough documentation for another agent/user to install and use it without reading the author's private context.
