---
name: tree-of-thought
description: Explores multiple reasoning paths simultaneously using tree search strategies (DFS/BFS). Use when evaluating competing hypotheses, decision trees, or multi-branch exploration scenarios.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Tree of Thought (ToT) enables the agent to evaluate multiple distinct reasoning pathways in parallel. Unlike linear sequential thinking, ToT maintains a tree structure of thoughts, allowing the agent to explore different solution branches, evaluate their promise via heuristics/scores, and backtrack from non-viable branches.

## When to Use

- **Branching Decision Trees**: Problems with distinct alternative choices (e.g., architectural choices, algorithm selection).
- **Exploration & Backtracking**: Complex puzzle solving, strategic planning, or system optimization where early choices lock in downstream constraints.
- **Comparative Evaluation**: When you need to systematically compare 3+ competing approaches before selecting the best solution.

## When NOT to Use

- Simple sequential tasks with a single clear path forward.
- Direct factual queries.

## Execution Workflow

1. **Root Node Definition**:
   - Define the root problem state and establish evaluation criteria (e.g., feasibility, complexity, risk, performance).

2. **Branch Generation (Expansion)**:
   - From the current node, generate $K$ distinct candidate thoughts/sub-solutions (branches).
   - Label branches clearly (e.g., `Branch A: Microservice Architecture`, `Branch B: Monolith with Event Bus`).

3. **Evaluation & Scoring**:
   - Assess each branch independently against the established criteria.
   - Assign a heuristic score or feasibility index ($0.0$ to $1.0$).

4. **Search Strategy Execution**:
   - **Depth-First Search (DFS)**: Deeply evaluate Branch A down to its outcome before evaluating Branch B. Backtrack if Branch A drops below threshold.
   - **Breadth-First Search (BFS)**: Evaluate level 1 of all branches simultaneously before expanding to level 2.

5. **Pruning & Selection**:
   - Prune (discard) low-scoring branches.
   - Select the winning branch and provide full rationale.

## Expected Output Contract

```markdown
### Tree Evaluation Summary
- **Current Depth**: [Depth Level]
- **Active Branches**:
  - **Branch 1 [Score: X/10]**: [Description & Feasibility]
  - **Branch 2 [Score: Y/10]**: [Description & Feasibility]
- **Action**: [Expand / Prune / Backtrack / Select Winner]
```

## Scripts

Python support omitted: Agent context window natively tracks this tree structure and heuristic evaluation without requiring external deterministic scripts.

## Gotchas

- Avoid generating too many fine-grained branches simultaneously; keep branch factor between 2 and 4 to maintain focus.
- Always establish objective scoring criteria before evaluating branches to avoid confirmation bias.
