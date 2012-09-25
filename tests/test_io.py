import unittest
import sys

from src.io import Io
from mock import *

class TestIo(unittest.TestCase):

  def setUp(self):
    self.io = Io()

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
    self.mock_stdout.assert_has_calls([call.write('Welcome to Tic Tac Toe')])

  def test_get_play_type_presents_the_list_of_play_types(self):
    self.mock_stdin.readline.return_value = "3\n"
    self.io.get_play_type()
    self.mock_stdout.assert_has_calls([call.write('1: Player vs. Computer'),
                                       call.write('2: Player vs. Player'),
                                       call.write('3: Computer vs. Computer')], any_order=True)

  def test_get_play_type_returns_a_valid_play_type(self):
    self.mock_stdin.readline.return_value = "1\n"
    self.assertEqual(1, self.io.get_play_type())
    self.mock_stdin.readline.return_value = "3\n"
    self.assertEqual(3, self.io.get_play_type())

  def test_get_play_type_rejects_invalid_numbers(self):
    return_values = ["2\n", "4\n"]
    self.mock_stdin.readline.side_effect = lambda: return_values.pop()
    self.io.get_play_type()
    self.mock_stdout.assert_has_calls([call.write('Invalid Play Type')])

  def test_get_move_asks_for_the_move(self):
    self.mock_stdin.readline.return_value = "1\n"
    self.io.get_move()
    self.mock_stdout.assert_has_calls([call.write('What is your move? ')])

  def test_get_move_rejects_invalid_input(self):
    return_values = ["2\n", "what\n"]
    self.mock_stdin.readline.side_effect = lambda: return_values.pop()
    self.io.get_move()
    self.mock_stdout.assert_has_calls([call.write('Invalid Entry')])

