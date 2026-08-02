---
name: session-info
description: Use this skill for session_info.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- The user asks for session info
- You need to perform session_info

## Workflow

1. Determine the parameters for the task.
2. Execute the necessary steps.
3. Run the script `scripts/session_info.py` to validate or compute.
3. Format the final output for the user.

## Outputs

- A formatted response with reasoning and conclusions.

## Scripts

- `scripts/session_info.py` - required local session inspection helper

## Gotchas

- Ensure all required parameters are provided.
