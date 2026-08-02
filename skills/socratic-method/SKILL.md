---
name: socratic-method
description: Uses disciplined, probing questions to uncover underlying assumptions, test reasoning logic, and guide conceptual understanding.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

The Socratic Method employs targeted questioning to challenge assumptions, clarify concepts, and guide users or reasoning processes toward deeper self-correction.

## When to Use

- **Clarifying Requirements**: Uncovering hidden assumptions or ambiguous requests from users.
- **Educational Guidance**: Leading users to discover solutions independently through guided questions.

## Execution Workflow

1. **Identify Premise**: State the user's initial assertion or assumption.
2. **create Probing Questions**:
   - *Conceptual Clarification*: "What exactly do we mean by X?"
   - *Probing Assumptions*: "What are we assuming here?"
   - *Probing Evidence*: "What evidence supports this?"
   - *Alternative Perspectives*: "What is the counter-argument?"
   - *Exploring Consequences*: "If this is true, what follows?"
3. **Refine Concept**: Synthesize answers into a clearer, error-free proposition.

## Expected Output Contract

```markdown
### Socratic Dialog / Probe
- **Target Premise**: [Initial Statement]
- **Probing Questions**:
  1. [Clarification question]
  2. [Assumption challenge]
- **Refined Understanding**: [Deeper Conclusion]
```

## Scripts

- `scripts/socratic_method.py` - Deterministic evaluation, state validation, and CLI tool for socratic-method.

