---
name: pdr-reasoning
description: Implements Predict-Disrupt-Reflect (PDR) reasoning to stress-test plans, identify hidden failure modes, and build resilient strategies.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Predict-Disrupt-Reflect (PDR) is a adversarial reasoning protocol designed to combat optimism bias and build bulletproof strategies. It forces the agent to explicitly predict an outcome, actively try to disrupt/break the prediction with worst-case scenarios, and reflect to refine the strategy.

## When to Use

- **Plan Validation & Risk Assessment**: Before deploying critical code, database migrations, or major architectural changes.
- **Adversarial Red-Teaming**: Identifying edge cases, security vulnerabilities, or single points of failure.
- **High-Stakes Decision Making**: Where failure carries high costs and mitigation must be built in up front.

## Execution Workflow

1. **Predict (Base Strategy)**:
   - State the proposed plan, expected sequence of events, and intended successful outcome.

2. **Disrupt (Red Team Attack)**:
   - Introduce severe disruption scenarios: "What if the DB times out?", "What if memory spikes?", "What if an unexpected input is received?".
   - Actively attempt to break the plan.

3. **Reflect & Harden**:
   - Analyze how the plan failed under disruption.
   - Modify the plan to incorporate fallback mechanisms, circuit breakers, and contingency paths.

## Expected Output Contract

```markdown
### PDR Strategy Stress-Test
- **Prediction**: [Proposed plan and intended outcome]
- **Disruption Scenarios**:
  - *Disruption 1*: [Failure vector] -> *Impact*: [Severity]
- **Reflection & Mitigation**: [Hardened plan incorporating safeguards]
```

## Scripts

Python support omitted: Agent context window natively executes PDR stress-testing without requiring external deterministic scripts.
