"""Tests for progression and assessment logic (no writes to tracked data)."""
import importlib.util
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "progress.py"
spec = importlib.util.spec_from_file_location("progress_tool", SCRIPT)
progress = importlib.util.module_from_spec(spec)
spec.loader.exec_module(progress)


def fresh():
    return {"schema_version": 1, "program": {"total_sessions": 312}, "sessions": {}}


class ProgressTests(unittest.TestCase):
    def test_next_session_and_mapping(self):
        self.assertIn("Buổi 1, tuần 1", progress.summary(fresh()))
        data = fresh()
        data["sessions"]["1"] = {"status": "passed"}
        data["sessions"]["2"] = {"status": "passed"}
        data["sessions"]["3"] = {"status": "passed"}
        self.assertIn("Buổi 4, tuần 2", progress.summary(data))

    def test_grade_requires_submission(self):
        with self.assertRaises(ValueError):
            progress.action_grade(fresh(), 1, 90, "a.md", "OK", False)

    def test_grade_after_submission(self):
        data = fresh()
        with TemporaryDirectory() as d, patch.object(progress, "ROOT", Path(d)):
            evidence = Path(d) / "lab.md"
            evidence.write_text("Lab completed", encoding="utf-8")
            progress.action_start(data, 1)
            progress.action_submit(data, 1, "lab.md", "Nộp")
            progress.action_grade(data, 1, 85, "lab.md", "Đủ minh chứng", False)
            self.assertEqual(data["sessions"]["1"]["status"], "passed")
            self.assertEqual(len(data["sessions"]["1"]["assessments"]), 1)

    def test_safety_block(self):
        data = fresh()
        with TemporaryDirectory() as d, patch.object(progress, "ROOT", Path(d)):
            (Path(d) / "lab.md").write_text("Example", encoding="utf-8")
            progress.action_start(data, 3)
            progress.action_submit(data, 3, "lab.md", "")
            progress.action_grade(data, 3, 99, "lab.md", "Unsafe wiring", True)
            self.assertEqual(data["sessions"]["3"]["status"], "needs_revision")

    def test_invalid_session(self):
        for i in (0, 313):
            with self.assertRaises(ValueError):
                progress.action_start(fresh(), i)


if __name__ == "__main__":
    unittest.main()
