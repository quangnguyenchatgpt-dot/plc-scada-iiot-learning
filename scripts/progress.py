#!/usr/bin/env python3
"""Local, Git-versioned learning progress for 312 sessions. Standard library only."""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "learning" / "progress.json"
HISTORY = ROOT / "learning" / "history.jsonl"
TOTAL = 312
VALID = {"in_progress", "submitted", "needs_revision", "passed"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def check_id(number: int) -> str:
    if not 1 <= number <= TOTAL:
        raise ValueError(f"Buổi phải trong khoảng 1–{TOTAL}.")
    return str(number)


def load() -> dict:
    with DATA.open(encoding="utf-8") as fp:
        data = json.load(fp)
    if data.get("schema_version") != 1 or data.get("program", {}).get("total_sessions") != TOTAL:
        raise ValueError("Phiên bản dữ liệu hoặc tổng số buổi không hợp lệ.")
    if not isinstance(data.get("sessions"), dict):
        raise ValueError("sessions phải là object.")
    return data


def atomic_write(data: dict) -> None:
    DATA.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".progress-", suffix=".json", dir=DATA.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fp:
            json.dump(data, fp, indent=2, ensure_ascii=False)
            fp.write("\n")
        os.replace(name, DATA)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def save(data: dict, event: dict) -> None:
    event["at"] = now()
    data["updated_at"] = event["at"]
    atomic_write(data)
    with HISTORY.open("a", encoding="utf-8", newline="\n") as fp:
        fp.write(json.dumps(event, ensure_ascii=False) + "\n")


def relative_evidence(path: str) -> str:
    if not path.strip():
        raise ValueError("Cần đường dẫn bằng chứng.")
    resolved = (ROOT / path).resolve()
    if not resolved.is_relative_to(ROOT):
        raise ValueError("Bằng chứng phải nằm trong repository.")
    if not resolved.is_file():
        raise ValueError(f"Chưa tìm thấy file bằng chứng: {path}")
    return resolved.relative_to(ROOT).as_posix()


def summary(data: dict) -> str:
    sessions = data["sessions"]
    passed = [i for i in range(1, TOTAL + 1)
              if sessions.get(str(i), {}).get("status") == "passed"]
    next_id = next((i for i in range(1, TOTAL + 1) if i not in passed), None)
    active = sum(r.get("status") == "in_progress" for r in sessions.values())
    submitted = sum(r.get("status") == "submitted" for r in sessions.values())
    revision = sum(r.get("status") == "needs_revision" for r in sessions.values())
    nxt = (f"Buổi {next_id}, tuần {(next_id - 1) // 3 + 1}, "
           f"buổi trong tuần {(next_id - 1) % 3 + 1}") if next_id else "Đã đạt tất cả"
    return (f"Đạt: {len(passed)}/{TOTAL} ({len(passed) / TOTAL * 100:.1f}%). "
            f"Đang học: {active}; Đã nộp: {submitted}; Cần sửa: {revision}. "
            f"Tiếp theo: {nxt}.")


def action_start(data: dict, number: int) -> dict:
    sid = check_id(number)
    rec = data["sessions"].get(sid, {})
    if rec.get("status") == "passed":
        raise ValueError("Buổi đã đạt; không mở lại bằng lệnh start.")
    rec.setdefault("assessments", [])
    rec["status"] = "in_progress"
    rec.setdefault("started_at", now())
    data["sessions"][sid] = rec
    return {"type": "started", "session_id": number}


def action_submit(data: dict, number: int, evidence: str, note: str) -> dict:
    sid = check_id(number)
    rec = data["sessions"].get(sid, {})
    if rec.get("status") == "passed":
        raise ValueError("Buổi đã đạt; giữ nguyên điểm.")
    if rec.get("status") not in ("in_progress", "submitted", "needs_revision"):
        raise ValueError("Cần start trước khi submit.")
    ref = relative_evidence(evidence)
    rec["status"] = "submitted"
    rec["evidence"] = ref
    rec["submitted_at"] = now()
    rec["note"] = note
    rec.setdefault("assessments", [])
    data["sessions"][sid] = rec
    return {"type": "submitted", "session_id": number, "evidence": ref}


def action_grade(data: dict, number: int, score: int, evidence: str,
                 feedback: str, critical_issue: bool) -> dict:
    sid = check_id(number)
    if not 0 <= score <= 100:
        raise ValueError("Điểm phải nằm trong 0–100.")
    rec = data["sessions"].get(sid, {})
    if rec.get("status") != "submitted":
        raise ValueError("Chỉ chấm khi bài ở trạng thái submitted.")
    ref = relative_evidence(evidence)
    if rec.get("evidence") != ref:
        raise ValueError("Bằng chứng chấm phải khớp với bài đã nộp.")
    if not feedback.strip():
        raise ValueError("Chấm điểm phải có nhận xét dựa trên bằng chứng.")
    passed = score >= 75 and not critical_issue
    rec.setdefault("assessments", []).append({
        "score": score, "feedback": feedback, "evidence": ref,
        "critical_issue": critical_issue, "graded_at": now(),
    })
    rec["status"] = "passed" if passed else "needs_revision"
    data["sessions"][sid] = rec
    return {"type": "graded", "session_id": number,
            "score": score, "result": rec["status"], "evidence": ref}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="Xem buổi tiếp theo và tổng tiến độ")
    start = sub.add_parser("start")
    start.add_argument("session", type=int)
    submit = sub.add_parser("submit")
    submit.add_argument("session", type=int)
    submit.add_argument("--evidence", required=True)
    submit.add_argument("--note", default="")
    grade = sub.add_parser("grade")
    grade.add_argument("session", type=int)
    grade.add_argument("--score", type=int, required=True)
    grade.add_argument("--evidence", required=True)
    grade.add_argument("--feedback", required=True)
    grade.add_argument("--critical-issue", action="store_true")
    args = parser.parse_args(argv)
    try:
        data = load()
        if args.command == "status":
            print(summary(data))
            return 0
        if args.command == "start":
            event = action_start(data, args.session)
        elif args.command == "submit":
            event = action_submit(data, args.session, args.evidence, args.note)
        else:
            event = action_grade(data, args.session, args.score, args.evidence,
                                 args.feedback, args.critical_issue)
        save(data, event)
        print(json.dumps(event, ensure_ascii=False))
        print(summary(data))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Lỗi: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
