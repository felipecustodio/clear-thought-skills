---
name: ethical-analysis
description: Evaluates decisions through major ethical frameworks (Utilitarianism, Deontology, Virtue Ethics, Rights-Based Ethics).
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Ethical Analysis evaluates actions and technical implementations for moral compliance, fairness, user privacy, and societal impact using established philosophical ethical frameworks.

## When to Use

- **Data Privacy & AI Governance**: Evaluating data usage, user tracking, or AI model safety.
- **Policy & System Safety**: Assessing impact of automated actions on users, accessibility, and fairness.

## Execution Workflow

1. **Utilitarian Assessment**: Evaluate consequences — which action maximizes net benefit for the greatest number?
2. **Deontological Assessment**: Evaluate duties & rules — does the action violate core moral rules, consent, or laws regardless of outcome?
3. **Rights & Fairness Assessment**: Does the decision treat individuals equitably and respect fundamental rights?
4. **Synthesis & Mitigation**: create a resolution balancing ethical duties and maximizing positive outcomes.

## Expected Output Contract

```markdown
### Ethical Evaluation
- **Utilitarian Perspective**: [Consequence Analysis]
- **Deontological Perspective**: [Duty & Rules Analysis]
- **Fairness & Rights**: [Rights & Equity Assessment]
- **Ethical Recommendation**: [Balanced Ethical Recommendation]
```

## Scripts

- `scripts/ethical_analysis.py` - Deterministic evaluation, state validation, and CLI tool for ethical-analysis.

