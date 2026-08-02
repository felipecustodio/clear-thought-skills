---
name: analogical-reasoning
description: Transfers insights, principles, and structural patterns from a familiar source domain to an unfamiliar target domain.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Analogical Reasoning maps structural relationships from a well-understood source domain to solve novel problems in a target domain. It enables creative cross-domain problem solving and intuitive explanations.

## When to Use

- **Novel Problem Solving**: Applying proven architecture patterns (e.g., assembly line) to new fields (e.g., software CI/CD pipelines).
- **Simplifying Complex Concepts**: Explaining abstract technical systems using intuitive real-world analogs.

## Execution Workflow

1. **Identify Target Domain**: Define the problem or concept that needs solving/explanation.
2. **Select Source Domain**: Identify a familiar domain sharing deep structural similarities (not surface similarities).
3. **Map Structural Relationships**: Align elements of Source $\to$ Target ($A \to X, B \to Y$).
4. **Transfer Insights**: Apply known solutions from the source to generate hypotheses for the target.
5. **Validate Limits**: Identify where the analogy breaks down to avoid false equivalences.

## Expected Output Contract

```markdown
### Analogical Transfer
- **Source Domain**: [Familiar System]
- **Target Domain**: [Novel Problem]
- **Structural Mapping**:
  - `Source Concept A` -> `Target Concept X`
- **Inferred Solution**: [Transferred Insight]
- **Analogy Breakdown / Limitations**: [Where analogy fails]
```

## Scripts

- `scripts/analogical_reasoning.py` - Deterministic evaluation, state validation, and CLI tool for analogical-reasoning.

