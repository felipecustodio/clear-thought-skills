---
name: session-export
description: Use this skill for session_export.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- The user asks for session export
- You need to perform session_export

## Workflow

1. Determine the parameters for the task.
2. Execute the necessary steps.
3. Run the script `scripts/session_export.py` to validate or compute.
3. Format the final output for the user.

## Outputs

- A formatted response with reasoning and conclusions.

## Scripts

- `scripts/session_export.py` - required explicit JSON export helper

## Gotchas

- Ensure all required parameters are provided.
