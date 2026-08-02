---
name: causal-analysis
description: Use this skill for causal_analysis.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- The user asks for causal analysis
- You need to perform causal_analysis

## Workflow

1. Determine the parameters for the task.
2. Execute the necessary steps.
3. Run the script `scripts/causal_analysis.py` to validate or compute.
3. Format the final output for the user.

## Outputs

- A formatted response with reasoning and conclusions.

## Scripts

- `scripts/causal_analysis.py` - required for graph/intervention checks

## Gotchas

- Ensure all required parameters are provided.
