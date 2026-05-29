# Clear Thought Skills Specification

## Goal

Migrate `clearthought-onepointfive` MCP server by Waldzell AI into Agent Skills plus small modular Python scripts.

Outcome: all reasoning and thinking tools exist as installable skill directories. Each skill uses `SKILL.md` for agent-facing reasoning workflow and `scripts/` only for deterministic computation, validation, formatting, or state transforms.

This is a migration of capability, not architecture. The target project MUST use its own minimal, clearer organization instead of copying `clearthought-onepointfive` folders, categories, naming quirks, or MCP dispatch structure.

## Source

- Source project: `clearthought-onepointfive/`
- Source MCP package: `@waldzellai/clear-thought-onepointfive`
- Source license: MIT
- Source model: single `clear_thought` MCP tool with operation dispatch
- Target model: many focused Agent Skills with required Python support for deterministic checks, templates, validation, formatting, or algorithms
- Agent Skills docs index: `https://agentskills.io/llms.txt`

## Principles

- Prefer skill instructions over code for reasoning workflows.
- Put repeatable algorithms in Python scripts.
- Keep scripts narrow, deterministic, non-interactive.
- Keep `SKILL.md` under 500 lines and ideally under 5,000 tokens.
- Use progressive disclosure: main workflow in `SKILL.md`, detailed examples in `references/`, reusable templates in `assets/`.
- Use modern Python and `uv`.
- Use Astral tools: `ruff` for linting/formatting and `ty` for type checking.
- Use `prek` for git hooks; do not use `pre-commit`.
- Preserve Clear Thought operation intent, not MCP transport.
- Prefer a smaller, cleaner target organization over source parity.
- Avoid building another MCP server.
- Avoid hidden global state. Use explicit session import/export files for session skills.

## Repository Shape

This is the preferred minimal shape. It does not need to mirror source TypeScript directories.

```text
.
├── README.md
├── SPEC.md
├── AGENTS.md
├── Justfile
├── .pre-commit-config.yaml
├── pyproject.toml
├── uv.lock
├── scripts/
│   └── validate_skills.py
├── skills/
│   ├── sequential-thinking/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   ├── references/
│   │   └── evals/
│   └── ...
├── shared/
│   └── clear_thought/
│       ├── __init__.py
│       ├── schemas.py
│       ├── formatting.py
│       └── validation.py
└── tests/
```

## Skill Format

Every skill directory MUST contain `SKILL.md` with valid YAML frontmatter:

```yaml
---
name: skill-name
description: Use this skill when...
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---
```

Rules:

- `name` matches parent directory.
- `name` uses lowercase letters, numbers, hyphens only.
- `description` says what task skill handles and when agent MUST use it.
- `description` stays under 1024 characters.
- `license` is `MIT`.
- `compatibility` only appears when scripts need Python or external tools.

## Script Rules

Use Python for bundled scripts.

Scripts MUST:

- run with `uv run scripts/<name>.py ...`;
- expose `--help`;
- accept inputs via flags, files, or stdin;
- avoid prompts and TTY interaction;
- send machine-readable output to stdout;
- send diagnostics to stderr;
- return meaningful non-zero exit codes on failure;
- validate arguments before execution;
- use typed functions and dataclasses or Pydantic where helpful;
- include focused tests when behavior is non-trivial.

Scripts MUST use PEP 723 inline metadata when dependencies are local to that script. Shared package code belongs under `shared/clear_thought/`.

## Skill Template

Each `SKILL.md` MUST follow this structure:

```markdown
---
name: example-skill
description: Use this skill when the user needs...
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- ...

## Workflow

1. ...
2. ...
3. ...

## Outputs

- ...

## Scripts

- `scripts/example.py` - ...

## Gotchas

- ...
```

## Operation Mapping

Convert all source operations. Names below use Agent Skill directory naming.

| Source operation | Target skill | Python support |
| --- | --- | --- |
| `sequential_thinking` | `sequential-thinking` | planner and sequence validator |
| `tree_of_thought` | `tree-of-thought` | branch scoring |
| `beam_search` | `beam-search` | required for beam expansion/ranking |
| `mcts` | `monte-carlo-tree-search` | required for selection/rollout/backprop helpers |
| `graph_of_thought` | `graph-of-thought` | required for graph validation/traversal |
| `mental_model` | `mental-model` | model catalog lookup |
| `debugging_approach` | `debugging-approach` | hypothesis tracker |
| `creative_thinking` | `creative-thinking` | idea scoring/dedup |
| `visual_reasoning` | `visual-reasoning` | diagram schema validator |
| `metacognitive_monitoring` | `metacognitive-monitoring` | checklist scorer |
| `scientific_method` | `scientific-method` | experiment template generator |
| `collaborative_reasoning` | `collaborative-reasoning` | persona/round manager |
| `decision_framework` | `decision-framework` | required for weighted decision math |
| `socratic_method` | `socratic-method` | question ladder generator |
| `structured_argumentation` | `structured-argumentation` | argument map validator |
| `systems_thinking` | `systems-thinking` | required for component/edge/loop checks |
| `research` | `research-reasoning` | source matrix formatter |
| `analogical_reasoning` | `analogical-reasoning` | mapping table generator |
| `causal_analysis` | `causal-analysis` | required for graph/intervention checks |
| `statistical_reasoning` | `statistical-reasoning` | required for summary/Bayes/test/Monte Carlo math |
| `simulation` | `simulation-reasoning` | required for deterministic simulation runner |
| `optimization` | `optimization-reasoning` | required for grid/search objective evaluation |
| `ethical_analysis` | `ethical-analysis` | stakeholder matrix formatter |
| `mdp_planning` | `mdp-planning` | required for value/policy iteration |
| `decision_networks` | `decision-networks` | required for expected utility computation |
| `visual_dashboard` | `visual-dashboard` | dashboard spec generator |
| `custom_framework` | `custom-framework` | framework schema validator |
| `code-execution` | `code-execution-reasoning` | required sandbox runner |
| `orchestration_suggest` | `orchestration-suggest` | skill router table |
| `orchestration-suggest` | `orchestration-suggest` | merge alias into same skill |
| `ooda-loop` | `ooda-loop` | loop tracker |
| `ulysses-protocol` | `ulysses-protocol` | phase gate validator |
| `pdr-reasoning` | `pdr-reasoning` | required PDR graph algorithms |
| `session_info` | `session-info` | required local session inspection helper |
| `session_export` | `session-export` | required explicit JSON export helper |
| `session_import` | `session-import` | required explicit JSON import helper |
| `notebook_create` | excluded | notebook feature, not reasoning tool |
| `notebook_add_cell` | excluded | notebook feature, not reasoning tool |
| `notebook_run_cell` | excluded | notebook feature, not reasoning tool |
| `notebook_export` | excluded | notebook feature, not reasoning tool |

Notebook operations are excluded from this migration. They are not reasoning tools.

## Skill Grouping

Default: one source reasoning operation becomes one skill.

Exceptions:

- Pattern aliases (`tree_of_thought`, `beam_search`, `mcts`, `graph_of_thought`) remain separate skills and share references with `sequential-thinking` so descriptions trigger precisely.
- `orchestration_suggest` and `orchestration-suggest` merge into one `orchestration-suggest` skill.
- Session tools remain separate skills and use explicit local JSON import/export. Hidden global persistence remains out of scope.

## Shared Python Package

`shared/clear_thought/` provides code reused by scripts:

- `schemas.py`: dataclasses or Pydantic models for common inputs.
- `validation.py`: graph, probability, criteria, and numeric validation helpers.
- `formatting.py`: JSON and Markdown result rendering.
- `math_utils.py`: normalization, scoring, probability helpers.

Shared package MUST avoid agent-specific APIs. Scripts call package functions; skills call scripts.

## Python Tooling

Use `uv` for all Python package management.

Package management rules:

- `pyproject.toml` is the source of truth for project metadata, runtime dependencies, development dependencies, and tool configuration.
- `uv.lock` is required and MUST be committed.
- Use `uv add <package>` for runtime dependencies.
- Use `uv add --dev <package>` for development dependencies.
- Run `uv lock` after dependency or Python version changes.
- Run `uv sync` before checks to install the locked environment.
- Commit `pyproject.toml` and `uv.lock` in the same change whenever dependencies change.
- Do not use `pip install`, `pip-tools`, Poetry, Pipenv, Conda environment files, or ad hoc requirements files for project dependency management.

Commands:

```bash
uv lock
uv sync
uv run pytest -n auto
uv run ruff check .
uv run ruff format --check .
uv run ty check
uv run python scripts/validate_skills.py
uv run prek run --all-files
```

Minimum `pyproject.toml`:

```toml
[project]
name = "clear-thought-skills"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []

[dependency-groups]
dev = [
  "pytest>=8",
  "pytest-cov>=6",
  "pytest-xdist>=3",
  "pytest-randomly>=3",
  "pytest-timeout>=2",
  "ruff>=0.8",
  "ty>=0.0.1a",
  "prek>=0.2",
]

[tool.pytest.ini_options]
addopts = "-n auto --cov=shared --cov=scripts --cov-report=term-missing --cov-report=xml --strict-config --strict-markers"
testpaths = ["tests"]

[tool.ruff]
target-version = "py312"
line-length = 100

[tool.ruff.lint]
select = ["ALL"]
ignore = ["COM812", "D"]
```

Add runtime dependencies only when script complexity justifies them.

## Just Targets

Use `just` as command runner.

Required targets:

```just
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
```

`just check` is the required local gate before pushing code.

`just lock` updates `uv.lock` from `pyproject.toml`.

`just check-lock` verifies `uv.lock` matches `pyproject.toml`.

`just validate-skills` is the required Agent Skills metadata and eval schema gate.

## Git Hooks

Use `prek`, not `pre-commit`.

Required hooks:

- `uv-lock-check`
- `ruff-check`
- `ruff-format`
- `ty-check`
- `pytest`
- `validate-skills`

Hook config MUST live in `.pre-commit-config.yaml` because `prek` uses the same config format.

Install:

```bash
uv sync
uv run prek install
```

Run:

```bash
uv run prek run --all-files
```

## GitHub CI

GitHub Actions MUST run on every pull request and every push to `main`.

Required CI checks:

- lockfile validation: `just check-lock`;
- dependency installation from lockfile: `just sync`;
- lint and format checks: `just lint`;
- type checking: `just type`;
- tests: `just test`;
- skill metadata and eval schema validation: `just validate-skills`.

CI workflow lives at `.github/workflows/ci.yml`.

The repository MUST configure branch protection for `main` so PRs can merge only after the CI job named `lint type test skill-validation` passes. Direct pushes to `main` MUST also run CI.

## Test Strategy

Goal: very high test coverage across skills, scripts, shared helpers, and expected agent-facing behaviors.

Coverage targets:

- overall line coverage: 95% minimum;
- branch coverage: 90% minimum where branch coverage is enabled;
- every bundled script has CLI tests for `--help`, valid input, invalid input, and representative output;
- every shared helper has unit tests;
- every skill has metadata/frontmatter tests;
- every skill has eval definitions tested for schema validity;
- every skill has behavior tests that assert expected workflow, output contract, and gotchas are present in `SKILL.md`;
- deterministic algorithms have golden tests against source examples from `clearthought-onepointfive` where practical;
- edge cases cover invalid probabilities, malformed graphs, empty options, bad weights, missing required fields, and non-finite numbers.

Use modern pytest practices:

- `pytest-xdist` with `-n auto` for parallel execution;
- `pytest-cov` for coverage reporting;
- `pytest-randomly` to expose order coupling;
- `pytest-timeout` to prevent hung script tests;
- temporary directories via `tmp_path`;
- subprocess CLI tests for scripts instead of importing `main()` only;
- parametrized tests for operation examples and skill directories.

Tests are part of product quality, not optional migration cleanup.

## Skill Validation

Local skill validation runs with:

```bash
uv run python scripts/validate_skills.py
```

The validator MUST check:

- every directory under `skills/` contains `SKILL.md`;
- `SKILL.md` starts with YAML frontmatter delimited by `---`;
- frontmatter contains non-empty `name` and `description`;
- `name` matches the parent directory;
- `name` uses lowercase letters, numbers, and single hyphens;
- `description` is 1024 characters or fewer;
- `license` is `MIT`;
- `compatibility`, when present, is 500 characters or fewer;
- `SKILL.md` body is non-empty;
- every skill contains `evals/evals.json`;
- `evals/evals.json` has `skill_name` matching the skill directory;
- `evals/evals.json` has at least 2 eval cases;
- every eval case has non-empty `id`, `prompt`, and `expected_output`;
- every eval case has `files` as a list of non-empty strings, using `[]` when there are no input files;
- every eval case has `assertions` as a non-empty list of non-empty strings.

External spec validation uses:

```bash
skills-ref validate skills/<skill-name>
```

Run both local validation and `skills-ref` validation before marking a skill complete.

## Migration Workflow

For each operation:

1. Read source TypeScript operation and related types.
2. Identify reasoning workflow vs deterministic computation.
3. Draft `SKILL.md` with activation description, workflow, output contract, gotchas.
4. Add Python script only for deterministic logic.
5. Add references only when main skill would become too large.
6. Add eval cases under `skills/<skill>/evals/evals.json`.
7. Add script tests under `tests/`.
8. Run `uv run python scripts/validate_skills.py`.
9. Run `just check`.
10. Update migration checklist.

## Eval Requirements

Each skill MUST include at least 2 eval cases before marked complete:

- normal use case;
- edge or ambiguity case.

Eval cases MUST be realistic user prompts with expected outputs. Each skill eval suite MUST compare output quality with the skill against a baseline without the skill or against the previous skill version. Store eval run artifacts in iteration directories with `with_skill/`, `without_skill/` or `old_skill/`, `timing.json`, `grading.json`, and aggregated `benchmark.json`.

Assertions MUST be added once first-run outputs reveal concrete pass/fail checks. Grading MUST record `PASS` or `FAIL` with concrete evidence. Benchmark summaries MUST include pass-rate delta, time delta, and token delta.

Eval file:

```json
{
  "skill_name": "decision-framework",
  "evals": [
    {
      "id": "weighted-choice",
      "prompt": "Choose between three vendors using cost, reliability, and support.",
      "expected_output": "Weighted comparison with recommendation and tradeoffs.",
      "files": [],
      "assertions": [
        "Output includes criteria weights.",
        "Output includes score per option.",
        "Output states recommendation with rationale."
      ]
    }
  ]
}
```

## Validation

Skill validation:

```bash
uv run python scripts/validate_skills.py
skills-ref validate skills/<skill-name>
```

Project validation:

```bash
uv lock --check
uv sync
uv run pytest -n auto
uv run ruff check .
uv run ruff format --check .
uv run ty check
uv run python scripts/validate_skills.py
uv run prek run --all-files
```

If `skills-ref` is unavailable, local validation remains required and blocks completion on any error.

## Acceptance Criteria

Project complete when:

- every in-scope reasoning operation has target skill directory;
- every skill has valid `SKILL.md` frontmatter;
- every skill description clearly states when to use it;
- every deterministic source algorithm has Python equivalent or explicit rationale for omission;
- all Python scripts run non-interactively with `uv run`;
- tests cover all skills, bundled scripts, shared helpers, and expected skill behaviors;
- coverage meets configured thresholds;
- eval files exist for all completed skills;
- local skill validation passes;
- `skills-ref validate` passes for every skill;
- `just check` passes;
- `prek run --all-files` passes;
- GitHub CI passes on PRs and protected `main` branch;
- README documents installation and usage;
- `pyproject.toml` and `uv.lock` are current and committed;
- source MCP server is no longer required at runtime.

## Migration Checklist

- [ ] Scaffold Python project with `uv`.
- [ ] Create `pyproject.toml`.
- [ ] Generate and commit `uv.lock`.
- [ ] Add `ruff`, `ty`, `pytest`, `pytest-cov`, `pytest-xdist`, `pytest-randomly`, `pytest-timeout`, and `prek`.
- [ ] Create `Justfile`.
- [ ] Add `scripts/validate_skills.py`.
- [ ] Add `prek` hooks.
- [ ] Add GitHub CI workflow.
- [ ] Configure required branch protection for CI on `main`.
- [ ] Create shared package.
- [ ] Create skill template.
- [ ] Migrate core skills.
- [ ] Migrate pattern skills.
- [ ] Migrate collaborative skills.
- [ ] Migrate analysis skills.
- [ ] Migrate metagame skills.
- [ ] Implement session skills with explicit local JSON import/export.
- [ ] Document notebook exclusion in README.
- [ ] Add evals.
- [ ] Add high-coverage tests for skills, scripts, shared helpers, and behaviors.
- [ ] Validate skill metadata and eval schemas.
- [ ] Run `skills-ref validate` for every skill.
- [ ] Make `just check` pass.
- [ ] Update README.

## Out Of Scope

- Rebuilding MCP transport.
- Publishing to npm.
- Maintaining Smithery integration.
- Recreating interactive notebook runtime.
- Persisting hidden global agent state outside explicit session import/export files.
