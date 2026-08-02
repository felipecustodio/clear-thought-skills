---
name: starter-strategic-decision
description: "Starter skill for multi-criteria strategic decision making, tech stack selection, and vendor evaluation. Orchestrates decision matrices, probability modeling, ethical checks, and panel reviews."
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

starter-strategic-decision acts as an automated starter orchestration pipeline. It chains together the ideal combination of reasoning skills for high-level tasks, ensuring structured execution without manual skill routing.

## Execution Workflow

1. **Construct Decision Matrix (`decision-framework`)**: Define candidate choices, criteria, and weighted scoring models.
2. **Probabilistic Evaluation (`statistical-reasoning`)**: Estimate baseline probabilities, expected utility, and confidence intervals.
3. **Ethics & Compliance Check (`ethical-analysis`)**: Assess privacy, data safety, and fairness across Utilitarian and Deontological lenses.
4. **Multi-Persona Panel Review (`collaborative-reasoning`)**: Evaluate consensus across Security, Performance, and Product personas.

## Expected Output Contract

```markdown
### Starter Workflow Execution: [starter-strategic-decision]
- **Phase 1 Output**: [Initial Analysis]
- **Phase 2 Output**: [Detailed Evaluation]
- **Final Synthesized Solution**: [Complete Recommendation]
```

## Scripts

- `scripts/starter_strategic_decision.py` - Orchestration helper and state validation tool for starter-strategic-decision.

## Gotchas

- Ensure all sub-skill prerequisites are satisfied before executing downstream pipeline steps.
