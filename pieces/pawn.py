## broken
from Chess.vars import *
def pawn(piece_pos:str, board:list[str]):
    piece_index = board_sqs.index(piece_pos)
    file,rank = piece_pos
    color = board[piece_index][:3]

    plegal_sq = []
    canMove2squares = False 
    if (color == WHITE or rank == '2'):
        canMove2squares =  True 
    print(color, rank)
    if (color == BLACK and rank == '7'):
        canMove2squares = True


    for i in range(2):  ## because the maximum moves the pawn can do in one turn is 2 
        if (canMove2squares):
            if (color == WHITE):
                piece_index-=8
                plegal_sq.append(piece_index)
            elif (color == BLACK):
                piece_index+=8 
                plegal_sq.append(piece_index)
    ## ENPASSANT
    return plegal_sq
