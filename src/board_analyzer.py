import game

class BoardAnalyzer:

  win_sets = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
              [1, 4, 7], [2, 5, 8], [3, 6, 9],
              [1, 5, 9], [3, 5, 7]]

  NO_WINNER = 'Nobody'

  def game_over(self, board):
    if self.is_winner(game.PLAYER_ONE, board):
      return True
    elif self.is_winner(game.PLAYER_TWO, board):
      return True
    elif board.no_open_squares():
      self.winner = self.NO_WINNER
      return True
    return False

  def is_winner(self, player, board):
    for win_set in self.win_sets:
      count = 0
      for square in win_set:
        if board.get_square(square) == player:
          count += 1
      if count == len(win_set):
        self.winner = player
        return True
