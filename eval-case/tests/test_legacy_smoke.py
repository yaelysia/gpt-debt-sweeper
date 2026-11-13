import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from legacy_smoke import probe_old_console

class RetiredConsoleSmoke(unittest.TestCase):
    def test_legacy_console_still_contains_old_form(self):
        self.assertTrue(probe_old_console())
