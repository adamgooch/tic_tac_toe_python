class BoardAnalyzer:

  def game_over(self, board):
    if self.open_squares(board) == 0:
      self.winner = 'Nobody'
      return True

  def open_squares(self, board):
    open_squares = 0
    for square in board:
      if square != 'X' and square != 'O':
        open_squares += 1
    return open_squares
