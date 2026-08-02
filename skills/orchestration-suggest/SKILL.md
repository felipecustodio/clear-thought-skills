---
name: orchestration-suggest
description: Use this skill for orchestration-suggest.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- The user asks for orchestration suggest
- You need to perform orchestration-suggest

## Workflow

1. Determine the parameters for the task.
2. Execute the necessary steps.
3. Run the script `scripts/orchestration_suggest.py` to validate or compute.
3. Format the final output for the user.

## Outputs

- A formatted response with reasoning and conclusions.

## Scripts

- `scripts/orchestration_suggest.py` - merge alias into same skill

## Gotchas

- Ensure all required parameters are provided.
