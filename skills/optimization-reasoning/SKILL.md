---
name: optimization-reasoning
description: Formulates problems as mathematical or logical optimization models with explicit objective functions and constraints.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Optimization Reasoning identifies the mathematically or logically best solution from a set of available alternatives subject to defined constraints. It turns vague trade-offs into formal objective functions.

## When to Use

- **Resource Allocation**: Budgeting, memory allocation, thread pool sizing, scheduling.
- **Trade-off Analysis**: Maximizing performance while minimizing cost or latency constraints.

## Execution Workflow

1. **Identify Decision Variables**: Define the tunable variables ($x_1, x_2, \dots, x_n$).
2. **Formulate Objective Function**: State the goal explicitly (e.g., $\max f(x)$ or $\min g(x)$).
3. **Define Hard Constraints**: List non-negotiable boundaries (e.g., $h_i(x) \le C$).
4. **Evaluate Feasible Region**: Find the optimal combination of variables satisfying all constraints.

## Expected Output Contract

```markdown
### Optimization Model
- **Objective**: [Maximize / Minimize Statement]
- **Variables**: [List of decision variables]
- **Constraints**: [Hard limits]
- **Optimal Solution**: [Recommended Configuration]
```

## Scripts

- `scripts/optimization_reasoning.py` - Deterministic evaluation, state validation, and CLI tool for optimization-reasoning.

