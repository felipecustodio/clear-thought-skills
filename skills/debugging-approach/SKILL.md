---
name: debugging-approach
description: Applies root-cause isolation, binary search debugging, error trace analysis, and systematic troubleshooting methodologies.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Debugging Approach provides a systematic methodology for isolating software bugs, performance bottlenecks, and hardware/network errors without reliance on guess-and-check.

## When to Use

- **Software Debugging**: Investigating stack traces, test failures, memory leaks, or unexpected output.
- **System Troubleshooting**: Diagnosing configuration errors or environment mismatches.

## Execution Workflow

1. **Reproduce & Isolate**: Establish minimal reproducible example.
2. **Formulate Hypotheses**: List potential failure points based on error signature.
3. **Binary Search Isolation**: Divide search space in half (e.g., git bisect, narrowing down line numbers or components).
4. **Inspect State**: Verify actual vs expected values at boundaries.
5. **Fix & Verify**: Apply minimal necessary fix and verify no regressions.

## Expected Output Contract

```markdown
### Debugging Report
- **Error Signature**: [Stack trace / symptom]
- **Isolation Boundary**: [Component / line identified]
- **Root Cause**: [Mechanism of failure]
- **Verification**: [Test confirming fix]
```

## Scripts

Python support omitted: Agent context window natively applies debugging methodologies without requiring external deterministic scripts.
