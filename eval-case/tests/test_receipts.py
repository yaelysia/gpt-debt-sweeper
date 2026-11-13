import unittest
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
from reporting import _receipt_for, _confirm_receipt
from verify_receipt import verify_sample

class InternalReceiptTests(unittest.TestCase):
    def test_self_generated_receipt(self):
        value = (ROOT / "fixtures" / "receipt_sample.txt").read_text(encoding="utf-8").strip()
        self.assertTrue(_confirm_receipt(value, _receipt_for(value)))
        self.assertTrue(verify_sample(value))
