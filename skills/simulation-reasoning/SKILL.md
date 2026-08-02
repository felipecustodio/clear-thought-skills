---
name: simulation-reasoning
description: Use this skill for simulation.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Use When

- The user asks for simulation reasoning
- You need to perform simulation

## Workflow

1. Determine the parameters for the task.
2. Execute the necessary steps.
3. Run the script `scripts/simulation_reasoning.py` to validate or compute.
3. Format the final output for the user.

## Outputs

- A formatted response with reasoning and conclusions.

## Scripts

Python support omitted: Agent context window natively tracks this state without requiring external deterministic scripts.

## Gotchas

- Ensure all required parameters are provided.
