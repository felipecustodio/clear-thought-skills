---
name: code-execution-reasoning
description: Mental dry-run execution of code blocks, tracking variable states, call stacks, memory references, and iteration indices step by step.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Code Execution Reasoning performs a rigorous mental dry-run of code line by line. It tracks environment variables, heap/stack states, pointer mutations, and loop counters to detect off-by-one errors and race conditions.

## When to Use

- **Code Review**: Auditing algorithmic code without running it directly.
- **Static Bug Hunting**: Locating off-by-one errors, null pointers, or memory leaks.

## Execution Workflow

1. **Initialize State**: List input variables and their initial memory state.
2. **Line-by-Line Execution Trace**:
   - For each executed statement, record modified variables and current control flow line.
3. **Loop & Condition Verification**: Verify loop invariants, boundary indices ($i=0, i=N-1$), and terminating conditions.
4. **Return State Verification**: Confirm final returned payload matches requirements.

## Expected Output Contract

```markdown
### Code Dry-Run Trace
| Line | Code Statement | Variable States | Control Flow |
| :--- | :--- | :--- | :--- |
| L1 | `x = 5` | `{x: 5}` | Next L2 |
| L2 | `x += 1` | `{x: 6}` | Next L3 |

- **Final Returned Value**: [Result]
- **Detected Issues**: [Boundary/State errors]
```

## Scripts

- `scripts/code_execution_reasoning.py` - Deterministic evaluation, state validation, and CLI tool for code-execution-reasoning.

