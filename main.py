import Chess 
from pieces import rook 
chess = Chess.Chess()
board = chess.Board("rkr5/8/8/8/8/8/r7/1K6 w - - 0 1")
print(Chess.chess.isCheckMate(board(), Chess.vars.WHITE))
#print(rook.rook('b1', board()))