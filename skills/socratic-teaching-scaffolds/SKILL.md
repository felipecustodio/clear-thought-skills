---
name: socratic-teaching-scaffolds
description: Guides learners to discover knowledge through strategic Socratic questioning and progressive scaffolding removal. Combines question ladders, misconception detectors, Feynman explanations, and worked-example fading.
license: MIT
compatibility: Requires Python 3.12+ and uv when running bundled scripts.
---

## Overview & Purpose

Socratic Teaching Scaffolds guides learners to discover knowledge through strategic Socratic questioning and progressive scaffolding removal. It combines question ladders, misconception detectors, Feynman explanations, and worked-example fading to build durable mental models.

## When to Use

- **Teaching & Mentoring**: Onboarding team members, mentoring problem-solving, or teaching complex technical concepts.
- **Correcting Misconceptions**: Identifying and eliminating faulty mental models through contradiction and discovery.
- **Guided Discovery**: When the user requests "teach me", "help me understand", "explain like I'm 5", or "guided discovery".

## When NOT to Use

- Direct implementation tasks where the user simply wants code written immediately without a learning loop.

## Execution Workflow

1. **Diagnose Understanding**: Ask diagnostic probing questions to identify the learner's current knowledge level and misconceptions.
2. **Design Question Ladder & Scaffolding Plan**: Build a sequence of questions from simple to complex (Problem Decomposition -> Base Case -> Recursive/General Case -> Termination/Edge Reasoning).
3. **Guide Discovery through Questioning**: Present questions in sequence, providing hints, worked examples, or Feynman analogies as needed.
4. **Fade Scaffolding**: Progressively remove hints, ask more open-ended questions, and monitor optimal challenge vs. frustration.
5. **Validate Understanding & Transfer**: Test the learner with novel problems and ask for explanations in their own words.

## Expected Output Contract

```markdown
### Socratic Scaffold Session
- **Target Concept**: [Concept Name]
- **Diagnostic Finding**: [Learner's current mental model]
- **Question Ladder**:
  1. [Probing question 1]
  2. [Probing question 2]
- **Feynman Analogy**: [Simple physical / real-world framing]
- **Validation**: [Transfer problem or self-explanation prompt]
```

## Scripts

- `scripts/socratic_teaching_scaffolds.py` - Evaluation helper and scaffolding state validation tool.

## Gotchas

- Never give away the full answer upfront when in Socratic mode; allow the learner to make the discovery.
- If the learner experiences extreme frustration, temporarily increase scaffolding levels before fading again.
