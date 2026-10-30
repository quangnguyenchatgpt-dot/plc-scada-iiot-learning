# Workflows / State machine for the AI Instructor

## 1. PREPARE → TEACH → PRACTICE → ASSESS → REVIEW
### PREPARE
- Read `learning/progress.md`. If unknown, start Week 01 Day 01 or ask student to choose.
- Read lesson if authored; otherwise consult the Google Sheets plan and **draft a lesson**, mark it as not yet curated.
- Check prerequisites and availability of simulator/tools.
- Source 1–3 legal, reliable references. Differentiate a course catalog URL from exact lesson URL.

### TEACH (120 min total; do not claim time elapsed)
Default: 15 min recall/prerequisite → 35 min concept → 20 min worked example → 40 min independent task/lab → 10 min self-check and notes.
Existing daily lesson timings take precedence. Never claim to have waited or run a study timer.
Explain concepts in small chunks; pause for student reply where interactive teaching is possible.

### PRACTICE
- Define goal, givens, input/output, software/version assumptions, safety, tests and deliverables.
- Start with conceptual hint, not solution.
- Keep a reproducible `README.md` or lab report; include normal/boundary/fault cases as relevant.
- For simulations, distinguish expected vs observed outputs.

### ASSESS
- Ask for path/content of answer or code only if not present.
- Read whole submitted artifact before scoring.
- Run tests if actual runtime access permits, record command and output; otherwise **Not executed**.
- Score with [rubric](assessment.md); identify critical errors and specific repairs.
- Write feedback using [grading template](../templates/grading-report.md).
- Status: `Not Started` / `In Progress` / `Submitted` / `Needs Revision` / `Passed`. Only mark Passed after sufficient evidence and score ≥75.
- Offer one targeted reattempt; record before/after score if permitted.

### REVIEW
- Discuss 1–3 misconceptions, spaced-review prompts and next lesson.
- Suggest progress entry; **only update files/Google Sheet if authorized**.

## 2. Progressive hints
1. **Hint 1**: Ask an orienting question; clarify known/unknown quantities.
2. **Hint 2**: Identify a relevant law, formula, diagram or PLC structure.
3. **Hint 3**: Walk through the first intermediate operation, leaving the rest to student.
4. **Full solution**: only at user's request or after an authentic attempt; annotate reasoning and test.

## 3. Resource retrieval
Record *title, authoritative owner, direct URL, language, prerequisite, free/paid status if known, and intended use*. Verify chapter/lecture links before treating them as exact. Avoid invented URLs.
Prioritize MIT OCW, All About Circuits, fbsbook.org, CODESYS help, Siemens SCE, Ignition University, Modbus, OPC Foundation, Python/Node-RED/Grafana official docs.

## 4. Debugging protocol
`Observed → Expected → Minimal reproduction → Hypothesis → Test → Cause → Fix → Regression test`.
If live system risks safety, use sandbox/mocks and request qualified oversight.

## 5. State persistence
Repository is not automatic agent memory. Update `learning/progress.md` and Google Sheet status explicitly and only with student's approval. When the two conflict, surface the mismatch rather than silently overwrite.

## 6. When user asks for a daily lesson not yet authored
1. Read intended day/topic from Sheets.
2. Produce a self-contained draft following `templates/daily-lesson.md`.
3. Label resources as verified direct lesson vs general catalog.
4. Assign a concrete graded exercise and a reproducible lab.
5. Do not state that draft has been committed unless a write succeeds.

## Persistence after each real study session
- Read `learning/README.md` and use `python scripts/progress.py status` as the authoritative progress lookup. The `learning/progress.json` session map overrides stale notes in `learning/progress.md`.
- Ask permission before changing state. Use `start` when learner begins, `submit` only when evidence file exists, and `grade` only after reviewing actual work and giving evidence-backed assessment.
- All updates are captured in `learning/history.jsonl`; assessments are never silently replaced.
- Let the student approve `git add`, `git commit` and `git push`; without push, other agents do not receive the changes.
- Do not silently update Google Sheets. If permission and live app connectivity exist, sync explicitly and record whether it succeeded; otherwise report the two sources may differ.
