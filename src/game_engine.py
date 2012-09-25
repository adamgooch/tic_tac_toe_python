from board import Board

class GameEngine:

  def __init__(self, board, io, board_analyzer):
    self.board = board
    self.io = io
    self.board_analyzer = board_analyzer

  def start(self, play_type):
    self.play_type = play_type
    while not(self.board_analyzer.game_over(self.board)):
      self.io.display_board(self.board)
      self.place_move()

  def place_move(self):
    move = self.io.get_move()
    self.board[move - 1] = 'X'
