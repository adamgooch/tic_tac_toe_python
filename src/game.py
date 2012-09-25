from io import Io

class Game:

  P_VS_P = 2

  def __init__(self, io):
    self.io = io

  def start(self):
    print('Welcome To Tic Tac Toe')
    self.play_type = self.io.get_play_type()
    print('Awesome, let\'s do this!')
