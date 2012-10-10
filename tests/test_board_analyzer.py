import unittest

from src.board_analyzer import BoardAnalyzer
from src.board import Board

class TestBoardAnalyzer(unittest.TestCase):

  no_winner_board = Board([ 'X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O' ])
  empty_board = Board([ '1', '2', '3', '4', '5', '6', '7', '8', '9' ])
  x_wins_board = Board([ 'X', 'X', 'X', 'O', '5', 'O', '7', 'O', '9' ])
  o_wins_board = Board([ 'O', 'O', 'O', 'X', '5', 'X', '7', 'X', '9' ])

  def setUp(self):
    self.board_analyzer = BoardAnalyzer()

  def test_game_over_is_true_when_board_is_full(self):
    self.assertTrue(self.board_analyzer.game_over(self.no_winner_board))

  def test_game_over_is_false_when_there_is_no_winner_and_board_is_not_full(self):
    self.assertFalse(self.board_analyzer.game_over(self.empty_board))

  def test_game_over_is_true_when_x_has_won(self):
    self.assertTrue(self.board_analyzer.game_over(self.x_wins_board))

  def test_game_over_is_true_when_o_has_won(self):
    self.assertTrue(self.board_analyzer.game_over(self.o_wins_board))

  def test_game_over_sets_the_winner_value_to_nobody(self):
    self.board_analyzer.game_over(self.no_winner_board)
    self.assertEqual('Nobody', self.board_analyzer.winner)

  def test_game_over_sets_the_winner_to_x(self):
    self.board_analyzer.game_over(self.x_wins_board)
    self.assertEqual('X', self.board_analyzer.winner)

  def test_game_over_sets_the_winner_to_o(self):
    self.board_analyzer.game_over(self.o_wins_board)
    self.assertEqual('O', self.board_analyzer.winner)

  def test_x_wins_diagonally(self):
    board = Board(['X', 'O', 'X', 'O', 'X', 'O', 'X', '8', '9'])
    self.assertTrue([self.board_analyzer.game_over(board)])

  def test_nobody_wins(self):
    board = Board(['X', '2', 'O', '4', '5', '6', '7', '8', '9'])
    self.assertFalse(self.board_analyzer.game_over(board))
