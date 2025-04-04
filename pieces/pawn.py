from Chess.vars import *
def pawn(piece_pos:str, board:list[str]):
    piece_index = board_sqs.index(piece_pos)
    file,rank = piece_pos
    color = board[piece_index][:3]

    plegal_sq = []
    canMove2squares = False 
    if (color == WHITE and rank == '2' and board[piece_index-16] == EMPTY and board[piece_index-8] == EMPTY):
        canMove2squares =  True 
    if (color == BLACK and rank == '7' and board[piece_index+16] == EMPTY and board[piece_index+8] == EMPTY):
        canMove2squares = True
    
    for i in range(2):  ## because the maximum moves the pawn can do in one turn is 2 
        if (canMove2squares):
            if (color == WHITE):
                piece_index-=8
                plegal_sq.append(piece_index)
            elif (color == BLACK):
                piece_index+=8 
                plegal_sq.append(piece_index)
        else:
            if (color == WHITE and board[piece_index-8] == EMPTY):
                plegal_sq.append(piece_index-8)
            elif (color == BLACK and board[piece_index+8] == EMPTY):
                plegal_sq.append(piece_index+8)

    ## currently if the piece is in the edges some funky stuff happens FIXIT LATER 
    if (color == WHITE and board[piece_index-9][:3] != color and board[piece_index-9] != EMPTY):
        plegal_sq.append(piece_index-9)          
    if (color == WHITE and board[piece_index-7][:3] != color and board[piece_index-7] != EMPTY):
        plegal_sq.append(piece_index-7)

    if (color == BLACK and board[piece_index+9][:3] != color and board[piece_index+9] != EMPTY):
        plegal_sq.append(piece_index+9)
    if (color == BLACK and board[piece_index+7][:3] != color and board[piece_index+7] != EMPTY):
        plegal_sq.append(piece_index+7)
    
    ## enpassant
    possible_enpassant_squares = []
    piece_index                = board_sqs.index(piece_pos) 
    if (color == WHITE):
        possible_enpassant_squares.append(piece_index-9)
        possible_enpassant_squares.append(piece_index-7)
    elif (color == BLACK):
        possible_enpassant_squares.append(piece_index+9)
        possible_enpassant_squares.append(piece_index+7)

    

    return plegal_sq
