# Agent Skill Registry

A public registry for reusable agent skills across multiple coding and assistant agents, starting with **Codex** and **Claude**.

The goal is to make skills discoverable, installable, and portable without forcing every ecosystem to use the exact same runtime format.

## What belongs here?

A registry entry can point to:

- A Codex skill directory containing `SKILL.md`
- A Claude-compatible skill package
- A repository that supports both
- A generic agent capability package with documented adapters

## Registry format

Registry entries live in [`registry.json`](./registry.json). Each entry declares:

- `id`: stable slug
- `name`: display name
- `description`: short summary
- `source`: Git URL or package URL
- `license`: SPDX license identifier
- `compatibility`: supported agents, currently `codex` and/or `claude`
- `entrypoints`: platform-specific files or folders
- `tags`: search/discovery terms

Schema: [`schemas/skill-entry.schema.json`](./schemas/skill-entry.schema.json)

## Example entry

```json
{
  "id": "hello-agent-skill",
  "name": "Hello Agent Skill",
  "description": "Minimal example showing a cross-agent skill registry entry.",
  "source": "https://github.com/example/hello-agent-skill",
  "license": "MIT",
  "compatibility": ["codex", "claude"],
  "entrypoints": {
    "codex": "SKILL.md",
    "claude": "skill.md"
  },
  "tags": ["example", "starter"]
}
```

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md).
