import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from notifications import send_welcome

class WelcomeTests(unittest.TestCase):
    def test_welcome(self):
        self.assertEqual(send_welcome("Ada"), "TO:Ada|welcome")

    def test_empty_name(self):
        self.assertEqual(send_welcome(""), "TO:|welcome")
