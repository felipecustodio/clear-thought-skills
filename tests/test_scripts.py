import subprocess
import sys
from pathlib import Path
from typing import Any


def run_script(path: str, args: list[str]) -> subprocess.CompletedProcess[str]:
    cmd = [sys.executable, path, *args]
    return subprocess.run(cmd, capture_output=True, text=True, check=False)  # noqa: S603


def test_all_skill_scripts() -> None:
    scripts = [str(p) for p in Path("skills").glob("*/scripts/*.py")]
    assert len(scripts) >= 35  # noqa: PLR2004
    for script_path in scripts:
        # Test --help
        res_help = run_script(script_path, ["--help"])
        assert res_help.returncode == 0
        assert "usage" in res_help.stdout.lower()

        # Test execution with --json
        res_exec = run_script(script_path, ["--input", "test_payload", "--json"])
        assert res_exec.returncode == 0
        assert "success" in res_exec.stdout


def test_session_export(tmp_path: Any) -> None:  # noqa: ANN401
    f = tmp_path / "out.json"
    res = run_script(
        "skills/session-export/scripts/session_export.py",
        ["--file", str(f), "--data", '{"test": 1}'],
    )
    assert res.returncode == 0


def test_session_import(tmp_path: Any) -> None:  # noqa: ANN401
    f = tmp_path / "in.json"
    f.write_text('{"test": 1}')
    res = run_script(
        "skills/session-import/scripts/session_import.py",
        ["--file", str(f)],
    )
    assert res.returncode == 0
    assert "imported" in res.stdout or "success" in res.stdout
