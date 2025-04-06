import Chess 
from pieces import pawn
chess = Chess.Chess()
board = chess.Board()
#print(board.Move("Ne4"))
moves = chess.PseudolegalMovegen(board())
from Chess import chess
print(Chess.chess.filterlegalmoves(moves,board()))