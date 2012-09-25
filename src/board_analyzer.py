class BoardAnalyzer:

  win_sets = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
              [0, 3, 6], [1, 4, 7], [2, 5, 8],
              [0, 4, 8], [2, 4, 6]]

  def game_over(self, board):
    if self.winner('X', board):
      return True
    elif self.winner('O', board):
      return True
    elif self.open_squares(board) == 0:
      self.winner = 'Nobody'
      return True
    return False

  def winner(self, player, board):
    for win_set in self.win_sets:
      count = 0
      for square in win_set:
        if board[square] == player:
          count += 1
      if count == 3:
        self.winner = player
        return True

  def open_squares(self, board):
    open_squares = 0
    for square in board:
      if square != 'X' and square != 'O':
        open_squares += 1
    return open_squares
