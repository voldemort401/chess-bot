import Chess 
from pieces import pawn
chess = Chess.Chess()
board = chess.Board()
i = 0 
while True:
    i+=1
    a = input("move?")
    print(board.Move(a))
    

#moves = chess.PseudolegalMovegen(board())
#from Chess import chess
#print(Chess.chess.filterPseudolegalmoves(moves,board()))