---
name: sequential-thinking
description: A detailed, step-by-step reasoning process for dynamic, reflective problem-solving. Use when tackling complex, multi-stage problems that require hypothesis revision, thought branching, and continuous re-evaluation.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Sequential Thinking is a step-by-step method for complex problem solving. It allows the AI agent to explicitly trace its internal reasoning steps, evaluate intermediate conclusions, adjust assumptions on the fly, and dynamically branch or revise previous thoughts when new evidence or edge cases emerge.

## When to Use

- **Multi-step Problem Solving**: When a request cannot be answered safely or accurately in a single step.
- **Hypothesis Testing & Refinement**: When initial assumptions might be wrong or need iterative validation.
- **Uncertainty & Ambiguity**: When working through complex math, algorithm design, architecture planning, or debugging.
- **Thought Revision**: When you realize a previous line of reasoning contained an error or overlooked a constraint.

## When NOT to Use

- Simple factual lookup or straightforward direct questions.
- Basic code formatting or syntax conversion tasks.

## Execution Workflow

1. **Initialize Step Context**:
   - Begin with `Thought 1`. Define the scope of the problem and state initial assumptions explicitly.
   - Outline the total estimated number of steps required, while acknowledging this number can adjust dynamically.

2. **Iterative Progression**:
   - For each step (`Thought N`):
     - State the primary objective of this specific thought.
     - Execute the cognitive analysis, computation, or verification.
     - Check for flaws, false assumptions, or missing requirements.

3. **Branching & Revisions (As Needed)**:
   - **Revision**: If Thought N invalidates Thought N-K, explicitly flag a revision: `[Revises Thought N-K]`. State what changed and why.
   - **Branching**: If multiple viable paths exist (e.g., Solution A vs. Solution B), create a branch context `[Branch ID: X, From Thought: Y]` to explore alternative hypotheses safely.

4. **Verification & Convergence**:
   - Determine if `nextThoughtNeeded` is true or false.
   - Once all branches converge or the optimal path is confirmed, summarize the final solution with high confidence.

## Expected Output Contract

Always present your sequential thinking clearly using structured blocks:

```markdown
### Thought [Number] / [Total Estimated]
- **Objective**: [What is being evaluated or solved in this step]
- **Analysis**: [Detailed reasoning process]
- **Self-Correction / Notes**: [Any identified risks, revisions, or branching context]
- **Status**: [Continue / Revise / Finalize]
```

## Scripts

- `scripts/sequential_thinking.py` - Deterministic evaluation, state validation, and CLI tool for sequential-thinking.

## Gotchas

- Do not rush to set `nextThoughtNeeded: false` until all edge cases and edge constraints have been systematically validated.
- Ensure revision thoughts explicitly state which prior thought number is being revised to maintain a clean context graph.
