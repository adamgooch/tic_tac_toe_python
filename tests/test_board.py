import unittest

from src.board import Board

class TestBoard(unittest.TestCase):

  def test_default_board_as_string(self):
    board = Board()
    line_1 = "     |     |     \n"
    line_2 = "  0  |  1  |  2  \n"
    line_3 = "     |     |     \n"
    line_4 = "-----+-----+-----\n"
    line_5 = "     |     |     \n"
    line_6 = "  3  |  4  |  5  \n"
    line_7 = "     |     |     \n"
    line_8 = "-----+-----+-----\n"
    line_9 = "     |     |     \n"
    line_10 = "  6  |  7  |  8  \n"
    line_11 = "     |     |     \n"
    desired_result = line_1.join([line_2,
      line_3, line_4, line_5, line_6, line_7, line_8, line_9, line_10, line_11])
    self.assertEqual(board.as_string(), desired_result)

  def test_given_board_as_string(self):
    board = Board(['0', 'X', '2', '3', '4', '5', '6', '7', '8'])
    line_1 = "     |     |     \n"
    line_2 = "  0  |  X  |  2  \n"
    line_3 = "     |     |     \n"
    line_4 = "-----+-----+-----\n"
    line_5 = "     |     |     \n"
    line_6 = "  3  |  4  |  5  \n"
    line_7 = "     |     |     \n"
    line_8 = "-----+-----+-----\n"
    line_9 = "     |     |     \n"
    line_10 = "  6  |  7  |  8  \n"
    line_11 = "     |     |     \n"
    desired_result = line_1.join([line_2,
      line_3, line_4, line_5, line_6, line_7, line_8, line_9, line_10, line_11])
    self.assertEqual(board.as_string(), desired_result)

#if __name__ == '__main__':
#  unittest.main()
