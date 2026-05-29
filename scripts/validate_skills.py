"""Validate Agent Skill directories and eval metadata."""
# ruff: noqa: EM101, EM102, TRY003

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, cast

NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")
FRONTMATTER_MIN_LINES = 3
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
MAX_COMPATIBILITY_LENGTH = 500
MIN_EVAL_CASES = 2


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) < FRONTMATTER_MIN_LINES or lines[0] != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter delimited by ---")

    try:
        end = lines[1:].index("---") + 1
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter must end with ---") from exc

    frontmatter: dict[str, Any] = {}
    for line_number, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line {line_number}: {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            raise ValueError(f"empty frontmatter key on line {line_number}")
        frontmatter[key] = value.strip("\"'")

    body = "\n".join(lines[end + 1 :]).strip()
    return frontmatter, body


def require_string(mapping: dict[str, Any], key: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key!r} must be a non-empty string")
    return value


def validate_skill(skill_dir: Path) -> list[str]:  # noqa: C901
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    eval_file = skill_dir / "evals" / "evals.json"

    if not skill_file.exists():
        return [f"{skill_dir}: missing SKILL.md"]

    try:
        frontmatter, body = parse_frontmatter(skill_file)
        name = require_string(frontmatter, "name")
        description = require_string(frontmatter, "description")

        if name != skill_dir.name:
            errors.append(
                f"{skill_file}: name {name!r} must match directory {skill_dir.name!r}",
            )
        if not NAME_RE.fullmatch(name) or "--" in name:
            errors.append(
                f"{skill_file}: name must use lowercase letters, numbers, and single hyphens",
            )
        if len(name) > MAX_NAME_LENGTH:
            errors.append(f"{skill_file}: name must be 64 characters or fewer")
        if len(description) > MAX_DESCRIPTION_LENGTH:
            errors.append(f"{skill_file}: description must be 1024 characters or fewer")
        if frontmatter.get("license") != "MIT":
            errors.append(f"{skill_file}: license must be MIT")
        compatibility = frontmatter.get("compatibility")
        if compatibility is not None and (
            not isinstance(compatibility, str) or len(compatibility) > MAX_COMPATIBILITY_LENGTH
        ):
            errors.append(
                f"{skill_file}: compatibility must be a string of 500 characters or fewer",
            )
        if not body:
            errors.append(f"{skill_file}: body must not be empty")
    except ValueError as exc:
        errors.append(f"{skill_file}: {exc}")

    if not eval_file.exists():
        errors.append(f"{skill_dir}: missing evals/evals.json")
    else:
        errors.extend(validate_evals(eval_file, skill_dir.name))

    return errors


def validate_evals(eval_file: Path, skill_name: str) -> list[str]:  # noqa: C901
    errors: list[str] = []
    try:
        data = json.loads(eval_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{eval_file}: invalid JSON: {exc}"]

    if not isinstance(data, dict):
        return [f"{eval_file}: root must be an object"]

    if data.get("skill_name") != skill_name:
        errors.append(f"{eval_file}: skill_name must be {skill_name!r}")

    evals = data.get("evals")
    if not isinstance(evals, list) or len(evals) < MIN_EVAL_CASES:
        errors.append(f"{eval_file}: evals must contain at least 2 cases")
        return errors

    for index, case in enumerate(evals):
        prefix = f"{eval_file}: evals[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{prefix} must be an object")
            continue
        eval_case = cast("dict[str, object]", case)
        for key in ("id", "prompt", "expected_output"):
            value = eval_case.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(
                    f"{prefix}.{key} must be a non-empty string",
                )
        files = eval_case.get("files")
        if not isinstance(files, list) or any(
            not isinstance(item, str) or not item for item in files
        ):
            errors.append(f"{prefix}.files must be a list of non-empty strings")
        assertions = eval_case.get("assertions")
        if (
            not isinstance(assertions, list)
            or not assertions
            or any(not isinstance(item, str) or not item for item in assertions)
        ):
            errors.append(
                f"{prefix}.assertions must be a non-empty list of non-empty strings",
            )

    return errors


def find_skill_dirs(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.iterdir() if path.is_dir())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate Agent Skill directories and eval files.",
    )
    parser.add_argument(
        "--skills-dir",
        default="skills",
        help="Directory containing skill directories.",
    )
    args = parser.parse_args(argv)

    skill_dirs = find_skill_dirs(Path(args.skills_dir))
    errors = [error for skill_dir in skill_dirs for error in validate_skill(skill_dir)]

    if errors:
        for error in errors:
            sys.stderr.write(f"{error}\n")
        return 1

    sys.stdout.write(f"Validated {len(skill_dirs)} skill directories.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
