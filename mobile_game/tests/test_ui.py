import unittest
from app.ui import GameUI

class TestUI(unittest.TestCase):
    def setUp(self):
        self.ui = GameUI()

    def test_initial_score_label(self):
        self.assertEqual(self.ui.score_label.text, "Score: 0")

    def test_update_score_label(self):
        self.ui.update_score(10)
        self.assertEqual(self.ui.score_label.text, "Score: 10")
