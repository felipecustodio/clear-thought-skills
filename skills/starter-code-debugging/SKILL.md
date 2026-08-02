---
name: starter-code-debugging
description: "Starter skill for systematic software debugging and bug resolution. Orchestrates error isolation, code dry-runs, sequential thinking, and regression prevention."
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

starter-code-debugging acts as an automated starter orchestration pipeline. It chains together the ideal combination of reasoning skills for high-level tasks, ensuring structured execution without manual skill routing.

## Execution Workflow

1. **Isolate Error Boundary (`debugging-approach`)**: Use binary search troubleshooting to isolate the root failure line or component.
2. **Execute Code Dry-Run (`code-execution-reasoning`)**: Perform line-by-line mental execution tracking variable states and pointer references.
3. **Iterative Refinement (`sequential-thinking`)**: Step through code logic, revising hypotheses as new evidence is revealed.
4. **Stress-Test & Red-Team Fix (`pdr-reasoning`)**: Predict edge cases, attempt to break the solution, and harden against regressions.

## Expected Output Contract

```markdown
### Starter Workflow Execution: [starter-code-debugging]
- **Phase 1 Output**: [Initial Analysis]
- **Phase 2 Output**: [Detailed Evaluation]
- **Final Synthesized Solution**: [Complete Recommendation]
```

## Scripts

- `scripts/starter_code_debugging.py` - Orchestration helper and state validation tool for starter-code-debugging.

## Gotchas

- Ensure all sub-skill prerequisites are satisfied before executing downstream pipeline steps.
