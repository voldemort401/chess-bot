import Chess 
from pieces import rook 
chess = Chess.Chess()
board = chess.Board("8/3k4/8/8/1nb5/1B6/3K4/1r6 w - - 0 1")
print(Chess.chess.isCheckMate(board(), Chess.vars.WHITE))
#print(rook.rook('b1', board()))