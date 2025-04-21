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
    possible_moves = [current_pos+9 , current_pos-9, current_pos+1 , current_pos-1, current_pos+7, current_pos-7, 
                      current_pos+8, current_pos-8]

    for i in possible_moves[:]:
        if (i > 63 or i < 0):
            possible_moves.remove(i)
        elif (board[i][:3] == color):
            possible_moves.remove(i)
    return set(possible_moves)


def castle(king_pos, board, move, out=1) -> list:
    from Chess.chess import isinCheck
    if (type(king_pos) == str):
        king_pos = board_sqs.index(king_pos)
    move = move.upper()
    castle_rights = board[67]
    turn          = board[64]
    canCastle=kingSidecastle=queenSidecastle=True
    if (turn == WHITE):
        if (king_moved[0] == 1):
            canCastle = False
        if (isinCheck(board, king_pos)):
            canCastle = False
        if (rook_moved[0] == 1):
            kingSidecastle = False
        if (rook_moved[1] == 1):
            queenSidecastle = False


        if (canCastle):
            if (kingSidecastle and move == 'O-O'):
                for i in range(3):
                    new_king_pos = king_pos + i
                    if (isinCheck(board, new_king_pos) == True):
                        kingSidecastle=False
                        break
                    else:
                        if (i == 2):
                            rook_position = new_king_pos-1
                            if (out == 1):
                                board[king_pos] = EMPTY
                                board[63]       = EMPTY
                                board[new_king_pos] =  WKING
                                board[rook_position] = WROOK
                                board[65] = board[65]+1 #increment the turn 
                                board[66] = board[66]+1 # increment the half move clock
                                kingSidecastle=queenSidecastle=False
                                return board
                return kingSidecastle


            if (queenSidecastle):                
                for i in range(3):
                    new_king_pos = king_pos - i
                    if (isinCheck(board, new_king_pos) == True):
                        queenSidecastle=False
                        break
                    else:
                        if (i == 2):
                            rook_position = new_king_pos+1
                            if (out == 1):
                                board[king_pos] = EMPTY
                                board[56]       = EMPTY
                                board[new_king_pos] = WKING
                                board[rook_position] = WROOK
                                kingSidecastle=queenSidecastle=False
                                board[65] = board[65]+1
                                board[66] = board[66]+1
                                return board
                return queenSidecastle 

        


    elif (turn == BLACK):
        if (king_moved[1] == 1):
            canCastle = False
        if (isinCheck(board, king_pos)):
            canCastle = False
        if (rook_moved[2] == 1):
            kingSidecastle = False
        if (rook_moved[3] == 1):
            queenSidecastle = False


        if (canCastle):
            if (kingSidecastle and move == 'O-O'):
                for i in range(3):
                    new_king_pos = king_pos + i
                    if (isinCheck(board, new_king_pos) == True):
                        kingSidecastle=False
                        break
                    else:
                        if (i == 2):
                            rook_position = new_king_pos-1
                            if (out == 1):
                                board[king_pos] = EMPTY
                                board[7]       = EMPTY
                                board[new_king_pos] = BKING
                                board[rook_position] = BROOK
                                board[66] = board[66]+1
                                return board
                return kingSidecastle


            if (queenSidecastle):                
                for i in range(3):
                    new_king_pos = king_pos - i
                    if (isinCheck(board, new_king_pos) == True):
                        queenSidecastle=False
                        break
                    else:
                        if (i == 2):
                            rook_position = new_king_pos+1
                            if (out == 1):
                                board[king_pos] = EMPTY
                                board[2]       = EMPTY
                                board[new_king_pos] = BKING
                                board[66] = board[66]+1 #increment the half move clock
                                board[rook_position] = BROOK
                                return board
                return queenSidecastle 

        
