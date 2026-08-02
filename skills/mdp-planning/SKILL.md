---
name: mdp-planning
description: Formulates sequential decision-making problems as Markov Decision Processes (MDPs) with states, actions, transition probabilities, and rewards.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

MDP Planning models environments where outcomes are partly random and partly under the control of a decision maker. It uses Bellman equations to compute optimal policies ($\pi^*$).

## When to Use

- **Sequential Decision Making under Uncertainty**: Robotics, automated trading, adaptive workflows.
- **Policy Optimization**: Finding the best action for every possible state of a system.

## Execution Workflow

1. **Define MDP Tuple $(S, A, P, R, \gamma)$**:
   - $S$: Set of states.
   - $A$: Set of actions.
   - $P(s'|s, a)$: Transition probability matrix.
   - $R(s, a)$: Reward function.
   - $\gamma$: Discount factor ($0 \le \gamma < 1$).
2. **Compute Value Function $V(s)$**: Use Value Iteration or Policy Iteration ($V(s) = \max_a [R(s, a) + \gamma \sum P(s'|s, a)V(s')]$).
3. **Extract Optimal Policy ($\pi^*$)**: Recommend the optimal action for the current state.

## Expected Output Contract

```markdown
### MDP Planning Summary
- **State Space S**: [State Definitions]
- **Action Space A**: [Available Actions]
- **Optimal Policy π***:
  - `State S1` -> `Action A1`
  - `State S2` -> `Action A2`
- **Expected Discounted Reward**: [Value V(S)]
```

## Scripts

Python support omitted: Agent context window natively executes MDP planning without requiring external deterministic scripts.
