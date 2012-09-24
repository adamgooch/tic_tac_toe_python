class Board:

  def __init__(self, default_board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']):
    self.board = default_board

  def as_string(self):
    line_1 =    "     |     |     \n"
    line_2 = "  " + self.board[0] + "  |  " + self.board[1] + "  |  " + self.board[2] + "  \n"
    line_3 = "     |     |     \n"
    line_4 = "-----+-----+-----\n"
    line_5 = "     |     |     \n"
    line_6 = "  " + self.board[3] + "  |  " + self.board[4] + "  |  " + self.board[5] + "  \n"
    line_7 = "     |     |     \n"
    line_8 = "-----+-----+-----\n"
    line_9 = "     |     |     \n"
    line_10 = "  " + self.board[6] + "  |  " + self.board[7] + "  |  " + self.board[8] + "  \n"
    line_11 = "     |     |     \n"

    return ''.join([line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9, line_10, line_11])

  def stupid(self):
    return "What?"
