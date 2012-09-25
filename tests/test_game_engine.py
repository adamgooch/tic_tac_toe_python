import unittest
import sys
import src.game

from src.game_engine import GameEngine
from mock import *

class TestGameEngine(unittest.TestCase):

  moves = [2]

  def setUp(self):
    self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    self.mock_io = Mock()
    self.mock_board_analyzer = Mock()
    self.engine = GameEngine(self.board, self.mock_io, self.mock_board_analyzer)
    self.mock_io.get_move.return_value = self.moves[0]

  def test_start_displays_board(self):
    return_values = [False, True]
    self.mock_board_analyzer.game_over.side_effect = return_values
    self.engine.start(src.game.PLAYER_VS_PLAYER)
    self.mock_io.assert_has_calls([call.display_board(self.board)])

  def test_start_gets_player_move(self):
    return_values = [False, True]
    self.mock_board_analyzer.game_over.side_effect = return_values
    self.engine.start(src.game.PLAYER_VS_PLAYER)
    self.mock_io.assert_has_calls([call.get_move()])

  def test_start_puts_move_on_the_board(self):
    return_values = [False, True]
    self.mock_board_analyzer.game_over.side_effect = return_values
    self.engine.start(src.game.PLAYER_VS_PLAYER)
    self.assertEqual(self.board[self.moves[0] - 1], 'X')

  def test_start_checks_if_game_is_over(self):
    return_values = [False, True]
    self.mock_board_analyzer.game_over.side_effect = return_values
    self.engine.start(src.game.PLAYER_VS_PLAYER)
    self.mock_board_analyzer.assert_has_calls([call.game_over(self.board)])

