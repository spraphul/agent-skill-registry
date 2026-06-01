#!/usr/bin/env python3
"""Validate registry structure and platform entrypoint directories."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SUPPORTED_AGENTS = {"codex", "claude"}


def load_registry(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f"failed to read {path}: {exc}") from exc


def validate(registry_path: Path) -> list[str]:
    root = registry_path.parent
    registry = load_registry(registry_path)
    errors: list[str] = []
    seen_ids: set[str] = set()

    if not isinstance(registry.get("skills"), list):
        return ["registry.skills must be a list"]

    for index, skill in enumerate(registry["skills"]):
        prefix = f"skills[{index}]"
        skill_id = skill.get("id")
        if not skill_id:
            errors.append(f"{prefix}: missing id")
            continue
        if skill_id in seen_ids:
            errors.append(f"{prefix}: duplicate id {skill_id!r}")
        seen_ids.add(skill_id)

        compatibility = set(skill.get("compatibility", []))
        entrypoints = skill.get("entrypoints", {})
        unknown_agents = compatibility - SUPPORTED_AGENTS
        if unknown_agents:
            errors.append(f"{skill_id}: unsupported agents {sorted(unknown_agents)}")

        source = skill.get("source")
        if not source:
            errors.append(f"{skill_id}: missing source")
            continue
        source_path = (root / source).resolve() if not str(source).startswith(("http://", "https://", "git@")) else None
        if source_path and not source_path.exists():
            errors.append(f"{skill_id}: source path does not exist: {source}")
            continue

        for agent in compatibility:
            rel = entrypoints.get(agent)
            if not rel:
                errors.append(f"{skill_id}: missing entrypoints.{agent}")
                continue
            if source_path is None:
                continue
            entrypoint = source_path / rel
            if not entrypoint.is_dir():
                errors.append(f"{skill_id}: entrypoint for {agent} is not a directory: {entrypoint}")
                continue
            if not (entrypoint / "SKILL.md").is_file():
                errors.append(f"{skill_id}: entrypoint for {agent} lacks SKILL.md: {entrypoint}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="registry.json", type=Path)
    args = parser.parse_args()

    errors = validate(args.registry)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"ok: {args.registry}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
