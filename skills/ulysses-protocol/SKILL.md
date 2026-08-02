---
name: ulysses-protocol
description: Applies pre-commitment mechanisms and strict constraint bounds (Ulysses Contracts) to prevent self-sabotage, scope creep, or decision paralysis.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

The Ulysses Protocol enforces pre-commitment mechanisms (named after Ulysses tying himself to the mast to resist the Sirens). It is used to lock in boundaries, execution limits, and strict stopping rules before engaging in tasks prone to scope creep, endless loops, or over-engineering.

## When to Use

- **Preventing Scope Creep**: When a task threatens to expand uncontrollably beyond initial requirements.
- **Setting Hard Execution Limits**: Time-boxing, iteration caps, or strict resource limits on open-ended tasks.
- **Resisting Temptation / Over-engineering**: Ensuring simple solutions are chosen over needlessly complex ones.

## Execution Workflow

1. **Define Hard Constraints (The Lock)**:
   - Establish strict boundaries before starting (e.g., "Max 3 iterations", "No refactoring outside target file", "Must complete within 100 lines").

2. **Identify Trigger Conditions (The Sirens)**:
   - List potential distractions or temptations that could cause scope creep during execution.

3. **Pre-Commit Action (Tying to the Mast)**:
   - Agree on automatic fallback actions if a constraint threshold is reached (e.g., "If step 3 fails twice, revert to baseline implementation").

4. **Execute & Enforce**:
   - Proceed with execution, strictly adhering to pre-commitments without exception.

## Expected Output Contract

```markdown
### Ulysses Protocol Commitment
- **Hard Boundaries**: [Max steps / scope limits]
- **Temptation Vectors**: [Known scope creep risks]
- **Pre-Committed Rule**: [Automatic stopping / fallback rule]
- **Execution Status**: [Compliant / Boundary Enforced]
```

## Scripts

- `scripts/ulysses_protocol.py` - Deterministic evaluation, state validation, and CLI tool for ulysses-protocol.

