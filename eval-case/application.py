"""Desktop entrypoint and packaging inventory for the current UI."""
import json
from pathlib import Path

ROOT = Path(__file__).parent


def launch_window():
    config = json.loads((ROOT / "window.json").read_text(encoding="utf-8"))
    return (ROOT / config["window_entry"]).read_text(encoding="utf-8")


def package_assets():
    return [line.strip() for line in (ROOT / "package-files.txt").read_text(encoding="utf-8").splitlines() if line.strip()]
