import subprocess
import sys
from typing import Any


def run_script(path: str, args: list[str]) -> subprocess.CompletedProcess:
    cmd = [sys.executable, path, *args]
    return subprocess.run(cmd, capture_output=True, text=True, check=False)  # noqa: S603


def test_sequential_thinking() -> None:
    res = run_script(
        "skills/sequential-thinking/scripts/sequential_thinking.py",
        ["--thought", "hello", "--number", "1"],
    )
    assert res.returncode == 0
    assert "ok" in res.stdout

    res2 = run_script("skills/sequential-thinking/scripts/sequential_thinking.py", ["--help"])
    assert res2.returncode == 0
    assert "usage" in res2.stdout.lower()

    res3 = run_script("skills/sequential-thinking/scripts/sequential_thinking.py", [])
    assert res3.returncode != 0


def test_session_export(tmp_path: Any) -> None:  # noqa: ANN401
    f = tmp_path / "out.json"
    res = run_script(
        "skills/session-export/scripts/session_export.py",
        ["--file", str(f), "--data", '{"test": 1}'],
    )
    assert res.returncode == 0
    assert "exported" in res.stdout
    assert f.exists()

    res2 = run_script("skills/session-export/scripts/session_export.py", ["--help"])
    assert res2.returncode == 0

    res3 = run_script(
        "skills/session-export/scripts/session_export.py", ["--file", str(f), "--data", "invalid"]
    )
    assert res3.returncode == 1


def test_session_import(tmp_path: Any) -> None:  # noqa: ANN401
    f = tmp_path / "in.json"
    f.write_text('{"test": 1}')
    res = run_script("skills/session-import/scripts/session_import.py", ["--file", str(f)])
    assert res.returncode == 0
    assert "imported" in res.stdout

    res2 = run_script("skills/session-import/scripts/session_import.py", ["--help"])
    assert res2.returncode == 0

    res3 = run_script(
        "skills/session-import/scripts/session_import.py", ["--file", "doesnotexist.json"]
    )
    assert res3.returncode == 1

    f2 = tmp_path / "bad.json"
    f2.write_text("invalid")
    res4 = run_script("skills/session-import/scripts/session_import.py", ["--file", str(f2)])
    assert res4.returncode == 1
