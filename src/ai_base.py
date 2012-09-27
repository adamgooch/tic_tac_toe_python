import abc

class AiBase(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def get_move(board, player):
    """Given a board array and a player, 'X' or 'O', return
       an available move as an index of the board."""
