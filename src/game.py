from board import Board
from copy import copy

PLAYER_VS_AI = 1
PLAYER_VS_PLAYER = 2
AI_VS_AI = 3

PLAYER_ONE = 'X'
PLAYER_TWO = 'O'

class Game:

  AFFIRMATIVE_ANSWER = 'y'

  def __init__(self, io, engine):
    self.io = io
    self.engine = engine
    self.play_again = True

  def begin(self):
    while self.play_again:
      self.io.greet()
      self.play_type = self.io.get_play_type()
      self.engine.start(self.play_type, Board())
      self.ask_to_play_again()

  def ask_to_play_again(self):
    play_again_answer = self.io.get_play_again()
    if play_again_answer == self.AFFIRMATIVE_ANSWER:
      self.play_again = True
    else:
      self.play_again = False
