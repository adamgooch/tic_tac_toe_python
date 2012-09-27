import unittest
import sys

from src.io import Io
from mock import *

class TestIo(unittest.TestCase):

  def setUp(self):
    self.io = Io()
    self.board = ['1', '2', '3', '4', 'X', '6', '7', '8', '9']

    self.mock_stdin = Mock(spec=sys.stdin)
    self.real_stdin = sys.stdin
    sys.stdin = self.mock_stdin

    self.mock_stdout = Mock(spec=sys.stdout)
    self.real_stdout = sys.stdout
    sys.stdout = self.mock_stdout

  def tearDown(self):
    sys.stdin = self.real_stdin
    sys.stdout = self.real_stdout

  def test_greet_welcomes_the_user(self):
    self.io.greet()
    self.mock_stdout.assert_has_calls([call.write(self.io.GREETING)])

  def test_get_play_type_presents_the_list_of_play_types(self):
    self.mock_stdin.readline.return_value = "3\n"
    self.io.get_play_type()
    self.mock_stdout.assert_has_calls([call.write(''.join(self.io.SHOW_PLAY_TYPES))])

  def test_get_play_type_returns_a_valid_play_type(self):
    self.mock_stdin.readline.return_value = "1\n"
    self.assertEqual(1, self.io.get_play_type())
    self.mock_stdin.readline.return_value = "3\n"
    self.assertEqual(3, self.io.get_play_type())

  def test_get_play_type_rejects_invalid_numbers(self):
    return_values = ["4\n", "2\n"]
    self.mock_stdin.readline.side_effect = return_values
    self.io.get_play_type()
    self.mock_stdout.assert_has_calls([call.write(self.io.INVALID_PLAY_TYPE)])

  def test_get_move_asks_for_the_move(self):
    self.mock_stdin.readline.return_value = "1\n"
    self.io.get_move(self.board)
    self.mock_stdout.assert_has_calls([call.write(self.io.MOVE_QUERY)])

  def test_get_move_rejects_invalid_input(self):
    return_values = ["invalid\n", "2\n"]
    self.mock_stdin.readline.side_effect = return_values
    self.io.get_move(self.board)
    self.mock_stdout.assert_has_calls([call.write(self.io.INVALID_ENTRY)])

  def test_get_move_rejects_numbers_that_arent_playable(self):
    return_values = ["10\n", "2\n"]
    self.mock_stdin.readline.side_effect = return_values
    self.io.get_move(self.board)
    self.mock_stdout.assert_has_calls([call.write(self.io.INVALID_MOVE)])

  def test_display_board_prints_the_board(self):
    expected_result = """
         |     |
      %s  |  %s  |  %s
         |     |
    -----+-----+-----
         |     |
      %s  |  %s  |  %s
         |     |
    -----+-----+-----
         |     |
      %s  |  %s  |  %s
         |     |
    """ % ('1', '2', '3', '4', 'X', '6', '7', '8', '9')
    self.io.display_board(self.board)
    self.mock_stdout.assert_has_calls([call.write(expected_result)])

  def test_display_game_over_message_shows_appropriate_message(self):
    self.io.display_game_over_message('Nobody')
    self.mock_stdout.assert_has_calls([
      call.write(str('Nobody ' + self.io.WINNING_MESSAGE).center(self.io.MESSAGE_WIDTH))])
    self.io.display_game_over_message('X')
    self.mock_stdout.assert_has_calls([
      call.write(str('X ' + self.io.WINNING_MESSAGE).center(self.io.MESSAGE_WIDTH))])

  def test_get_play_again_asks_user_if_she_wants_to_play_again(self):
    self.mock_stdin.readline.return_value = 'y\n'
    self.io.get_play_again()
    self.mock_stdout.assert_has_calls([call.write(self.io.PLAY_AGAIN_QUERY)])

  def test_get_play_again_returns_y_if_the_answer_is_yes(self):
    self.mock_stdin.readline.return_value = 'y\n'
    self.assertEquals('y', self.io.get_play_again())
