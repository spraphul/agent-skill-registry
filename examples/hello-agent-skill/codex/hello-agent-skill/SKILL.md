---
name: hello-agent-skill
description: Minimal Codex-compatible smoke-test skill. Use when validating registry discovery, Codex skill packaging, or a basic agent skill installation path.
---

# Hello Agent Skill

Use this skill to verify that a Codex-compatible skill directory can be discovered and loaded from the registry.

## Instructions

1. Reply with a short greeting.
2. State that this is a Codex registry smoke test.
3. If asked to validate bundled resources, mention that this scaffold includes `scripts/`, `references/`, `assets/`, and `agents/openai.yaml`.

## Optional resources

- For a tiny reference note, read `references/usage.md`.
- For deterministic output, run `python scripts/say_hello.py`.
