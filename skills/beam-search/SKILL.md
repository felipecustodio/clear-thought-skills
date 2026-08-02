---
name: beam-search
description: Evaluates multiple solution candidates in parallel, maintaining a fixed beam width of the top-k highest-scoring states at each step. Use for constrained optimization and decoding.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Beam Search is a heuristic search algorithm that explores a graph by expanding the most promising nodes in a limited set. It maintains a fixed number ($k$, the beam width) of the best candidate states at each level, preventing combinatorial explosion while offering broader exploration than greedy search.

## When to Use

- **Constrained Search Spaces**: When looking for an optimal sequence or configuration (e.g., prompt optimization, workflow synthesis, pathfinding).
- **Top-K Candidate Tracking**: When maintaining a strict limit on the number of active possibilities at any given step.
- **Resource-Constrained Exploration**: When Tree-of-Thought would generate too many unmanageable branches.

## When NOT to Use

- Problems where global context requires deep backtracking that exceeds the beam width.
- Single-path deterministic logic.

## Execution Workflow

1. **Configure Parameters**:
   - Set **Beam Width ($k$)**: Number of candidates to retain (typically $2 \le k \le 5$).
   - Set **Max Depth / Iterations**: Maximum depth of expansion.

2. **Initialize Candidates**:
   - Generate initial set of $k$ distinct candidate solutions for Step 1.

3. **Expand & Evaluate**:
   - For each candidate in the current beam, generate all valid next-step extensions.
   - Score each generated candidate extension using a scoring function.

4. **Select Top-K (Pruning)**:
   - Rank all expanded candidates across the entire beam.
   - Retain only the top $k$ highest-scoring candidates; discard all others.

5. **Termination & Selection**:
   - Repeat until maximum depth is reached or candidates satisfy complete solution criteria.
   - Return the single highest-scoring path.

## Expected Output Contract

```markdown
### Beam Search - Iteration [N]
- **Beam Width**: [k]
- **Top Candidates Retained**:
  1. **Candidate 1 [Score: X]**: [State Summary]
  2. **Candidate 2 [Score: Y]**: [State Summary]
- **Pruned Candidates Count**: [Count]
```

## Scripts

- `scripts/beam_search.py` - Deterministic evaluation, state validation, and CLI tool for beam-search.

## Gotchas

- If beam width is set too low ($k=1$), the search degenerates into greedy search and may get stuck in local optima.
