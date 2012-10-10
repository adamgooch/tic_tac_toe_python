import unittest
import src.game

from src.board import Board

class TestBoard(unittest.TestCase):

  def setUp(self):
    self.board = Board()

  def test_put_mark_in_square_is_true_when_the_square_has_not_been_taken(self):
    self.assertTrue(self.board.put_mark_in_square(src.game.PLAYER_ONE, 1))

  def test_put_mark_in_square_is_false_when_the_square_has_already_been_taken(self):
    self.board.put_mark_in_square(src.game.PLAYER_ONE, 1)
    self.assertFalse(self.board.put_mark_in_square(src.game.PLAYER_ONE, 1))

  def test_square_is_available_is_true_when_x_or_o_has_not_taken_it(self):
    self.assertTrue(self.board.square_is_available(1))

  def test_square_is_available_is_false_when_it_has_been_taken(self):
    self.board.put_mark_in_square(src.game.PLAYER_ONE, 1)
    self.assertFalse(self.board.square_is_available(0))

  def test_squares_returns_the_number_of_squares_on_the_board(self):
    self.assertEqual(9, self.board.number_of_squares())

  def test_get_square_returns_the_contents_of_the_given_square(self):
    self.assertEqual('1', self.board.get_square(1))
    self.board.put_mark_in_square(src.game.PLAYER_ONE, 1)
    self.assertEqual(src.game.PLAYER_ONE, self.board.get_square(1))

  def test_get_available_squares_returns_an_array_of_the_squares_not_taken(self):
    self.board.put_mark_in_square(src.game.PLAYER_ONE, 1)
    self.board.put_mark_in_square(src.game.PLAYER_ONE, 3)
    self.board.put_mark_in_square(src.game.PLAYER_ONE, 5)
    self.assertEqual([2, 4, 6, 7, 8, 9], self.board.get_available_squares())

  def test_no_open_squares_should_be_true_when_all_squares_have_been_taken(self):
    for square in range(9):
      self.board.put_mark_in_square(src.game.PLAYER_ONE, square + 1)
    self.assertTrue(self.board.no_open_squares())

  def test_no_open_squares_should_be_false_when_any_square_has_not_been_taken(self):
    for square in range(8):
      self.board.put_mark_in_square(src.game.PLAYER_ONE, square + 1)
    self.assertFalse(self.board.no_open_squares())
