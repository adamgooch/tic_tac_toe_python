import sys

from board_analyzer import BoardAnalyzer
from copy import copy

class Ai:
  PLAYER_O = 1
  PLAYER_X = -1

  def get_move(self, board, player):
    self.board_analyzer = BoardAnalyzer()
    return self.best_move(board, player)

  def best_move(self, board, player):
      alpha = -sys.maxint
      beta = sys.maxint
      available_squares = self.board_analyzer.get_available_squares(board)
      best_score = sys.maxint
      best_square = available_squares[0]
      for square in available_squares:
        new_board = copy(board)
        new_board[square] = self.player_mark(player)
        score = self.negamax(new_board, -player, alpha, beta)
        if score < best_score:
          best_score = score
          best_square = square
      return best_square

  def negamax(self, board, player, alpha, beta):
    if self.board_analyzer.game_over(board):
      return player * self.value_of_node()
    maximum = -sys.maxint
    available_squares = self.board_analyzer.get_available_squares(board)
    for square in available_squares:
      new_board = copy(board)
      new_board[square] = self.player_mark(player)
      result = -self.negamax(new_board, -player, -beta, -alpha)
      if result > maximum:
        maximum = result
      if result > alpha:
        alpha = result
      if alpha >= beta:
        return alpha
    return maximum

  def player_mark(self, player):
    return 'O' if player == self.PLAYER_O else 'X'

  def value_of_node(self):
    if self.board_analyzer.winner == 'X':
      return self.PLAYER_X
    elif self.board_analyzer.winner == 'O':
      return self.PLAYER_O
    else:
      return 0
