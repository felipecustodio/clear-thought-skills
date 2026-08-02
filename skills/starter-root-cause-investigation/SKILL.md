---
name: starter-root-cause-investigation
description: "Starter skill for incident post-mortems and deep scientific investigations. Orchestrates 5-Whys causal analysis, empirical hypothesis testing, and simulation modeling."
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

starter-root-cause-investigation acts as an automated starter orchestration pipeline. It chains together the ideal combination of reasoning skills for high-level tasks, ensuring structured execution without manual skill routing.

## Execution Workflow

1. **Execute 5-Whys Traversal (`causal-analysis`)**: Map symptoms back to fundamental root causes using counterfactual testing.
2. **Empirical Hypothesis Testing (`scientific-method`)**: Formulate falsifiable hypotheses, design experiments, and record findings.
3. **Simulate Dynamic Behavior (`simulation-reasoning`)**: Model system behavior over time under seed conditions to observe emergent failures.
4. **Self-Audit Reasoning (`metacognitive-monitoring`)**: Perform real-time bias detection to ensure conclusions are grounded strictly in evidence.

## Expected Output Contract

```markdown
### Starter Workflow Execution: [starter-root-cause-investigation]
- **Phase 1 Output**: [Initial Analysis]
- **Phase 2 Output**: [Detailed Evaluation]
- **Final Synthesized Solution**: [Complete Recommendation]
```

## Scripts

- `scripts/starter_root_cause_investigation.py` - Orchestration helper and state validation tool for starter-root-cause-investigation.

## Gotchas

- Ensure all sub-skill prerequisites are satisfied before executing downstream pipeline steps.
