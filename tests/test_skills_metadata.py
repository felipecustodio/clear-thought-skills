import json
from pathlib import Path


def test_skills_frontmatter() -> None:
    skills = list(Path("skills").glob("*/SKILL.md"))
    assert len(skills) > 0
    for s in skills:
        with s.open("r", encoding="utf-8") as f:
            content = f.read()
        assert content.startswith("---")
        assert "name:" in content
        assert "description:" in content


def test_evals_schema() -> None:
    evals = list(Path("skills").glob("*/evals/evals.json"))
    assert len(evals) > 0
    for e in evals:
        with e.open("r", encoding="utf-8") as f:
            data = json.load(f)
        assert "skill_name" in data
        assert "evals" in data
        assert len(data["evals"]) >= 2  # noqa: PLR2004
        for ev in data["evals"]:
            assert "id" in ev
            assert "prompt" in ev
            assert "expected_output" in ev
            assert "assertions" in ev
            assert "files" in ev
