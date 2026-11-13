import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from application import launch_window, package_assets

class CurrentUiTests(unittest.TestCase):
    def test_current_window_loads(self):
        self.assertIn("Current UI", launch_window())

    def test_all_shipped_assets_exist(self):
        root = Path(__file__).resolve().parent.parent
        self.assertIn("ui/dist/index.html", package_assets())
        for item in package_assets():
            self.assertTrue((root / item).is_file(), item)
