---
name: structured-argumentation
description: Constructs formal logical arguments using Claim, Data, Warrant, Backing, Counter-argument, and Rebuttal (Toulmin Model).
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Structured Argumentation applies formal argument frameworks (e.g., Toulmin Model) to build persuasive, sound, and objective technical proposals while explicitly addressing counter-arguments.

## When to Use

- **RFCs & Technical Proposals**: Pitching new architecture or technology adoption.
- **Debate & Position Papers**: Defending strategic technical choices against skepticism.

## Execution Workflow

1. **Claim**: State the core assertion clearly.
2. **Data / Evidence**: Present verifiable facts, metrics, or benchmark data supporting the claim.
3. **Warrant**: Explain the logical connection linking the data to the claim.
4. **Counter-Argument**: Explicitly present the strongest opposing view.
5. **Rebuttal / Qualification**: Address the counter-argument and state constraints under which the claim holds true.

## Expected Output Contract

```markdown
### Toulmin Argument Structure
- **Claim**: [Core Assertion]
- **Data**: [Empirical Evidence]
- **Warrant**: [Logical Bridge]
- **Counter-Argument**: [Opposing View]
- **Rebuttal**: [Refutation / Boundary Conditions]
```

## Scripts

Python support omitted: Agent context window natively constructs structured arguments without requiring external deterministic scripts.
