---
name: metacognitive-monitoring
description: Evaluates the agent's own reasoning process in real time, detecting cognitive biases, confidence drift, and logical gaps.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Metacognitive Monitoring is "thinking about thinking." It provides real-time self-assessment of the agent's own cognitive state, identifying overconfidence, confirmation bias, or drift away from original user constraints.

## When to Use

- **Self-Correction Loops**: Mid-task checks during long, multi-step agent workflows.
- **Bias Detection**: Ensuring recommendations aren't biased toward early assumptions.

## Execution Workflow

1. **Evaluate Current Confidence Level**: Rate confidence (0.0 to 1.0) in the current line of reasoning.
2. **Audit for Cognitive Biases**:
   - *Confirmation Bias*: Am I ignoring contradictory evidence?
   - *Anchoring*: Am I overly fixated on the first solution considered?
   - *Sunk Cost*: Am I continuing down a bad path just because I spent time on it?
3. **Assess Goal Drift**: Compare current sub-task against original user prompt requirements.
4. **Course Correction**: Adjust strategy if confidence drops or drift is detected.

## Expected Output Contract

```markdown
### Metacognitive Self-Audit
- **Confidence Index**: [0.0 - 1.0]
- **Detected Biases**: [None / Identified Bias]
- **Goal Alignment Check**: [On Track / Drifted]
- **Corrective Action**: [Continue / Adjust Focus / Pivot Strategy]
```

## Scripts

Python support omitted: Agent context window natively performs metacognitive monitoring without requiring external deterministic scripts.
