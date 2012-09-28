import game

class BoardAnalyzer:

  win_sets = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
              [0, 3, 6], [1, 4, 7], [2, 5, 8],
              [0, 4, 8], [2, 4, 6]]

  NO_WINNER = 'Nobody'

  def game_over(self, board):
    if self.get_winner(game.PLAYER_ONE, board):
      return True
    elif self.get_winner(game.PLAYER_TWO, board):
      return True
    elif not self.any_open_squares(board):
      self.winner = self.NO_WINNER
      return True
    return False

  def get_winner(self, player, board):
    for win_set in self.win_sets:
      count = 0
      for square in win_set:
        if board[square] == player:
          count += 1
      if count == len(win_set):
        self.winner = player
        return True

  def any_open_squares(self, board):
    for square in board:
      if self.square_is_available(square):
        return True
    return False

  def get_available_squares(self, board):
    available_squares = []
    index = 0
    for square in board:
      if self.square_is_available(square):
        available_squares.append(index)
      index += 1
    return available_squares

  def square_is_available(self, square_contents):
    return False if square_contents == game.PLAYER_ONE or square_contents == game.PLAYER_TWO else True
