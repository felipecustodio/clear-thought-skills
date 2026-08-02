---
name: ooda-loop
description: Applies the Observe-Orient-Decide-Act (OODA) loop for rapid adaptive decision making in fast-changing or volatile environments.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

The OODA Loop (Observe, Orient, Decide, Act) is an iterative strategy framework developed by John Boyd. It emphasizes agility, rapid adaptation, and mental orientation updating when operating under dynamic, changing, or competitive conditions.

## When to Use

- **Rapidly Changing Environments**: Incident response, live debugging, real-time strategy adjustment.
- **Adaptive Execution**: When new information arrives continuously and invalidates old assumptions quickly.
- **Competitive & Adversarial Contexts**: Outmaneuvering fast-paced constraints or dynamic operational challenges.

## Execution Workflow

1. **Observe**:
   - Gather fresh raw data, current state indicators, logs, or system responses. Avoid premature interpretation.

2. **Orient**:
   - Contextualize data using existing mental models, past experience, and domain knowledge.
   - Update your internal situational model. Identify biases or outdated assumptions.

3. **Decide**:
   - Formulate a clear hypothesis or select the single best immediate action from available alternatives.

4. **Act**:
   - Execute the action rapidly to test the hypothesis or stabilize the environment.

5. **Loop**:
   - Immediately observe the outcome of the action and repeat the cycle.

## Expected Output Contract

```markdown
### OODA Loop Iteration
- **Observe**: [Fresh data & observations]
- **Orient**: [Updated mental model & context analysis]
- **Decide**: [Selected immediate action]
- **Act**: [Execution step & expected feedback]
```

## Scripts

- `scripts/ooda_loop.py` - Deterministic evaluation, state validation, and CLI tool for ooda-loop.

