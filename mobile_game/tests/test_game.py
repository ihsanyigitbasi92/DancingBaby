import unittest
from app.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_score(self):
        self.assertEqual(self.game.score, 0)

    def test_score_increment(self):
        self.game.on_touch()
        self.assertEqual(self.game.score, 1)
