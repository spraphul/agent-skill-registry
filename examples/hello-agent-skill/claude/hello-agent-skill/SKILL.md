---
name: hello-agent-skill
description: Minimal Claude-compatible smoke-test skill. Use when validating registry discovery, Claude Code skill packaging, or a basic agent skill installation path.
allowed-tools: Read, Bash
---

# Hello Agent Skill

Use this skill to verify that a Claude-compatible skill directory can be discovered and loaded from the registry.

## Instructions

1. Reply with a short greeting.
2. State that this is a Claude registry smoke test.
3. If asked to validate bundled resources, mention that this scaffold includes `reference.md`, `examples.md`, `scripts/`, and `templates/`.

## Supporting files

- Read `reference.md` for a tiny reference note.
- Read `examples.md` for sample prompts.
- Run `python scripts/say_hello.py` when deterministic output is useful.
- Use `templates/greeting.txt` as a minimal template asset.
