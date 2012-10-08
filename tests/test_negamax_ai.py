import sys
import unittest
from src.negamax_ai import NegamaxAi

class TestNegamaxAi(unittest.TestCase):

  def setUp(self):
    self.ai = NegamaxAi()

  def test_get_move_blocks_a_threat(self):
    board = [ 'X', 'X', '3', 'O', '5', '6', '7', '8', '9' ]
    self.assertEqual(self.ai.get_move(board, self.ai.PLAYER_O), 2)

  def test_get_move_should_take_center(self):
    board = [ 'X', '2', '3', '4', '5', '6', '7', '8', '9' ]
    self.assertEqual(self.ai.get_move(board, self.ai.PLAYER_O), 4)

  def test_get_move_takes_win(self):
    board = [ 'X', 'O', '3', '4', 'O', 'X', 'X', '8', '9' ]
    self.assertEqual(self.ai.get_move(board, self.ai.PLAYER_O), 7)

