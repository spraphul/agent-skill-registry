# Agent Skill Registry

A public registry for reusable agent skills across multiple coding and assistant agents, starting with **Codex** and **Claude**.

The goal is to make skills discoverable, installable, and portable without forcing every ecosystem to use the exact same runtime format.

## What belongs here?

A registry entry can point to:

- A Codex skill directory containing `SKILL.md`
- A Claude-compatible skill package
- A repository that supports both
- A generic agent capability package with documented adapters

## Example scaffold layout

The example skill keeps platform packages separate so consumers can copy or install the expected directory for their agent:

```text
examples/hello-agent-skill/
├── codex/
│   └── hello-agent-skill/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── assets/
│       ├── references/
│       └── scripts/
└── claude/
    └── hello-agent-skill/
        ├── SKILL.md
        ├── examples.md
        ├── reference.md
        ├── scripts/
        └── templates/
```

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
  "source": "./examples/hello-agent-skill",
  "license": "MIT",
  "compatibility": ["codex", "claude"],
  "entrypoints": {
    "codex": "codex/hello-agent-skill",
    "claude": "claude/hello-agent-skill"
  },
  "tags": ["example", "starter"]
}
```

## Install skills

Use the installer to copy one or more registry skills into Codex or Claude skill directories:

```bash
python3 scripts/install_skill.py hello-agent-skill --agent codex
python3 scripts/install_skill.py hello-agent-skill --agent claude
python3 scripts/install_skill.py hello-agent-skill --agent both
```

See [`docs/INSTALL.md`](./docs/INSTALL.md) for user, project, dry-run, force, and bulk-install options.

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md).
