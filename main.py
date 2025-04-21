import Chess 
from pieces import pawn
chess = Chess.Chess()
board = chess.Board(fen="6R1/4r3/8/k7/Ppr5/4K3/6R1/8 w - - 3 3")
print(board.move("Kd3"))