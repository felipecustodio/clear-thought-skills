---
name: starter-implement
description: "Fundamental Execution Phase starter skill. Restores stored plan state and orchestrates step-by-step implementation, code dry-runs, metacognitive self-correction, and debugging."
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

starter-implement acts as an automated starter orchestration skill for the primary agent loop: IMPLEMENT. It ensures disciplined execution of reasoning frameworks throughout this critical phase.

## Execution Workflow

1. **Import Verified Plan (`session-import`)**: Deserializes stored plan state from disk to initialize memory context.
2. **Execute Step-by-Step (`sequential-thinking`)**: Trace execution steps linearly, allowing dynamic thought revisions when needed.
3. **Code Dry-Run & State Inspection (`code-execution-reasoning`)**: Track memory, loop invariants, and pointer state line by line.
4. **Metacognitive Self-Audit (`metacognitive-monitoring`)**: Monitor execution in real time to detect confidence drift or confirmation bias.
5. **Systematic Debugging (`debugging-approach`)**: If an anomaly or test failure occurs, isolate root causes via binary search troubleshooting.
6. **Serialize Execution State (`session-export`)**: Save final implementation state to disk.

## Expected Output Contract

```markdown
### Agentic Loop Phase: [STARTER-IMPLEMENT]
- **Phase Status**: [Complete / In Progress]
- **Key Deliverables**: [Summary of Phase Output]
- **Hand-off Artifact**: [Exported State / Implementation Code]
```

## Scripts

- `scripts/starter_implement.py` - State serialization and execution helper for starter-implement.

## Gotchas

- Ensure `starter-plan` has exported a valid plan state before triggering `starter-implement`.
