from board import Board

class GameEngine:

  def __init__(self, board, io, board_analyzer):
    self.board = board
    self.io = io
    self.board_analyzer = board_analyzer

  def start(self, play_type):
    self.play_type = play_type
    self.player_one_turn = True
    while not(self.board_analyzer.game_over(self.board)):
      self.io.display_board(self.board)
      self.place_move()
    self.io.display_board(self.board)
    self.io.display_game_over_message(self.board_analyzer.winner)

  def place_move(self):
    if self.player_one_turn:
      move = self.io.get_move()
      if not self.taken(move):
        self.board[move] = 'X'
        self.player_one_turn = False
    else:
      move = self.io.get_move()
      if not self.taken(move):
        self.board[move] = 'O'
        self.player_one_turn = True

  def taken(self, move):
    if self.board[move] == 'X':
      return True
    if self.board[move] == 'O':
      return True
    return False
