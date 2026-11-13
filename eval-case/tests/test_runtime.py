import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from engine import run_command

class RuntimePluginTests(unittest.TestCase):
    def test_status_loaded_only_through_config_and_importlib(self):
        self.assertEqual(run_command("status"), "READY")

    def test_unknown_command_is_rejected(self):
        with self.assertRaises(KeyError):
            run_command("legacy")
