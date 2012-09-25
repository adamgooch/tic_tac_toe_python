import unittest

from src.board_analyzer import BoardAnalyzer

class TestBoardAnalyzer(unittest.TestCase):

  def test_game_over_is_true_when_board_is_full(self):
    board = [ 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O' ]
    board_analyzer = BoardAnalyzer()
    self.assertEqual(True, board_analyzer.game_over(board))

  def test_game_over_sets_the_winner_value(self):
    board = [ 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O' ]
    board_analyzer = BoardAnalyzer()
    board_analyzer.game_over(board)
    self.assertEqual('Nobody', board_analyzer.winner)
