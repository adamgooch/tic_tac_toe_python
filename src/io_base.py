import abc

class IoBase(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def greet(self):
    """Display a greeting."""

  @abc.abstractmethod
  def get_play_type(self):
    """Return a number from within the range of play types."""
    return

  @abc.abstractmethod
  def get_move(self, board):
    """Given a board array, return a number within the range of the board array."""
    return

  @abc.abstractmethod
  def display_board(self, board):
    """Display the given board array in a proper format."""

  @abc.abstractmethod
  def display_game_over_message(self, winner):
    """Display an appropriate message given a specific winner string."""

  @abc.abstractmethod
  def get_play_again(self):
    """Present an option for the user to play again, return a 'y' for yes."""
    return
