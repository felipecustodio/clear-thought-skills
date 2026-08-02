---
name: pdr-reasoning
description: Use this skill for pdr-reasoning.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- The user asks for pdr reasoning
- You need to perform pdr-reasoning

## Workflow

1. Determine the parameters for the task.
2. Execute the necessary steps.
3. Run the script `scripts/pdr_reasoning.py` to validate or compute.
3. Format the final output for the user.

## Outputs

- A formatted response with reasoning and conclusions.

## Scripts

- `scripts/pdr_reasoning.py` - required PDR graph algorithms

## Gotchas

- Ensure all required parameters are provided.
