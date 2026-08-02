---
name: beam-search
description: Use this skill for beam_search.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- The user asks for beam search
- You need to perform beam_search

## Workflow

1. Determine the parameters for the task.
2. Execute the necessary steps.
3. Run the script `scripts/beam_search.py` to validate or compute.
3. Format the final output for the user.

## Outputs

- A formatted response with reasoning and conclusions.

## Scripts

- `scripts/beam_search.py` - required for beam expansion/ranking

## Gotchas

- Ensure all required parameters are provided.
