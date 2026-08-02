---
name: optimization-reasoning
description: Use this skill for optimization.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- The user asks for optimization reasoning
- You need to perform optimization

## Workflow

1. Determine the parameters for the task.
2. Execute the necessary steps.
3. Run the script `scripts/optimization_reasoning.py` to validate or compute.
3. Format the final output for the user.

## Outputs

- A formatted response with reasoning and conclusions.

## Scripts

- `scripts/optimization_reasoning.py` - required for grid/search objective evaluation

## Gotchas

- Ensure all required parameters are provided.
