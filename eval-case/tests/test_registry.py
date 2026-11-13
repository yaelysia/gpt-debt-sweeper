import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from notifications.registry import get_backend
from notifications.forwarder import Forwarder

class RegistryTests(unittest.TestCase):
    def test_roundtrip_through_scaffolding(self):
        sender = Forwarder(get_backend("text"))
        self.assertEqual(sender.send("Ada", "welcome"), "TO:Ada|welcome")
