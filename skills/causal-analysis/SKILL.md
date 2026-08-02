---
name: causal-analysis
description: Identifies root causes and causal relationships using Five Whys, Cause-and-Effect Diagrams, and Counterfactual Reasoning.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Causal Analysis moves beyond superficial symptoms to isolate underlying root causes. It distinguishes between correlation and causation, helping agents prevent recurring failures by addressing foundational systemic issues.

## When to Use

- **Incident Post-Mortems**: Diagnosing production outages or major system bugs.
- **System Failure Diagnosis**: Distinguishing root causes from surface-level errors.
- **Policy & Process Improvements**: Understanding downstream effects of structural changes.

## Execution Workflow

1. **Symptom Mapping**: State the observed failure clearly.
2. **The 5 Whys Traversal**: Iteratively ask "Why did this occur?" down 5 levels of causality.
3. **Counterfactual Test**: Verify causality by asking: "If cause X was absent, would outcome Y still have occurred?".
4. **Root Cause Identification**: Isolate the foundational driver.
5. **Preventative Action**: Define corrective controls targeted directly at the root cause.

## Expected Output Contract

```markdown
### Causal Analysis Summary
- **Observed Symptom**: [Surface error]
- **Causal Chain (5 Whys)**:
  1. Why? -> [Direct Cause]
  2. Why? -> [Sub Cause]
  ...
  5. Why? -> [Root Cause]
- **Root Cause**: [Core Issue]
- **Preventative Action**: [Structural Fix]
```

## Scripts

Python support omitted: Agent context window natively executes causal analysis without requiring external deterministic scripts.
