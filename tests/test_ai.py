import unittest
from src.ai import Ai

class TestAi(unittest.TestCase):

  def setUp(self):
    self.ai = Ai()

  def test_get_move_blocks_a_threat(self):
    board = [ 'X', 'X', '3', 'O', '5', '6', '7', '8', '9' ]
    self.assertEqual(self.ai.get_move(board), 2)
