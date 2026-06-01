#!/usr/bin/env python3
"""Agent Skill Registry command line interface."""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

SUPPORTED_AGENTS = ("codex", "claude")
DEFAULT_USER_DIRS = {
    "codex": Path.home() / ".agents" / "skills",
    "claude": Path.home() / ".claude" / "skills",
}
DEFAULT_PROJECT_DIRS = {
    "codex": Path(".agents") / "skills",
    "claude": Path(".claude") / "skills",
}


def load_registry(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f"failed to read {path}: {exc}") from exc


def registry_by_id(registry: dict) -> dict[str, dict]:
    return {skill["id"]: skill for skill in registry.get("skills", []) if "id" in skill}


def is_remote_source(source: str) -> bool:
    return source.startswith(("http://", "https://", "git@"))


def validate_registry(registry_path: Path) -> list[str]:
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
        unknown_agents = compatibility - set(SUPPORTED_AGENTS)
        if unknown_agents:
            errors.append(f"{skill_id}: unsupported agents {sorted(unknown_agents)}")

        source = skill.get("source")
        if not source:
            errors.append(f"{skill_id}: missing source")
            continue
        source_path = (root / source).resolve() if not is_remote_source(str(source)) else None
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


def destination_root(agent: str, scope: str, project_dir: Path | None, dest: Path | None) -> Path:
    if dest is not None:
        return dest.expanduser()
    if scope == "user":
        return DEFAULT_USER_DIRS[agent]
    base = project_dir.expanduser() if project_dir else Path.cwd()
    return base / DEFAULT_PROJECT_DIRS[agent]


def copy_skill(src: Path, dst: Path, force: bool, dry_run: bool) -> None:
    if not src.is_dir():
        raise SystemExit(f"source entrypoint is not a directory: {src}")
    if not (src / "SKILL.md").is_file():
        raise SystemExit(f"source entrypoint lacks SKILL.md: {src}")
    if dst.exists() and not force:
        raise SystemExit(f"destination exists, use --force to replace: {dst}")
    print(f"install {src} -> {dst}")
    if dry_run:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def install_skill(
    registry_path: Path,
    skill: dict,
    agent: str,
    scope: str,
    project_dir: Path | None,
    dest: Path | None,
    namespace_dest_by_agent: bool,
    force: bool,
    dry_run: bool,
) -> None:
    if agent not in skill.get("compatibility", []):
        raise SystemExit(f"{skill['id']} is not compatible with {agent}")
    rel_entrypoint = skill.get("entrypoints", {}).get(agent)
    if not rel_entrypoint:
        raise SystemExit(f"{skill['id']} does not define entrypoints.{agent}")
    source = str(skill.get("source", ""))
    if is_remote_source(source):
        raise SystemExit(f"remote sources are not installed by this local CLI yet: {source}")
    source_root = (registry_path.parent / source).resolve()
    src = source_root / rel_entrypoint
    dst_root = destination_root(agent, scope, project_dir, dest).resolve()
    if namespace_dest_by_agent:
        dst_root = dst_root / agent
    dst = dst_root / skill["id"]
    copy_skill(src, dst, force=force, dry_run=dry_run)


def expand_agents(selected_agents: list[str]) -> list[str]:
    agents: list[str] = []
    for selected in selected_agents:
        agents.extend(SUPPORTED_AGENTS if selected == "both" else [selected])
    return list(dict.fromkeys(agents))


def cmd_validate(args: argparse.Namespace) -> int:
    errors = validate_registry(args.registry.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"ok: {args.registry}")
    return 0


def cmd_install(args: argparse.Namespace) -> int:
    agents = expand_agents(args.agent)
    registry_path = args.registry.resolve()
    registry = load_registry(registry_path)
    by_id = registry_by_id(registry)

    if args.all:
        selected_skills = list(by_id.values())
    else:
        if not args.skills:
            raise SystemExit("provide at least one skill id or --all")
        missing = [skill_id for skill_id in args.skills if skill_id not in by_id]
        if missing:
            raise SystemExit(f"unknown skill id(s): {', '.join(missing)}")
        selected_skills = [by_id[skill_id] for skill_id in args.skills]

    namespace_dest_by_agent = args.dest is not None and len(agents) > 1

    for skill in selected_skills:
        for agent in agents:
            if agent in skill.get("compatibility", []):
                install_skill(
                    registry_path=registry_path,
                    skill=skill,
                    agent=agent,
                    scope=args.scope,
                    project_dir=args.project_dir,
                    dest=args.dest,
                    namespace_dest_by_agent=namespace_dest_by_agent,
                    force=args.force,
                    dry_run=args.dry_run,
                )
            elif not args.all:
                raise SystemExit(f"{skill['id']} is not compatible with {agent}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agent-skill", description="Install and validate agent skills for Codex and Claude.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="Validate registry structure and local entrypoints.")
    validate.add_argument("--registry", default="registry.json", type=Path, help="Registry JSON path.")
    validate.set_defaults(func=cmd_validate)

    install = subparsers.add_parser("install", help="Install one or more skills for Codex or Claude.")
    install.add_argument("--registry", default="registry.json", type=Path, help="Registry JSON path.")
    install.add_argument("skills", nargs="*", help="Skill ids to install. Use --all to install every compatible skill.")
    install.add_argument("--all", action="store_true", help="Install every registry skill compatible with the selected agent(s).")
    install.add_argument("--agent", choices=[*SUPPORTED_AGENTS, "both"], action="append", required=True, help="Target agent. Repeatable. Use both for Codex and Claude.")
    install.add_argument("--scope", choices=["user", "project"], default="user", help="Install to user or project skill directory.")
    install.add_argument("--project-dir", type=Path, help="Project root for --scope project. Defaults to current directory.")
    install.add_argument("--dest", type=Path, help="Override destination skills root. Useful for tests or custom installs.")
    install.add_argument("--force", action="store_true", help="Replace an existing installed skill directory.")
    install.add_argument("--dry-run", action="store_true", help="Print planned installs without copying files.")
    install.set_defaults(func=cmd_install)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
