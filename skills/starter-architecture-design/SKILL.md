---
name: starter-architecture-design
description: "Starter skill for end-to-end software architecture design. Orchestrates requirement probing, systems analysis, tree-of-thought exploration, boundary setting, and visual diagramming."
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

starter-architecture-design acts as an automated starter orchestration pipeline. It chains together the ideal combination of reasoning skills for high-level tasks, ensuring structured execution without manual skill routing.

## Execution Workflow

1. **Probe Requirements (`socratic-method`)**: Uncover hidden assumptions, latency targets, and scalability requirements.
2. **System Mapping (`systems-thinking`)**: Identify feedback loops, system dependencies, and potential bottlenecks.
3. **Explore Architectural Options (`tree-of-thought`)**: Compare competing architectures (e.g. Microservices vs Monolith) with heuristic scoring.
4. **Enforce Boundary Limits (`ulysses-protocol`)**: Establish strict scope limits and stopping criteria.
5. **Render Architecture (`visual-reasoning`)**: Generate a Mermaid flowchart and sequence diagram.

## Expected Output Contract

```markdown
### Starter Workflow Execution: [starter-architecture-design]
- **Phase 1 Output**: [Initial Analysis]
- **Phase 2 Output**: [Detailed Evaluation]
- **Final Synthesized Solution**: [Complete Recommendation]
```

## Scripts

- `scripts/starter_architecture_design.py` - Orchestration helper and state validation tool for starter-architecture-design.

## Gotchas

- Ensure all sub-skill prerequisites are satisfied before executing downstream pipeline steps.
