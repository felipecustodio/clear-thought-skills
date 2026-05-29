Use modern Python.

Use `uv` for Python tooling:
- `pyproject.toml` is the dependency source of truth.
- `uv lock` updates `uv.lock` after dependency changes.
- `uv sync` installs the locked environment from `pyproject.toml` and `uv.lock`.
- `uv run <command>` runs project commands.
- `uv add <package>` adds runtime dependencies and updates `uv.lock`.
- `uv add --dev <package>` adds development dependencies and updates `uv.lock`.
- Commit `pyproject.toml` and `uv.lock` together.

Use Astral tools:
- `uv run ruff check .` lints.
- `uv run ruff format .` formats.
- `uv run ty check` type checks.

Use `prek` for git hooks. Do not use `pre-commit`.

Use `just` targets:
- `just lock` updates `uv.lock`.
- `just sync` installs the locked environment.
- `just check-lock` verifies `uv.lock` matches `pyproject.toml`.
- `just lint` lints and checks formatting.
- `just type` type checks.
- `just test` runs tests.
- `just validate-skills` validates Agent Skill metadata and eval files.
- `just check` runs all required checks.

Validate skills with `uv run python scripts/validate_skills.py`.

Before pushing code, run `just check` and fix failures.

GitHub CI must pass for PRs before merge. Required CI gates: lockfile, lint, type check, tests, and skill validation.

Use conventional commits.
Keep commit messages concise.

Use conventional branch names:
- `feat/<short-description>` for features.
- `fix/<short-description>` for bug fixes.
- `docs/<short-description>` for documentation.
- `test/<short-description>` for tests.
- `ci/<short-description>` for CI-only work.
- `chore/<short-description>` for maintenance.

PR title format: `<type>: <concise summary>`.

PR body format:
- `## Summary` with 2-5 bullets.
- `## Validation` with commands run and results.
- `## Notes` only when useful.
- Keep wording concise.
- Use Mermaid diagrams when they clarify flow, architecture, or dependency relationships.
