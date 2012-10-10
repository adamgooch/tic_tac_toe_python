import abc
from io_base import IoBase

class ConsoleIo(IoBase):

  NUMBER_OF_PLAY_TYPES = 3
  MESSAGE_WIDTH = 26

  SHOW_PLAY_TYPES = """
There are 3 ways to play
------------------------
1: Player vs. Computer
2: Player vs. Player
3: Computer vs. Computer
"""
  GREETING = 'Welcome to Tic Tac Toe'
  PLAY_TYPE_QUERY = 'How do you want to play? '
  INVALID_PLAY_TYPE = 'Invalid Play Type'
  MOVE_QUERY = '(0 to Quit) What is your move? '
  INVALID_ENTRY = 'Invalid Entry\n'
  INVALID_MOVE = 'Invalid Move\n'
  WINNING_MESSAGE = 'WINS!\n'
  PLAY_AGAIN_QUERY = 'Would you like to play again? (y or n) '

  def greet(self):
    print self.GREETING

  def get_play_type(self):
    while True:
      print self.SHOW_PLAY_TYPES
      play_type = self.get_valid_number(self.PLAY_TYPE_QUERY)
      if play_type <= self.NUMBER_OF_PLAY_TYPES and play_type > 0:
        return play_type
      else:
        self.clear_terminal()
        print(self.INVALID_PLAY_TYPE)

  def get_move(self, board):
    while True:
      user_input = self.get_valid_number(self.MOVE_QUERY)
      if user_input >= 0 and user_input <= board.squares():
        return user_input
      else:
        print(self.INVALID_MOVE)

  def get_valid_number(self, prompt):
    while True:
      try:
        user_input = raw_input(prompt)
        move = int(user_input)
        return move
      except(ValueError):
        print(self.INVALID_ENTRY)

  def display_board(self, board):
    self.clear_terminal()
    print """
         |     |
      %s  |  %s  |  %s
         |     |
    -----+-----+-----
         |     |
      %s  |  %s  |  %s
         |     |
    -----+-----+-----
         |     |
      %s  |  %s  |  %s
         |     |
    """ % (board.get_square(1),
           board.get_square(2),
           board.get_square(3),
           board.get_square(4),
           board.get_square(5),
           board.get_square(6),
           board.get_square(7),
           board.get_square(8),
           board.get_square(9))

  def display_game_over_message(self, winner):
    full_message = ' '.join([winner, self.WINNING_MESSAGE])
    print str(full_message).center(self.MESSAGE_WIDTH)

  def get_play_again(self):
    answer = raw_input(self.PLAY_AGAIN_QUERY)
    return answer

  def clear_terminal(self):
    print chr(27) + "[2J"

