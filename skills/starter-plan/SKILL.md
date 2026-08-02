---
name: starter-plan
description: "Fundamental Planning Phase starter skill. Orchestrates goal decomposition, constraint discovery, alternative exploration, scope boundary locks, and risk red-teaming before execution."
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

starter-plan is a starter workflow for for the primary agent loop: PLAN. It ensures disciplined execution of reasoning frameworks throughout this critical phase.

## Execution Workflow

1. **Orchestrate Planning Pipeline (`orchestration-suggest`)**: Analyze prompt and select optimal sub-skill sequences.
2. **Discover Requirements & Constraints (`socratic-method`)**: Probe hidden assumptions, non-functional requirements, and boundary conditions.
3. **Map System Architecture (`systems-thinking`)**: Identify component interconnections, feedback loops, and use points.
4. **Explore Alternative Plans (`tree-of-thought`)**: Evaluate multiple strategic execution branches using heuristic scoring.
5. **Set Scope & Hard Boundaries (`ulysses-protocol`)**: Lock in strict scope limits and stopping criteria to prevent creep.
6. **Stress-Test & Red-Team Plan (`pdr-reasoning`)**: Predict failure modes and build contingency safeguards into the plan.
7. **Serialize Plan State (`session-export`)**: Export the verified plan to disk for execution hand-off.

## Expected Output Contract

```markdown
### Agentic Loop Phase: [STARTER-PLAN]
- **Phase Status**: [Complete / In Progress]
- **Key Deliverables**: [Summary of Phase Output]
- **Hand-off Artifact**: [Exported State / Implementation Code]
```

## Scripts

- `scripts/starter_plan.py` - State serialization and execution helper for starter-plan.

## Gotchas

- Ensure `starter-plan` has exported a valid plan state before triggering `starter-implement`.
