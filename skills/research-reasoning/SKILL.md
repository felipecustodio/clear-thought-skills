---
name: research-reasoning
description: Synthesizes scientific literature, cross-references sources, evaluates evidence quality, and builds systematic research summaries.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Research Reasoning organizes literature review and information gathering into a structured synthesis, evaluating source credibility, methodology soundness, and evidence strength.

## When to Use

- **Literature Reviews**: Synthesizing academic papers, technical documentation, or benchmarks.
- **Fact-Checking & Evidence Synthesis**: Evaluating conflicting technical claims across sources.

## Execution Workflow

1. **Define Research Query**: State explicit research questions.
2. **Source Gathering & Categorization**: Collect primary sources, documentation, or empirical studies.
3. **Evidence Evaluation**: Grade sources by peer-review status, recency, sample size, and methodology.
4. **Synthesis & Triangulation**: Combine findings across multiple independent sources.
5. **Identify Gaps**: Highlight unresolved questions or conflicting evidence.

## Expected Output Contract

```markdown
### Research Synthesis
- **Research Question**: [Target Query]
- **Key Findings**:
  - *Finding 1* (Source A, B): [Summary of evidence]
- **Source Quality Evaluation**: [High / Medium / Low Credibility Analysis]
- **Unresolved Gaps**: [Open questions]
```

## Scripts

Python support omitted: Agent context window natively executes research synthesis without requiring external deterministic scripts.
