class Io:

  def greet(self):
    print('Welcome to Tic Tac Toe')
    print

  def get_play_type(self):
    print('There are 3 ways to play')
    print('------------------------')
    print('1: Player vs. Computer')
    print('2: Player vs. Player')
    print('3: Computer vs. Computer')
    print
    play_type = self.get_valid_number('How do you want to play? ')
    print
    if play_type < 4 and play_type > 0:
      return play_type
    else:
      self.clear_terminal()
      print('Invalid Play Type')
      print
      self.get_play_type()

  def get_move(self):
    return self.get_valid_number('What is your move? ')

  def get_valid_number(self, prompt):
    while True:
      try:
        user_input = input(prompt)
        move = int(user_input)
        return move
      except:
        print('Invalid Entry')

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
""" % (board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])

  def display_game_over_message(self, winner):
    print """%s Wins!""" % winner

  def clear_terminal(self):
    print chr(27) + "[2J"

