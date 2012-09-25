import unittest
import sys
import threading
import time

import src.io
from mock import *

class TestIo(unittest.TestCase):

  def setUp(self):
    self.io = src.io.Io()

    self.mock_stdin = Mock(spec=sys.stdin)
    self.real_stdin = sys.stdin
    sys.stdin = self.mock_stdin

    self.mock_stdout = Mock(spec=sys.stdout)
    self.real_stdout = sys.stdout
    sys.stdout = self.mock_stdout

  def tearDown(self):
    sys.stdin = self.real_stdin
    sys.stdout = self.real_stdout

  def test_get_move_returns_a_valid_square(self):
    self.mock_stdin.readline.return_value = "4\n"
    self.assertEqual(4, self.io.get_move())
    self.mock_stdin.readline.return_value = "0\n"
    self.assertEqual(0, self.io.get_move())

  def test_get_move_rejects_an_invalid_move(self):
    return_values = ["2\n", "what\n"]
    self.mock_stdin.readline.side_effect = lambda: return_values.pop()
    self.io.get_move()
    self.mock_stdout.assert_has_calls([call.write('Invalid Entry')])
