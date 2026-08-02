---
name: mdp-planning
description: Use this skill for mdp_planning.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- The user asks for mdp planning
- You need to perform mdp_planning

## Workflow

1. Determine the parameters for the task.
2. Execute the necessary steps.
3. Run the script `scripts/mdp_planning.py` to validate or compute.
3. Format the final output for the user.

## Outputs

- A formatted response with reasoning and conclusions.

## Scripts

- `scripts/mdp_planning.py` - required for value/policy iteration

## Gotchas

- Ensure all required parameters are provided.
