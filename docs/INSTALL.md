# Installing Skills

This registry installs platform-specific skill directories from a registry entry.

Each registry entry can expose one or more agent entrypoints:

```json
"entrypoints": {
  "codex": "codex/hello-agent-skill",
  "claude": "claude/hello-agent-skill"
}
```

The installer copies the selected entrypoint directory into the target agent's skills directory.

## Defaults

| Agent | User install root | Project install root |
| --- | --- | --- |
| Codex | `~/.agents/skills` | `.agents/skills` |
| Claude | `~/.claude/skills` | `.claude/skills` |

## Install one skill

```bash
python3 scripts/install_skill.py hello-agent-skill --agent codex
python3 scripts/install_skill.py hello-agent-skill --agent claude
```

## Install for both agents

```bash
python3 scripts/install_skill.py hello-agent-skill --agent both
```

## Install multiple skills

```bash
python3 scripts/install_skill.py hello-agent-skill another-skill --agent codex
```

## Install every compatible skill

```bash
python3 scripts/install_skill.py --all --agent codex
python3 scripts/install_skill.py --all --agent both
```

## Install into a project

```bash
python3 scripts/install_skill.py hello-agent-skill --agent codex --scope project --project-dir /path/to/repo
python3 scripts/install_skill.py hello-agent-skill --agent claude --scope project --project-dir /path/to/repo
```

## Preview or overwrite

```bash
python3 scripts/install_skill.py hello-agent-skill --agent both --dry-run
python3 scripts/install_skill.py hello-agent-skill --agent both --force
```

## Custom destination

Use `--dest` to copy into a custom skills root. This is useful for tests and non-standard agent setups.

```bash
python3 scripts/install_skill.py hello-agent-skill --agent codex --dest /tmp/codex-skills
```

When `--dest` is used with multiple agents, installs are namespaced by agent to avoid collisions:

```text
/tmp/agent-skills/
├── codex/hello-agent-skill/
└── claude/hello-agent-skill/
```

## Validate the registry

```bash
python3 scripts/validate_registry.py
```

Validation checks that every local registry entrypoint exists and contains `SKILL.md`.

## Security note

Skills can include scripts and agent instructions. Review `SKILL.md`, frontmatter, scripts, and bundled resources before installing third-party skills.
