"""Commands are discovered through configuration and importlib at runtime."""
import importlib
import json
from pathlib import Path

ROOT = Path(__file__).parent


def run_command(name):
    config = json.loads((ROOT / "commands.json").read_text(encoding="utf-8"))
    module_name = config["commands"][name]
    class_name = "".join(part.capitalize() for part in module_name.split("_")) + "Command"
    plugin = importlib.import_module("plugins." + module_name)
    return getattr(plugin, class_name)().run()
