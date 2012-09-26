class Ai:

  def get_move(self, board):
    index = 0
    for square in board:
      if square != 'X' and square != 'O':
        return index
      index += 1
