import unittest

from src.board_analyzer import BoardAnalyzer

class TestBoardAnalyzer(unittest.TestCase):

  no_winner_board = [ 'X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O' ]
  empty_board = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
  x_wins_board = [ 'X', 'X', 'X', 'O', '5', 'O', '7', 'O', '9' ]
  o_wins_board = [ 'O', 'O', 'O', 'X', '5', 'X', '7', 'X', '9' ]

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
