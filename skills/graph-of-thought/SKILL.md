---
name: graph-of-thought
description: Models complex problem solving as a Directed Acyclic Graph (DAG) of thoughts, enabling node aggregation, transformation, refinement, and non-linear network reasoning.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Graph of Thought (GoT) extends beyond tree structures by representing thoughts as vertices in a Directed Acyclic Graph (DAG). This allows operations like combining multiple independent lines of reasoning (aggregation), refining existing thoughts, and forming feedback loops or complex dependencies between distinct ideas.

## When to Use

- **Non-linear Problems**: Complex dependency networks, multi-perspective synthesis, or system integrations.
- **Thought Aggregation**: Combining outputs from 2+ distinct sub-analyses into a unified synthesis node.
- **Iterative Refinement Graphs**: When an idea needs feedback or inputs from multiple prior stages simultaneously.

## Execution Workflow

1. **Define Graph Vertices (Nodes)**:
   - Identify discrete units of reasoning or hypotheses as nodes ($V_1, V_2, \dots, V_n$).

2. **Establish Directed Edges (Dependencies)**:
   - Connect nodes with directional edges indicating dependencies ($V_i \to V_j$).

3. **Perform Graph Transformations**:
   - **Aggregation**: Merge insights from $V_a$ and $V_b$ into $V_{combined}$.
   - **Refinement**: Pass $V_i$ through a critique node to produce $V_{improved}$.
   - **Branching**: Split $V_i$ into sub-hypotheses $V_{i1}$ and $V_{i2}$.

4. **Evaluate Topological Order**:
   - Process nodes according to topological dependencies to synthesize final conclusions.

## Expected Output Contract

```markdown
### Graph of Thought Representation
- **Nodes**:
  - `Node A`: [Premise / Initial Finding]
  - `Node B`: [Independent Finding]
  - `Node C (Aggregated)`: [Merged insight from A + B]
- **Edges**: `A -> C`, `B -> C`
- **Graph State**: [Topological Execution / Synthesis Summary]
```

## Scripts

Python support omitted: Agent context window natively tracks graph topologies without requiring external deterministic scripts.
