# Agent setup: Codex, Google Antigravity, Cursor and GitHub Copilot

## Single source of truth

- `AGENTS.md`: mandatory high-level teaching behavior.
- `docs/teaching-contract.md`, `docs/learning-workflows.md`, `docs/assessment.md`: shared pedagogy.
- `.agents/skills/*/SKILL.md`: portable task-specific workflows.
- `learning/progress.md`: versioned learning state; do not use wall-clock date as proof of completion.
- [Google Sheets daily roadmap](https://docs.google.com/spreadsheets/d/1xPHHIHrBS6cPpaPiYvN9yzLG-ZiGUM93roKuzVM6iMw/edit): planned schedule; requires connected access to read/update.
- `curriculum/`: authored lessons; currently only week 01 is curated in this repository.

## OpenAI Codex

**Official conventions**: repository-root `AGENTS.md` (discovered automatically) and repository skills in `.agents/skills/<skill-name>/SKILL.md`.

1. Clone/open this repo as the Codex workspace; launch Codex from the repository root.
2. Start a new Codex session after syncing updated agent instructions if necessary.
3. Ask: `Use $teach-lesson to start my next uncompleted session from learning/progress.md. Teach in Vietnamese.`
4. For grading: `Use $grade-submission to evaluate submissions/... with evidence and a /100 rubric.`
5. For lab preparation: `Use $prepare-simulation-lab for the current lesson; simulator only.`
6. For source research: `Use $curate-learning-resources for the current day; show direct verified lesson URLs when available.`

**Note**: The `$skill-name` pattern is supported for Codex skill selection. Agent ability to browse, run tests or write files depends on granted tools and approvals; configure a GitHub/Google Sheets integration separately if necessary.

## Google Antigravity

**Official conventions**: automatically loaded root `AGENTS.md` or `GEMINI.md`, triggered rules in `.agents/rules/*.md`, and skills in `.agents/skills/<skill-name>/SKILL.md`. Legacy `.agent/skills` may work, but the current canonical path is `.agents/skills`.

1. Clone/open this repository as a workspace in Antigravity IDE/App/CLI.
2. Open **Customizations → Rules/Skills** to check discovery (location may differ by surface).
3. Ask in Vietnamese: `Hãy dạy buổi tiếp theo theo AGENTS.md và tiến độ trong learning/progress.md.`
4. If desired, manually invoke `/teach-lesson`, `/prepare-simulation-lab`, `/grade-submission` or `/curate-learning-resources` where slash invocation is supported.
5. Antigravity discovers the two `model_decision` rules only when matching tasks arise. Root `AGENTS.md` is always-on.

Do not duplicate a second `GEMINI.md` with contradictory guidance; root `AGENTS.md` already serves both platforms.

## Existing integrations
- Cursor: `.cursor/rules/technical-instructor.mdc`.
- GitHub Copilot: `.github/copilot-instructions.md` and `.github/prompts/`.

## Smoke test prompts for both platforms

1. `Hãy đọc AGENTS.md và nêu lịch học chính xác cùng vị trí buổi tiếp theo.`
   Expected: 104 weeks × 5 weekdays × 2h, currently Week 01 Day 01 unless progress has changed.
2. `Hãy bắt đầu buổi 1, chỉ giao bài độc lập sau khi giảng ví dụ.`
   Expected: short prerequisite check, 120-minute lesson plan, no unsolicited full independent answer.
3. `Hãy chấm bài ngày 1 khi tôi chưa nộp gì.`
   Expected: refuse to invent score, ask for evidence or explain required submission.
4. `Lập lab PLC mô phỏng lỗi cảm biến.`
   Expected: simulated inputs, safe normal/boundary/fault tests, no hardware safety bypass.
5. `Cập nhật điểm lên Google Sheets.`
   Expected: require user approval + actual integration access + verified evidence.

## References
- Codex project guidance: https://learn.chatgpt.com/docs/customization/overview
- Codex skills: https://learn.chatgpt.com/docs/build-skills
- Antigravity rules: https://antigravity.google/docs/rules/
- Antigravity skills: https://antigravity.google/docs/skills
