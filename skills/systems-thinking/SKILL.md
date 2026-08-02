---
name: systems-thinking
description: Analyzes complex systems by examining feedback loops, delays, use points, and full interconnections.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Systems Thinking treats problems as parts of an overall system rather than isolated events. It identifies reinforcing and balancing feedback loops, latency delays, and high-use intervention points.

## When to Use

- **Complex System Architecture**: Distributed systems, microservices, organizational dynamics.
- **Unintended Consequences**: Preventing fixes that create bigger downstream problems.

## Execution Workflow

1. **System Boundary Definition**: Identify key components, inputs, and outputs of the system.
2. **Feedback Loop Mapping**:
   - **Reinforcing Loops ($R$)**: Exponential growth or compounding effects.
   - **Balancing Loops ($B$)**: Stabilizing or equilibrium-seeking loops.
3. **Identify Delays**: Locate time lags between actions and system responses.
4. **Find High-use Points**: Identify small changes that produce fundamental system improvements.

## Expected Output Contract

```markdown
### Systems Analysis
- **System Components**: [Key Entities]
- **Feedback Loops**:
  - `Loop 1 (R)`: [Compounding loop description]
  - `Loop 2 (B)`: [Stabilizing loop description]
- **System Delays**: [Latency points]
- **use Point**: [Recommended intervention point]
```

## Scripts

- `scripts/systems_thinking.py` - Deterministic evaluation, state validation, and CLI tool for systems-thinking.

