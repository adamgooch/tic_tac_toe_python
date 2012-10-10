import sys
import unittest
from src.negamax_ai import NegamaxAi
from src.board import Board

class TestNegamaxAi(unittest.TestCase):

  def setUp(self):
    self.ai = NegamaxAi()

  def test_get_move_blocks_a_threat(self):
    board = Board([ 'X', 'X', '3', 'O', '5', '6', '7', '8', '9' ])
    self.assertEqual(self.ai.get_move(board, self.ai.PLAYER_O), 3)

  def test_get_move_should_take_center(self):
    board = Board([ 'X', '2', '3', '4', '5', '6', '7', '8', '9' ])
    self.assertEqual(self.ai.get_move(board, self.ai.PLAYER_O), 5)

  def test_get_move_takes_win(self):
    board = Board([ 'X', 'O', '3', '4', 'O', 'X', 'X', '8', '9' ])
    self.assertEqual(self.ai.get_move(board, self.ai.PLAYER_O), 8)

