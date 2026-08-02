---
name: session-import
description: Use this skill for session_import.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- The user asks for session import
- You need to perform session_import

## Workflow

1. Determine the parameters for the task.
2. Execute the necessary steps.
3. Run the script `scripts/session_import.py` to validate or compute.
3. Format the final output for the user.

## Outputs

- A formatted response with reasoning and conclusions.

## Scripts

- `scripts/session_import.py` - required explicit JSON import helper

## Gotchas

- Ensure all required parameters are provided.
