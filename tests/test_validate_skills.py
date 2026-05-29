"""Tests for local Agent Skill validation."""

from __future__ import annotations

import json
import subprocess
import sys
from typing import TYPE_CHECKING

import pytest

from scripts import validate_skills

if TYPE_CHECKING:
    from pathlib import Path


def skill_markdown(
    *,
    name: str = "demo-skill",
    description: str = "Use this skill when validating demo skill behavior.",
    license_name: str = "MIT",
    compatibility: str | None = None,
    body: str = "## Use When\n\n- Validating tests.\n",
) -> str:
    compatibility_line = f"compatibility: {compatibility}\n" if compatibility is not None else ""
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {description}\n"
        f"license: {license_name}\n"
        f"{compatibility_line}"
        "---\n\n"
        f"{body}"
    )


def evals_json(
    *,
    skill_name: str = "demo-skill",
    assertions: list[str] | None = None,
    files: list[str] | None = None,
) -> str:
    case = {
        "id": "normal",
        "prompt": "Validate this skill.",
        "expected_output": "Validation passes.",
        "files": [] if files is None else files,
        "assertions": ["Validation succeeds."] if assertions is None else assertions,
    }
    edge = {
        "id": "edge",
        "prompt": "Validate a minimal skill.",
        "expected_output": "Validation still passes.",
        "files": [],
        "assertions": ["Validation handles empty files list."],
    }
    return json.dumps({"skill_name": skill_name, "evals": [case, edge]})


def write_skill(
    root: Path,
    *,
    directory: str = "demo-skill",
    markdown: str | None = None,
    evals: str | None = None,
) -> Path:
    skill_dir = root / directory
    eval_dir = skill_dir / "evals"
    eval_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(markdown or skill_markdown(), encoding="utf-8")
    (eval_dir / "evals.json").write_text(evals or evals_json(), encoding="utf-8")
    return skill_dir


def test_validate_skill_accepts_valid_skill(tmp_path: Path) -> None:
    skill_dir = write_skill(tmp_path)

    assert validate_skills.validate_skill(skill_dir) == []


@pytest.mark.parametrize(
    ("markdown", "expected"),
    [
        ("not frontmatter", "must start with YAML frontmatter"),
        ("---\nname: demo-skill\nfoo: bar\n", "frontmatter must end"),
        ("---\ninvalid\n---\nbody", "invalid frontmatter line"),
        ("---\n: value\n---\nbody", "empty frontmatter key"),
        (skill_markdown(name="wrong-name"), "must match directory"),
        (skill_markdown(name="Bad--Name"), "single hyphens"),
        (skill_markdown(name="a" * 65), "64 characters"),
        (skill_markdown(description="x" * 1025), "1024 characters"),
        (skill_markdown(license_name="Apache-2.0"), "license must be MIT"),
        (skill_markdown(compatibility="x" * 501), "500 characters"),
        (skill_markdown(body=""), "body must not be empty"),
        (skill_markdown(description=""), "'description' must be a non-empty string"),
    ],
)
def test_validate_skill_rejects_bad_frontmatter(
    tmp_path: Path,
    markdown: str,
    expected: str,
) -> None:
    skill_dir = write_skill(tmp_path, markdown=markdown)

    errors = validate_skills.validate_skill(skill_dir)

    assert any(expected in error for error in errors)


def test_validate_skill_reports_missing_skill_file(tmp_path: Path) -> None:
    skill_dir = tmp_path / "missing-skill"
    skill_dir.mkdir()

    assert validate_skills.validate_skill(skill_dir) == [f"{skill_dir}: missing SKILL.md"]


def test_validate_skill_reports_missing_eval_file(tmp_path: Path) -> None:
    skill_dir = tmp_path / "demo-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text(skill_markdown(), encoding="utf-8")

    errors = validate_skills.validate_skill(skill_dir)

    assert errors == [f"{skill_dir}: missing evals/evals.json"]


@pytest.mark.parametrize(
    ("evals", "expected"),
    [
        ("{", "invalid JSON"),
        ("[]", "root must be an object"),
        (evals_json(skill_name="wrong-skill"), "skill_name must be"),
        (json.dumps({"skill_name": "demo-skill", "evals": []}), "at least 2 cases"),
        (
            json.dumps({"skill_name": "demo-skill", "evals": ["bad", "bad"]}),
            "must be an object",
        ),
        (
            json.dumps(
                {
                    "skill_name": "demo-skill",
                    "evals": [
                        {
                            "id": "",
                            "prompt": "",
                            "expected_output": "",
                            "files": [],
                            "assertions": ["ok"],
                        },
                        {
                            "id": "edge",
                            "prompt": "Prompt.",
                            "expected_output": "Output.",
                            "files": [],
                            "assertions": ["ok"],
                        },
                    ],
                },
            ),
            "must be present and non-empty",
        ),
        (evals_json(files=[""]), "files must be a list"),
        (evals_json(assertions=[]), "assertions must be a non-empty list"),
    ],
)
def test_validate_evals_rejects_bad_eval_files(
    tmp_path: Path,
    evals: str,
    expected: str,
) -> None:
    skill_dir = write_skill(tmp_path, evals=evals)

    errors = validate_skills.validate_skill(skill_dir)

    assert any(expected in error for error in errors)


def test_find_skill_dirs_handles_missing_and_sorted_dirs(tmp_path: Path) -> None:
    missing = tmp_path / "missing"
    (tmp_path / "z-skill").mkdir()
    (tmp_path / "a-skill").mkdir()
    (tmp_path / "README.md").write_text("ignore", encoding="utf-8")

    assert validate_skills.find_skill_dirs(missing) == []
    assert [path.name for path in validate_skills.find_skill_dirs(tmp_path)] == [
        "a-skill",
        "z-skill",
    ]


def test_main_reports_success_for_valid_skills(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    write_skill(tmp_path)

    exit_code = validate_skills.main(["--skills-dir", str(tmp_path)])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Validated 1 skill directories." in captured.out


def test_main_reports_errors_for_invalid_skills(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    write_skill(tmp_path, evals=evals_json(assertions=[]))

    exit_code = validate_skills.main(["--skills-dir", str(tmp_path)])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "assertions must be a non-empty list" in captured.err


def test_validate_script_cli_runs(tmp_path: Path) -> None:
    write_skill(tmp_path)

    result = subprocess.run(  # noqa: S603
        [
            sys.executable,
            "scripts/validate_skills.py",
            "--skills-dir",
            str(tmp_path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "Validated 1 skill directories." in result.stdout
