import game

class Board:

  def __init__(self, board_array = None):
    if board_array == None:
      self.board_array = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    else:
      self.board_array = board_array

  def put_mark_in_square(self, mark, square):
    if self.square_is_available(square - 1):
      self.board_array[square - 1] = mark #-1 accounts for 0 based array index
      return True
    else:
      return False

  def square_is_available(self, square):
    if self.board_array[square] == game.PLAYER_ONE or self.board_array[square] == game.PLAYER_TWO:
      return False
    else:
      return True

  def squares(self):
    return len(self.board_array)

  def get_square(self, square):
    return self.board_array[square - 1] #-1 accounts for 0 based array index

  def get_available_squares(self):
    available_squares = []
    for square in range(len(self.board_array)):
      if self.square_is_available(square):
        available_squares.append(square + 1) #+1 is to return square number vs. array index
    return available_squares

  def no_open_squares(self):
    if len(self.get_available_squares()) == 0:
      return True
    else:
      return False
