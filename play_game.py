from src.game import Game
from src.io import Io
from src.game_engine import GameEngine

io = Io()
engine = GameEngine(['1', '2', '3', '4', '5', '6', '7', '8', '9'], io)
game = Game(io, engine)
game.begin()
