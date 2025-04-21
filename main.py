import Chess 
from pieces import pawn
chess = Chess.Chess()
board = chess.Board(fen="r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1")
print(board.move("O-O"))