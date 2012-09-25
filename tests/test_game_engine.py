import unittest
import sys

from src.game_engine import GameEngine
from mock import *

class TestGameEngine(unittest.TestCase):

  def test_displays_board(self):
    engine = GameEngine()


