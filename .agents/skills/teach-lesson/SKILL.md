---
name: teach-lesson
description: Teach or continue a 120-minute Vietnamese lesson in electricity, ESP32, PLC, SCADA or IIoT, including an independent exercise. Use when the learner asks to start, continue or understand a lesson.
---

# Teach Lesson

Read `AGENTS.md`, `docs/learning-workflows.md` and `learning/progress.json`. If a terminal exists, run `python scripts/progress.py status` to select the first unpassed session. The learner chooses any three study days weekly. After missed days or weeks, continue the earliest unpassed session, never skip. Do not use calendar date or `progress.md` as proof of completion.

Identify the week, session and prerequisites. Read the authored lesson in `curriculum/` if present. Otherwise use the schedule and sources to create a **clearly labeled draft**, not a claim that the lesson was already curated.

Provide objectives and 1–3 legitimate sources (mark catalog links as catalog). Teach intuition → formal rules → worked example → industrial context. Assign a different problem for independent solution; provide progressive hints rather than a complete answer unless explicitly requested.

Keep exactly **120 minutes** (default 15 recall, 35 concept, 20 worked example, 40 practice, 10 review). Include expected deliverable and acceptance criteria.

`labs/` contains reference implementations; ask the student to save actual work under `submissions/`. Only at the student's direction run `scripts/progress.py start` or other progress commands; commit/push requires explicit authorization. Do not automatically sync Google Sheets.
