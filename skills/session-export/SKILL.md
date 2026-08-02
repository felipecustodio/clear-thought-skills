---
name: session-export
description: Serializes current session state, thought history, and memory data into structured JSON files for persistence.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Session Export serializes the active session context into structured JSON format to disk, allowing state persistence across tool calls or subagents.

## When to Use

- **State Persistence**: Saving progress before long background operations.
- **Hand-off to Subagents**: Exporting context for sibling or child subagents.

## Execution Workflow

1. **Gather Session Memory**: Collect active thoughts, variables, and metadata.
2. **Execute Export Script**: Call `scripts/session_export.py --file <path> --data <json_string>`.
3. **Verify File Creation**: Confirm the JSON target file was created cleanly.

## Expected Output Contract

```markdown
### Session Export Complete
- **Target File**: [File Path]
- **Export Status**: [Success / Failed]
```

## Scripts

- `scripts/session_export.py` - CLI script for JSON serialization.

## Gotchas

- Ensure payload JSON is properly escaped when passed via command line flags.
