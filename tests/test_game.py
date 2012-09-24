import unittest
import sys

from src.game import Game
from mock import *

class TestGame(unittest.TestCase):

  def setUp(self):
    self.real_stdout = sys.stdout
    self.mock_stdout = Mock()
    sys.stdout = self.mock_stdout
    self.game = Game()

  def test_start_gives_welcome_message(self):
    self.game.start()
    self.mock_stdout.assert_has_calls([call.write('Welcome To Tic Tac Toe')])

  def test_start_asks_for_play_type(self):
    self.game.start()
    self.mock_stdout.assert_has_calls([call.write('How do you want to play? ')])

