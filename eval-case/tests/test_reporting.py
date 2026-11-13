import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shopfront import checkout_preview

class CheckoutTests(unittest.TestCase):
    def test_invoice_total(self):
        order = {"id":"order-7","items":[{"count":2,"price":3},{"count":1,"price":4}]}
        self.assertEqual(checkout_preview(order), "order-7: 10 credits")

    def test_empty_items(self):
        self.assertEqual(checkout_preview({"id":"empty","items":[]}), "empty: 0 credits")
