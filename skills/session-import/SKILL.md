---
name: session-import
description: Deserializes stored JSON session state files to restore thought context and memory.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Session Import reads a stored JSON session file from disk and restores memory state, allowing seamless continuation of prior work.

## When to Use

- **Resuming Saved Work**: Loading previously exported session state.
- **Receiving Subagent Context**: Reading state created by another subagent process.

## Execution Workflow

1. **Locate Target File**: Verify existence of target `.json` file.
2. **Execute Import Script**: Call `scripts/session_import.py --file <path>`.
3. **Restore Context**: Parse returned JSON data and update active agent memory state.

## Expected Output Contract

```markdown
### Session Import Complete
- **Source File**: [File Path]
- **Imported Items Count**: [Count]
- **Status**: [Context Restored]
```

## Scripts

- `scripts/session_import.py` - CLI script for JSON deserialization.
