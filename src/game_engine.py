class GameEngine:

  def __init__(self, board):
    self.board = board

  def start(self):
    print(self.board.as_string())

