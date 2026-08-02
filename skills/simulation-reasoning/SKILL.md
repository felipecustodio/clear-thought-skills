---
name: simulation-reasoning
description: Simulates complex system behaviors over time under varying initial conditions or agent interactions.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Simulation Reasoning conducts step-by-step dynamic modeling of complex systems to observe emergent behavior, identify tipping points, and evaluate long-term outcomes under synthetic conditions.

## When to Use

- **Complex Dynamic Systems**: Queueing systems, load behavior under traffic bursts, concurrency race conditions.
- **Scenario Planning**: Simulating multi-agent market conditions, adoption curves, or failure cascades.

## Execution Workflow

1. **Define State Variables & Rules**: Establish system entities, parameters, and transition rules.
2. **Initialize Simulation**: Set initial seed conditions and time-step size ($\Delta t$).
3. **Step Through Epochs**: Execute state transitions iteratively over $N$ time steps.
4. **Analyze Emergent Patterns**: Identify bottlenecks, steady states, or catastrophic failure modes.

## Expected Output Contract

```markdown
### Simulation Results
- **Initial Conditions**: [Seed Parameters]
- **Execution Horizon**: [N Time Steps]
- **Key Metrics over Time**: [Summary Table / Stats]
- **Emergent Insights**: [System Behavior Analysis]
```

## Scripts

- `scripts/simulation_reasoning.py` - Deterministic evaluation, state validation, and CLI tool for simulation-reasoning.

