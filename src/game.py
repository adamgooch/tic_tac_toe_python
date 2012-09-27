from io import Io

PLAYER_VS_AI = 1
PLAYER_VS_PLAYER = 2
AI_VS_AI = 3

class Game:

  def __init__(self, io, engine):
    self.io = io
    self.engine = engine

  def begin(self):
    self.io.greet()
    self.play_type = self.io.get_play_type()
    self.engine.start(self.play_type)
    self.play_again()

  def play_again(self):
    play_again_answer = self.io.get_play_again()
    if play_again_answer == 'y':
      self.begin()

