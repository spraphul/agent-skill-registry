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

Run commands from the repository root, or pass an explicit registry file:

```bash
agent-skill install --registry /path/to/registry.json hello-agent-skill --agent codex
```

## Install the CLI

From the repository root:

```bash
pipx install .
```

For development inside a clone, use editable install:

```bash
python3 -m pip install -e .
```

After installation, use the `agent-skill` command. If `pip` warns that the script directory is not on `PATH`, either add that directory to `PATH` or use `pipx install .`.

## Defaults

| Agent | User install root | Project install root |
| --- | --- | --- |
| Codex | `~/.agents/skills` | `.agents/skills` |
| Claude | `~/.claude/skills` | `.claude/skills` |

## Install one skill

```bash
agent-skill install hello-agent-skill --agent codex
agent-skill install hello-agent-skill --agent claude
```

## Install for both agents

```bash
agent-skill install hello-agent-skill --agent both
```

## Install multiple skills

```bash
agent-skill install hello-agent-skill another-skill --agent codex
```

## Install every compatible skill

```bash
agent-skill install --all --agent codex
agent-skill install --all --agent both
```

## Install into a project

```bash
agent-skill install hello-agent-skill --agent codex --scope project --project-dir /path/to/repo
agent-skill install hello-agent-skill --agent claude --scope project --project-dir /path/to/repo
```

## Preview or overwrite

```bash
agent-skill install hello-agent-skill --agent both --dry-run
agent-skill install hello-agent-skill --agent both --force
```

## Custom destination

Use `--dest` to copy into a custom skills root. This is useful for tests and non-standard agent setups.

```bash
agent-skill install hello-agent-skill --agent codex --dest /tmp/codex-skills
```

When `--dest` is used with multiple agents, installs are namespaced by agent to avoid collisions:

```text
/tmp/agent-skills/
├── codex/hello-agent-skill/
└── claude/hello-agent-skill/
```

## Validate the registry

```bash
agent-skill validate
```

Validation checks that every local registry entrypoint exists and contains `SKILL.md`.

## Security note

Skills can include scripts and agent instructions. Review `SKILL.md`, frontmatter, scripts, and bundled resources before installing third-party skills.
