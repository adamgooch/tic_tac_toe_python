from io import Io

class Game:

  PLAYER_VS_AI = 1
  PLAYER_VS_PLAYER = 2
  AI_VS_AI = 3

  def __init__(self, io, engine):
    self.io = io
    self.engine = engine

  def begin(self):
    self.io.greet()
    self.play_type = self.io.get_play_type()
    self.engine.start(self.play_type)
