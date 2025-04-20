import Chess 
from pieces import pawn
chess = Chess.Chess()
board = chess.Board(fen="8/2r3R1/1k6/8/Ppr5/4K3/6R1/8 w - - 0 1")
print(chess.get_moves(board()))