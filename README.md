<p align="center">
  <video src="assets/brain.mp4" width="100%" controls></video>
</p>

# clear-thought-skills

◇ Clear Thought MCP, recast as Agent Skills.

Based on the original [Clear Thought 1.5 MCP Server](https://github.com/waldzellai/clearthought-onepointfive#) by Waldzell AI.

## § Aim

Convert Clear Thought reasoning tools into:

• focused `SKILL.md` instructions  
• minimal Python scripts  
• deterministic validation  
• high-coverage tests

## § Shape

```text
skills/        → Agent Skill directories
scripts/       → project utilities
shared/        → reusable Python helpers
tests/         → behavior and script coverage
SPEC.md        → migration contract
```

## § Rules

• `pyproject.toml` defines packages and tools  
• `uv.lock` pins the environment  
• `uv sync` installs dependencies  
• `just check` gates local changes  
• `prek` runs hooks  
• GitHub CI gates merges

## § Commands

```bash
just sync
just check
just validate-skills
```

## § Status

◦ planning complete  
◦ tooling scaffolded  
◦ skill migration next

## § Credit

Original implementation: [waldzellai/clearthought-onepointfive](https://github.com/waldzellai/clearthought-onepointfive#).
