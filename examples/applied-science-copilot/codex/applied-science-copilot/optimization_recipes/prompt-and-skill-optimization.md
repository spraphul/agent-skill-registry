# Prompt and Skill Optimization

Use when failures are instruction, example, routing, or procedural-boundary related.

Candidate techniques:

- APE/OPRO for prompt candidate generation and scoring.
- ProTeGi/TextGrad-style textual feedback for directed edits.
- DSPy teleprompters for module/signature pipelines.
- GEPA-style trace reflection for compound systems.
- Skill refactoring: split, merge, tighten triggers, add preconditions, constrain outputs, update tool permissions.

Required safeguards:

- Baseline prompt/skill version.
- Train/dev/holdout separation.
- Regression suite.
- Failure tags and changelog.
- Rollback version.
