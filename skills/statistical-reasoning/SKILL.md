---
name: statistical-reasoning
description: Applies statistical thinking, probability estimation, confidence intervals, and Bayesian updating to quantitative data.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Statistical Reasoning applies mathematical rigor to data interpretation, probability estimation, and decision making under uncertainty. It ensures that conclusions avoid common cognitive traps like base-rate neglect, sample size insensitivity, and regression to the mean.

## When to Use

- **Data Interpretation**: Analyzing benchmark results, metric changes, or experiment outcomes.
- **Bayesian Inference**: Updating prior beliefs when new quantitative evidence arrives.
- **Risk & Probability Modeling**: Estimating odds of failure or success across probabilistic outcomes.

## Execution Workflow

1. **State Prior Distribution ($P(A)$)**: Establish baseline probabilities based on historical data.
2. **Evaluate Likelihood ($P(B|A)$)**: Assess probability of observing the evidence given hypothesis $A$.
3. **Apply Bayes' Theorem**: Calculate posterior probability $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$.
4. **Determine Confidence Interval**: State margin of error and statistical significance level.

## Expected Output Contract

```markdown
### Statistical Assessment
- **Prior Probability P(A)**: [Baseline Rate]
- **Observed Likelihood P(B|A)**: [Evidence Probability]
- **Posterior Probability P(A|B)**: [Updated Rate]
- **Confidence Level**: [Significance Interval]
```

## Scripts

Python support omitted: Agent context window natively performs statistical reasoning without requiring external deterministic scripts.
