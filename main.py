import Chess 
from pieces import pawn
chess = Chess.Chess("r1b2rk1/1p1nbppp/pq1p4/3B4/P2NP3/2N1p3/1PP3PP/R2Q1R1K w - -")
print(chess.get_moves())
print(chess.move('Bc4'))