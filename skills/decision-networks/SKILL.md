---
name: decision-networks
description: Models complex probabilistic decisions with utility nodes using Influence Diagrams and Decision Networks.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Decision Networks extend Bayesian networks by incorporating decision nodes and utility nodes. They help agents compute expected utilities of decisions under uncertain environment states.

## When to Use

- **Decisions under Uncertainty**: When actions have uncertain outcomes with distinct financial/operational utilities.
- **Risk vs Reward Optimization**: Balancing high-risk/high-reward paths against safe/low-reward paths.

## Execution Workflow

1. **Define Chance Nodes**: Uncertain state variables in the environment.
2. **Define Decision Nodes**: Specific choices under agent control.
3. **Define Utility Nodes**: Quantifiable payoff or loss functions.
4. **Compute Expected Utility (EU)**: $\text{EU}(D) = \sum P(S|D) \times U(S, D)$.
5. **Select Maximum Utility Action**: Choose decision $D^*$ maximizing $\text{EU}(D)$.

## Expected Output Contract

```markdown
### Decision Network Analysis
- **Decision Nodes**: [Available Choices]
- **Chance Nodes**: [Uncertain State Probabilities]
- **Expected Utility**:
  - `Choice A`: Expected Utility = X
  - `Choice B`: Expected Utility = Y
- **Optimal Choice**: [Choice with Max EU]
```

## Scripts

Python support omitted: Agent context window natively models decision networks without requiring external deterministic scripts.
