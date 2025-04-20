from Chess.vars import *
def rook(piece_pos: str, board: list[str], q=0):
    pos = []
    piece = board[board_sqs.index(piece_pos)]

    piece_index = board_sqs.index(piece_pos) 
    piece_index2 = piece_index
    
    piece_sq = board_sqs[piece_index] # find the pos of the piece in algebric notation 
    file,rank = piece_sq
    
    color = piece[:3]

    if (piece != BROOK and piece != WROOK and q==0):
        return [-1] 

    # vertical movements 
    for i in range(8):
        piece_index -= 8
        if (piece_index > 0):
            if (board_sqs[piece_index][0] == file):
                if ( board[piece_index] == EMPTY):
                    pos.append(piece_index)
                elif (board[piece_index][:3] != color):
                    pos.append(piece_index)
                    break
                elif (board[piece_index][:3] == color):
                    break

        piece_index2 += 8
        if (piece_index2 <= 63):
            if (board_sqs[piece_index2][0] == file):
                if (board[piece_index2] == EMPTY):
                    pos.append(piece_index2)
                
                elif (board[piece_index2][:3] != color):
                    pos.append(piece_index2)
                    break 
                
                elif (board[piece_index2][:3] == color):
                    break
    


    piece_index = board_sqs.index(piece_pos) 
    piece_index2 = piece_index 
    # horizontal movements
    for i in range(8):
        piece_index  -= 1
        piece_index2 += 1 
        if (piece_index > 0):
            if (board_sqs[piece_index][1] == rank):
                if ( board[piece_index] == EMPTY):
                    pos.append(piece_index)
                elif (board[piece_index][:3] != color):
                    pos.append(piece_index)
                    break
                elif (board[piece_index][:3] == color):
                    break


        if (piece_index2 <= 63):
            if (board_sqs[piece_index2][1] == rank):
                if (board[piece_index2] == EMPTY):
                    pos.append(piece_index2)
                
                elif (board[piece_index2][:3] != color):
                    pos.append(piece_index2)
                    break 
                
                elif (board[piece_index2][:3] == color):
                    break
    
    return set(pos)

