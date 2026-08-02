---
name: monte-carlo-tree-search
description: Performs stochastic decision-making and search space exploration using Selection, Expansion, Simulation (Rollout), and Backpropagation. Use for high-uncertainty decision scenarios.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Monte Carlo Tree Search (MCTS) is a heuristic search algorithm for decision-making processes in complex, uncertain, or highly combinatorial environments. It balances exploration (trying unvisited paths) and exploitation (deepening promising paths) using Upper Confidence Bound for Trees (UCT).

## When to Use

- **High Uncertainty Decisions**: Scenarios with probabilistic outcomes or incomplete information.
- **Complex Strategic Games/Planning**: Multi-agent negotiations, competitive strategies, or deep tactical planning.
- **Exploration vs Exploitation**: When you need to avoid bias towards early-favored options and systematically explore under-visited options.

## Execution Workflow

1. **Selection**:
   - Starting at the root node, navigate down the tree using the UCT formula:
     $$	ext{UCT} = rac{w_i}{n_i} + c \sqrt{rac{\ln N}{n_i}}$$
     Select child nodes that maximize this balance of win rate and exploration incentive.

2. **Expansion**:
   - Upon reaching an unexpanded leaf node, create one or more child nodes representing potential next actions.

3. **Simulation (Rollout)**:
   - From the newly expanded node, perform a lightweight mental simulation (rollout) to estimate downstream outcome quality.

4. **Backpropagation**:
   - Propagate the simulation result back up through the visited nodes, updating visit counts ($n_i$) and accumulated value/rewards ($w_i$).

5. **Decision**:
   - After $N$ simulation rounds, select the action corresponding to the child node with the highest visit count or highest expected reward.

## Expected Output Contract

```markdown
### MCTS Simulation Summary
- **Total Simulations Run**: [N]
- **Node Statistics**:
  - **Node A**: Visits: [n], Value/Win Rate: [w/n], UCT Score: [score]
  - **Node B**: Visits: [n], Value/Win Rate: [w/n], UCT Score: [score]
- **Recommended Action**: [Action with highest visit density / expected value]
```

## Scripts

- `scripts/monte_carlo_tree_search.py` - Deterministic evaluation, state validation, and CLI tool for monte-carlo-tree-search.

## Gotchas

- Ensure the exploration constant $c$ is tuned appropriately ($c pprox 1.414$ by default). Higher values force more exploration of untried branches.
