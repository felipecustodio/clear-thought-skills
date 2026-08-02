---
name: collaborative-reasoning
description: Coordinates multi-agent or multi-persona perspectives (e.g. Architect, Security Engineer, Product Manager) to achieve consensus.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Collaborative Reasoning models multi-perspective discussions by simulating specialized domain experts (e.g. Security Specialist, Performance Engineer, UX Designer) to evaluate solutions holistically.

## When to Use

- **Cross-Functional Architecture Reviews**: Evaluating software designs across security, scalability, and developer experience.
- **Consensus Building**: Resolving conflicting priorities among stakeholders.

## Execution Workflow

1. **Define Expert Personas**: Assign distinct roles (e.g., `Persona A: Security Lead`, `Persona B: Systems Architect`).
2. **Independent Persona Analysis**: Generate feedback from each persona's strict domain perspective.
3. **Identify Conflicts & Trade-offs**: Highlight where persona priorities clash (e.g. security vs convenience).
4. **Synthesize Consensus**: Negotiate a balanced solution addressing key concerns from all personas.

## Expected Output Contract

```markdown
### Multi-Persona Panel Review
- **Perspectives**:
  - `Security Lead`: [Domain Feedback]
  - `Architecture Lead`: [Domain Feedback]
- **Identified Clashes**: [Conflict Summary]
- **Consensus Recommendation**: [Harmonized Solution]
```

## Scripts

- `scripts/collaborative_reasoning.py` - Deterministic evaluation, state validation, and CLI tool for collaborative-reasoning.

