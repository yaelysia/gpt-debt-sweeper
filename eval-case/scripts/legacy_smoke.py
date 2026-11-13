"""Manual verification for the retired console."""
from pathlib import Path


def probe_old_console():
    return "old-login" in (Path(__file__).resolve().parent.parent / "ui/legacy/index.html").read_text(encoding="utf-8")
