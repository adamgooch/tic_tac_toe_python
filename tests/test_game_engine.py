import unittest
import sys

from src.game_engine import GameEngine
from mock import *

class TestGameEngine(unittest.TestCase):

  def setUp(self):
    self.mock_stdout = Mock()
    sys.stdout = self.mock_stdout
    self.mock_board = Mock()
    self.game = GameEngine(self.mock_board)

  def test_displays_board(self):
    self.game.start()
    self.mock_board.as_string.assert_called_with()


