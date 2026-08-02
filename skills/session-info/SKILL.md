---
name: session-info
description: Summarizes the current agent session metadata, active reasoning state, thought counts, and historical trajectory.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Session Info provides a meta-view of the active conversation's cognitive trajectory, tracking active memory states, completed thoughts, and overall progress.

## When to Use

- **Progress Summarization**: Reporting session state during long-running tasks.
- **Context Audit**: Verifying remaining thought budget or session parameters.

## Execution Workflow

1. **Inspect Active Context**: Count thoughts executed, active branches, and current skill state.
2. **Synthesize History**: Summarize key milestones achieved in the current session.
3. **Report Metadata**: Output structured session status.

## Expected Output Contract

```markdown
### Session Status Report
- **Session ID**: [Current ID / Active Context]
- **Total Thoughts Executed**: [N]
- **Active Skills**: [List of active skills]
- **Current Milestone**: [Summary of progress]
```

## Scripts

- `scripts/session_info.py` - Deterministic evaluation, state validation, and CLI tool for session-info.

