import sys
import abc
import game
import console_io

from ai_base import AiBase
from board_analyzer import BoardAnalyzer
from copy import deepcopy

class NegamaxAi(AiBase):
  PLAYER_O = 1
  PLAYER_X = -1
  NEUTRAL = 0

  def get_move(self, board, player):
    self.board_analyzer = BoardAnalyzer()
    return self.best_move(board, player)

  def best_move(self, board, player):
      alpha = -sys.maxint
      beta = sys.maxint
      available_squares = board.get_available_squares()
      best_score = sys.maxint
      best_square = available_squares[0]
      for square in available_squares:
        new_board = deepcopy(board)
        new_board.put_mark_in_square(self.player_mark(player), square)
        score = self.negamax(new_board, -player, alpha, beta)
        if score < best_score:
          best_score = score
          best_square = square
      return best_square

  def negamax(self, board, player, alpha, beta):
    if self.board_analyzer.game_over(board):
      return player * self.value_of_node()
    maximum = -sys.maxint
    available_squares = board.get_available_squares()
    for square in available_squares:
      new_board = deepcopy(board)
      new_board.put_mark_in_square(self.player_mark(player), square)
      result = -self.negamax(new_board, -player, -beta, -alpha)
      if result > maximum:
        maximum = result
      if result > alpha:
        alpha = result
      if alpha >= beta:
        return alpha
    return maximum

  def player_mark(self, player):
    return game.PLAYER_TWO if player == self.PLAYER_O else game.PLAYER_ONE

  def value_of_node(self):
    if self.board_analyzer.winner == game.PLAYER_ONE:
      return self.PLAYER_X
    elif self.board_analyzer.winner == game.PLAYER_TWO:
      return self.PLAYER_O
    else:
      return self.NEUTRAL
