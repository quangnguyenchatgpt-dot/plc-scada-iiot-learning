---
name: grade-submission
description: Grade the student's actual PLC/SCADA/IIoT homework, code, calculations, simulations or lab reports using a 100-point evidence-based rubric. Use when the learner asks to grade, review, assess, score or correct submitted work.
---

# Grade Submission

Read `AGENTS.md`, `docs/assessment.md`, `templates/grading-report.md` and the original exercise instructions. Never grade from an imagined submission.

1. Find student-provided source and tests, read the whole relevant submission and restate the target requirements.
2. Evaluate concepts (20), exercise correctness (25), reproducible simulation/code (30), test coverage and handling of faults (15), and documentation (10).
3. When a runtime is available, run *appropriate safe tests* and report the exact command and observed result; otherwise explicitly mark **Not executed**.
4. Cite evidence by file, line, numeric result or trace, distinguishing a test failure from missing evidence.
5. Provide a score table with awarded and maximum values, total /100, and pass only if ≥75 **and** no critical safety issue or essential requirement failure.
6. Prioritize 1–3 actionable fixes and one focused reattempt. Use progressive hints by default instead of replacing a student's solution.
7. Offer a progress update but **do not write grades or edit student files without explicit permission**.
8. Preserve previous assessments; never overwrite the previous score without the student's approval.

## Persisting assessments
After grading actual submitted work and receiving learner approval, use `python scripts/progress.py grade ID --score SCORE --evidence PATH --feedback "..." [--critical-issue]`. The target record must already be in submitted state and reference an existing file inside the repository. If not, submit the real artifact first with `scripts/progress.py submit` after starting its session. This stores assessment history without overwriting prior attempts. Remote sync needs explicit Git commit/push permission.
