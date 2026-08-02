---
name: visual-dashboard
description: Generates interactive HTML/CSS/JS dashboards and metrics panels for complex data visualization.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Visual Dashboard renders rich, interactive HTML dashboards containing metrics panels, Charts, and responsive layouts to visually present complex analysis.

## When to Use

- **Data Reporting**: Displaying multi-metric performance reports or telemetry data.
- **Executive Summaries**: Creating visually engaging dashboard UI artifacts.

## Execution Workflow

1. **Define Layout & Panels**: Design grid/flex layout and identify metric panels.
2. **Construct HTML/CSS/JS Payload**: Build responsive HTML containing CSS styles and Chart.js script definitions.
3. **Output Dashboard Artifact**: Present clean HTML artifact for rendering.

## Expected Output Contract

```markdown
### Generated Visual Dashboard
- **Title**: [Dashboard Title]
- **Layout**: [Grid / Flex]
- **Panels Rendered**: [List of Panels]
- **HTML Payload**: [Rendered HTML block]
```

## Scripts

- `scripts/visual_dashboard.py` - Deterministic evaluation, state validation, and CLI tool for visual-dashboard.

