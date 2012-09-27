import unittest
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
    self.mock_engine.assert_has_calls([call.start(self.mock_io.get_play_type(), self.game.NEW_BOARD)])

  def test_play_again_asks_if_the_user_would_like_to_play_again(self):
    self.game.ask_to_play_again()
    self.mock_io.assert_has_calls([call.get_play_again()])

  def test_begin_starts_a_new_game_if_the_answer_is_yes(self):
    self.mock_io.get_play_again.side_effect = [self.game.AFFIRMATIVE_ANSWER, 'n']
    self.game.begin()
    self.mock_io.assert_has_calls([call.greet()])
