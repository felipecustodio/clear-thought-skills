---
name: orchestration-suggest
description: Recommends the optimal reasoning pattern or sequence of skills based on task complexity, constraints, and domain.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Orchestration Suggest acts as a meta-cognitive router, analyzing a user prompt and recommending which specific reasoning skills or workflows should be chained together for optimal problem solving.

## When to Use

- **Complex Unstructured Prompts**: When it is unclear which thinking framework is best suited.
- **Workflow Planning**: Designing multi-stage agent execution chains.

## Execution Workflow

1. **Analyze Task Attributes**: Evaluate complexity, domain, certainty, and constraint rigidity.
2. **Match Reasoning Patterns**: Select candidate frameworks (e.g., `sequential-thinking`, `pdr-reasoning`, `tree-of-thought`).
3. **Construct Execution Sequence**: Order selected patterns into a coherent workflow pipeline.
4. **Provide Rationale**: Explain why the chosen sequence fits the task profile.

## Expected Output Contract

```markdown
### Recommended Orchestration Pipeline
1. `Step 1: [Skill Name]` - [Rationale]
2. `Step 2: [Skill Name]` - [Rationale]
- **Estimated Complexity**: [Low / Medium / High]
```

## Scripts

- `scripts/orchestration_suggest.py` - Deterministic evaluation, state validation, and CLI tool for orchestration-suggest.

