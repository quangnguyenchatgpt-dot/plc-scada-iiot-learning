---
trigger: model_decision
description: Apply simulation-first safety and verification rules when authoring or reviewing electrical, PLC, SCADA, industrial communications or IIoT labs and designs.
---

# Industrial laboratory and validation

- Follow the common instructor contract in `AGENTS.md` and `docs/teaching-contract.md`.
- Software simulation comes before physical wiring.
- Do not recommend unsafe energized mains work, bypassing interlocks, or substituting ordinary PLC logic for functional safety.
- Explicitly state signal voltage/current units, I/O assumptions, device state and failure behavior.
- For lab results report expected, observed, evidence and whether tests truly executed.
- Prefer low-risk disconnected simulators and mock signals for fault injection.
