from src.game import Game
from src.io import Io
from src.game_engine import GameEngine

game = Game(Io(), GameEngine())
game.begin()
