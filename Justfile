sync:
    uv sync

lock:
    uv lock

lint:
    uv run ruff check .
    uv run ruff format --check .

type:
    uv run ty check

test:
    uv run pytest -n auto

validate-skills:
    uv run python scripts/validate_skills.py

check-lock:
    uv lock --check

check: check-lock lint type test validate-skills
    uv run prek run --all-files
