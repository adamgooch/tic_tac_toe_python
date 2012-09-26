from src.game import Game
from src.io import Io
from src.game_engine import GameEngine
from src.board_analyzer import BoardAnalyzer
from src.ai import Ai

io = Io()
ai = Ai()
board_analyzer = BoardAnalyzer()
engine = GameEngine(['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    io, ai, board_analyzer)
game = Game(io, engine)
game.begin()
