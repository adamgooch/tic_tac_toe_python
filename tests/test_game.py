import unittest
import sys

from src.game import Game
from mock import *

class TestGame(unittest.TestCase):

  def setUp(self):
    self.real_stdout = sys.stdout
    self.mock_stdout = Mock()
    sys.stdout = self.mock_stdout
    self.mock_io = Mock()
    self.game = Game(self.mock_io)

  def tearDown(self):
    sys.stdout = self.real_stdout

  def test_start_gives_welcome_message(self):
    self.game.start()
    self.mock_stdout.assert_has_calls([call.write('Welcome To Tic Tac Toe')])

  def test_start_sets_the_play_type(self):
    self.mock_io.get_play_type.return_value = 2
    self.game.start()
    self.mock_io.assert_has_calls([call.get_play_type()])
    self.assertEqual(self.game.play_type, self.game.P_VS_P)
