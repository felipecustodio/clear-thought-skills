---
name: code-execution-reasoning
description: Use this skill for code-execution.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- The user asks for code execution reasoning
- You need to perform code-execution

## Workflow

1. Determine the parameters for the task.
2. Execute the necessary steps.
3. Run the script `scripts/code_execution_reasoning.py` to validate or compute.
3. Format the final output for the user.

## Outputs

- A formatted response with reasoning and conclusions.

## Scripts

- `scripts/code_execution_reasoning.py` - required sandbox runner

## Gotchas

- Ensure all required parameters are provided.
