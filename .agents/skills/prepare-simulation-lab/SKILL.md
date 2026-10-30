---
name: prepare-simulation-lab
description: Design and guide safe, reproducible simulation-first labs for electronics, PLC Ladder/ST, PID, HMI/SCADA, Modbus, OPC UA, MQTT and IIoT. Use when the student asks for lab instructions, virtual equipment, simulator setup or debugging.
---

# Prepare Simulation Lab

Read `AGENTS.md`, `docs/learning-workflows.md`, `templates/daily-lesson.md` and the week's syllabus if present.

1. Identify the skill prerequisite and a measurable lab objective.
2. Prefer no-cost tools and simulators such as LTspice, CODESYS SoftPLC, Python models, Modbus simulators, Ignition Maker Edition, Node-RED and Mosquitto. Distinguish installation/licensing claims from verified facts.
3. Specify software, version assumption if material, hardware requirements, input/output and file layout.
4. Give numbered setup and lab steps with expected intermediate observations.
5. Add normal, boundary and fault-injection cases, with expected outcomes. Use mock signals when hardware is absent.
6. Provide an acceptance checklist, reproducible run command if applicable, and lab-report path using `templates/lab-report.md`.
7. Keep required work within the day's 2-hour limit; mark optional extensions separately.
8. When reviewing results, separate predicted results from actual measured output. Never claim tests were run when not executed.

Do not propose live mains work or bypass of industrial safety circuits. For PLC tests verify Stop priority, interlock, unexpected restart, fault/reset. For telemetry verify timestamps, quality and disconnect handling.
