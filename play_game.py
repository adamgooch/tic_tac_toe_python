from src.game import Game
from src.console_io import ConsoleIo
from src.game_engine import GameEngine
from src.board_analyzer import BoardAnalyzer
from src.negamax_ai import NegamaxAi

io = ConsoleIo()
ai = NegamaxAi()
board_analyzer = BoardAnalyzer()
engine = GameEngine(io, ai, board_analyzer)
game = Game(io, engine)
game.begin()
