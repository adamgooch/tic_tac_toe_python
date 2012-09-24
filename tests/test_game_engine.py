import unittest
import sys
from cStringIO import StringIO

from src.game_engine import GameEngine

class TestGameEngine(unittest.TestCase):

  def setUp(self):
    real_stdout = sys.stdout
    self.my_stdout = StringIO()
    sys.stdout = self.my_stdout

  def test_welcome_screen(self):
    game = GameEngine()
    game.start()
    self.assertEqual(self.my_stdout.getvalue(), 'Welcome To Tic Tac Toe\n')
