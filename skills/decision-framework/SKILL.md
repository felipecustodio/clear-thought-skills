---
name: decision-framework
description: Evaluates choices systematically using multi-criteria decision analysis (MCDA), weighted scoring matrices, and risk profiles.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Decision Framework structures complex choices with multiple competing options and criteria. It eliminates subjective bias by using weighted decision matrices and risk-reward scoring.

## When to Use

- **Technology Selection**: Choosing between frameworks, databases, or vendors.
- **Strategic Prioritization**: Evaluating features, projects, or architectural directions.

## Execution Workflow

1. **Define Options**: List candidate choices ($O_1, O_2, \dots, O_m$).
2. **Establish Criteria & Weights**: Define evaluation criteria ($C_1, C_2, \dots, C_n$) and assign weights ($\sum w_i = 1.0$).
3. **Score Candidates**: Score each option on a 1-10 scale for each criterion.
4. **Calculate Weighted Scores**: Total Score $= \sum (Score_{ij} \times w_j)$.
5. **Recommendation**: Recommend the highest-scoring option with sensitivity analysis.

## Expected Output Contract

```markdown
### Decision Matrix
| Criterion (Weight) | Option A | Option B | Option C |
| :--- | :--- | :--- | :--- |
| Performance (0.4) | 8 (3.2) | 6 (2.4) | 9 (3.6) |
| Cost (0.3) | 7 (2.1) | 9 (2.7) | 5 (1.5) |
| **Total Score** | **5.3** | **5.1** | **5.1** |

**Winning Choice**: Option A
```

## Scripts

- `scripts/decision_framework.py` - Deterministic evaluation, state validation, and CLI tool for decision-framework.

