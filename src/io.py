class Io:

  def get_move(self):
    while True:
      try:
        user_input = input('What is your move? ')
        move = int(user_input)
        break
      except:
        print('Invalid Entry')
    return move
