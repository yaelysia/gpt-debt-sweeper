import unittest
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
from run_legacy import check_retired_plugin

class OldDiagnosticTests(unittest.TestCase):
    def test_legacy_diagnostic(self):
        self.assertTrue(check_retired_plugin())
