from copy import copy
from io_base import IoBase

PLAYER_VS_AI = 1
PLAYER_VS_PLAYER = 2
AI_VS_AI = 3

class Game:

  NEW_BOARD = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  AFFIRMATIVE_ANSWER = 'y'

  def __init__(self, io, engine):
    self.io = io
    self.engine = engine
    self.play_again = True

  def begin(self):
    while self.play_again:
      self.io.greet()
      self.play_type = self.io.get_play_type()
      self.engine.start(self.play_type, copy(self.NEW_BOARD))
      self.ask_to_play_again()

  def ask_to_play_again(self):
    play_again_answer = self.io.get_play_again()
    if play_again_answer == self.AFFIRMATIVE_ANSWER:
      self.play_again = True
    else:
      self.play_again = False
