import unittest
import sys
import src.game

from mock import *

class TestGame(unittest.TestCase):

  def setUp(self):
    self.mock_io = Mock()
    self.mock_engine = Mock()
    self.game = src.game.Game(self.mock_io, self.mock_engine)

  def test_begin_greets_the_user(self):
    self.game.begin()
    self.mock_io.assert_has_calls([call.greet()])

  def test_begin_sets_the_play_type(self):
    self.mock_io.get_play_type.return_value = src.game.PLAYER_VS_PLAYER
    self.game.begin()
    self.mock_io.assert_has_calls([call.get_play_type()])
    self.assertEqual(self.game.play_type, src.game.PLAYER_VS_PLAYER)

  def test_begin_starts_the_game_engine(self):
    self.game.begin()
    self.mock_engine.assert_has_calls([call.start(self.mock_io.get_play_type())])
