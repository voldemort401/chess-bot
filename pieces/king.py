from Chess.vars import *
def king(piece_pos, board: list[str]):
    from Chess.chess import isinCheck
    brd_cpy = board
    if(type(piece_pos) == str):
        current_pos = board_sqs.index(piece_pos)

    elif (type(piece_pos) == int):
        current_pos = piece_pos
        if (current_pos > 63):
            return 'Invalid piece_pos' 
    else:
        return 'Invalid piece_pos' 

    if (board[current_pos] != WKING and board[current_pos] != BKING):
        return -1
 
    color = board[current_pos][:3] 
    possible_moves = []    
    pve9 = pve7 = pve1 = pve8 = True
    nve9 = nve7 = nve1 = nve8 = True

    possible_moves = [current_pos+9 , current_pos-9, current_pos+1 , current_pos-1, current_pos+7, current_pos-7, 
                      current_pos+8, current_pos-8]

    for i in possible_moves[:]:
        if (i > 63):
            possible_moves.remove(i)
            break
        if (board[i][:3] == color):
            possible_moves.remove(i)
    return possible_moves

def castle(piece_pos, board: list, move:str):
    from Chess.chess import isinCheck
    if type(piece_pos) == str:
        current_pos = board_sqs.index(piece_pos)
    else:
        current_pos = piece_pos
    board_cpy = board

    if (board[current_pos] != WKING and board[current_pos] != BKING):
        return -1
    color = board[current_pos][:3] 
    

    if (color == WHITE and king_moved[0] == 0 and rook_moved[0] == 0):
        if (board[current_pos+1] == EMPTY and board[current_pos+2] == EMPTY and move == 'O-O'):  ## kingside castle
            for i in range(2):
                king_pos = current_pos + 2
                rook_pos = king_pos-1
                if (board[63] == WROOK):
                    board[current_pos] = EMPTY
                    board[63]          = EMPTY
                    board[king_pos]    = WKING
                    board[rook_pos]    = WROOK
                    if (isinCheck(board, king_pos)):
                        board = board_cpy
                        return "can't O-O"
                else:
                    return "can't O-O"
            return board
            
        if (board[current_pos-1] == EMPTY and board[current_pos-2] == EMPTY and board[current_pos-3] == EMPTY and move == 'O-O-O'): ## queenside castle
            for i in range(2):
                king_pos = current_pos + i
                rook_pos = king_pos-1

                if (board[56] == WROOK):
                    board[current_pos] = EMPTY
                    board[56]          = EMPTY
                    board[king_pos]    = WKING
                    board[rook_pos]    = WROOK
                    if (isinCheck(board, king_pos)):
                        board = board_cpy
                        return "can't O-O-O"
                else:
                    return "Can't O-O-O"
            return board

    elif (color == BLACK and king_moved[1] == 0 and rook_moved[1] == 0):
        if (board[current_pos+1] == EMPTY and board[current_pos+2] == EMPTY and move == 'O-O'):  ## kingside castle
            for i in range(2):
                king_pos = current_pos + i 
                rook_pos = king_pos-1
                if (board[7] == BROOK):
                    board[current_pos] = EMPTY
                    board[7]          = EMPTY
                    board[king_pos]    = BKING
                    board[rook_pos]    = BROOK
                    if (isinCheck(board, king_pos)):
                        board = board_cpy
                        return "Can't O-O"
                else:
                    return "Can't O-O"
            return board

        if (board[current_pos-1] == EMPTY and board[current_pos-2] == EMPTY and board[current_pos-3] == EMPTY and move == 'O-O-O'): ## queenside castle
            for i in range(2):
                king_pos = current_pos + i
                rook_pos = king_pos-1
                if (board[0] == BROOK):
                    board[current_pos] = EMPTY
                    board[0]          = EMPTY
                    board[king_pos]    = BKING
                    board[rook_pos]    = BROOK
                    if (isinCheck(board, king_pos)):
                        board = board_cpy
                        return "Can't O-O-O"
                else:
                    return "Can't O-O-O"
            return board
    return "Cant castle"