---
name: structured-argumentation
description: Challenges the truth of the underlying premises
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- The user asks for structured argumentation
- You need to perform structured_argumentation

## Workflow

1. Determine the parameters for the task.
2. Execute the necessary steps.
3. Run the script `scripts/structured_argumentation.py` to validate or compute.
3. Format the final output for the user.

## Outputs

- A formatted response with reasoning and conclusions.

## Scripts

Python support omitted: Agent context window natively tracks this state without requiring external deterministic scripts.

## Gotchas

- Ensure all required parameters are provided.
