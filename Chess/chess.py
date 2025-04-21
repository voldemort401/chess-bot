from Chess.vars import *
from pieces.bishop import bishop
from pieces.king import king, castle
from pieces.queen import queen
from pieces.pawn import pawn
from pieces.rook import rook
from pieces.knight import knight
def generatePseudoLegalMoves(board, piece=None, color=None):
    pseudo_moves        = dict()
    turn                = board[64]
    if (piece != None):
        for i,j in enumerate(board):
         if (j != EMPTY and i < 64):
             position = board_sqs[i]
             if (turn == BLACK or color == BLACK):
                 if (j == BKNIGHT and piece == 'N'):
                     pseudo_moves.update({ position: list(knight( piece_pos=position, board=board)) }) 
                 elif (j == BKING and piece == 'K'):               
                     pseudo_moves.update({ position: list(king(piece_pos=position, board=board))})
                 elif (j == BROOK and piece == 'R'):  
                    pseudo_moves.update({ position:  list( rook(piece_pos=position, board=board))})
                 elif (j == BBISHOP and piece == 'B'): 
                     pseudo_moves.update({ position: list(bishop(piece_pos=position, board=board))})
                 elif (j == BPAWN and piece == ''): 
                     pseudo_moves.update({ position: list(pawn(piece_pos=position, board=board))})
                 elif (j == BQUEEN and piece == 'Q'):        
                     pseudo_moves.update({ position: list(queen(piece_pos=position, board=board))})

             elif (turn == WHITE and color == WHITE):
                 if (j == WKNIGHT and piece == 'N'):                     
                     pseudo_moves.update({ position: list(knight(piece_pos=position, board=board))})
                 elif (j == WKING and piece == 'K'):              
                     pseudo_moves.update({ position: list(king(piece_pos=position, board=board))})
                 elif (j == WROOK and piece == 'R'):
                     pseudo_moves.update({ position: list(rook(piece_pos=position, board=board))})
                 elif (j == WBISHOP and piece == 'B'): 
                     pseudo_moves.update({ position: list(bishop(piece_pos=position, board=board))})
                 elif (j == WPAWN and piece == ''): 
                     pseudo_moves.update({ position: list(pawn(piece_pos=position, board=board))})
                 elif (j == WQUEEN and piece == 'Q'):       
                     pseudo_moves.update({ position: list(queen(piece_pos=position, board=board))})
     
    else:
        for i,j in enumerate(board):
         if (j != EMPTY and i < 64):
             position = board_sqs[i]
             if (turn == BLACK or color == BLACK):
                 if (j == BKNIGHT):
                     pseudo_moves.update({position : list(knight(piece_pos=position, board=board))})
                 if (j == BKING):               
                     pseudo_moves.update({position : list(king(piece_pos=position, board=board))})
                 if (j == BROOK):
                     pseudo_moves.update({position : list(rook(piece_pos=position, board=board))})
                 if (j == BBISHOP): 
                     pseudo_moves.update({position : list(bishop(piece_pos=position, board=board))})
                 if (j == BPAWN): 
                     pseudo_moves.update({position : list(pawn(piece_pos=position, board=board))})
                 if (j == BQUEEN):        
                     pseudo_moves.update({position : list(queen(piece_pos=position, board=board))})

             elif (turn == WHITE or color == WHITE):
                 if (j == WKNIGHT):                     
                     pseudo_moves.update({position : list(knight(piece_pos=position, board=board))})
                 if (j == WKING):              
                     pseudo_moves.update({position : list(king(piece_pos=position, board=board))})
                 if (j == WROOK):
                     pseudo_moves.update({position : list(rook(piece_pos=position, board=board))})
                 if (j == WBISHOP): 
                     pseudo_moves.update({position : list(bishop(piece_pos=position, board=board))})
                 if (j == WPAWN): 
                     pseudo_moves.update({position : list(pawn(piece_pos=position, board=board))})
                 if (j == WQUEEN):       
                     pseudo_moves.update({position : list(queen(piece_pos=position, board=board))})
    
    pseudo_moves = {k:v for k,v in pseudo_moves.items() if v != []} # removes the pieces with no moves
    return pseudo_moves 
 
def isinCheck(board, king_pos, color=None) -> bool | str:
    if (color == None):
        color = board[64]
    
    if (color == WHITE):
        enmy_color = BLACK
    elif (color == BLACK):
        enmy_color = WHITE
    else:
        return f'ERR: Failed to get color color={color} king_pos={king_pos}'
    
    if (type(king_pos) == int):
        if (king(king_pos, board) == []):
            return False
    elif (type(king_pos) == str):
        if (king(board_sqs.index(king_pos), board) == []):
            return False

    black_moves = generatePseudoLegalMoves(board=board, piece=None, color=enmy_color)
    for keys in black_moves:
        squares = black_moves.get(keys)
        if king_pos in squares:
            return True

    return False 

def filterPseudolegalmoves(moves:dict, board, turn = None):
    if (turn == None):
        current_turn = board[64]
    else:
        current_turn = turn
    current_board = board
    
    for keys in moves:
        old_piece_pos = board_sqs.index(keys)
        target_square = moves.get(keys) 
        piece         = board[old_piece_pos]
        for new_piece_pos in target_square:            
            if (board[new_piece_pos] != WKING and board[new_piece_pos] != BKING):
                current_board = [EMPTY if x == old_piece_pos else o for x,o in enumerate(current_board)]
                current_board = [piece if x == new_piece_pos else o for x,o in enumerate(current_board)]

                if (current_turn == WHITE):
                    king_pos = current_board.index(WKING)
                elif (current_turn == BLACK):
                    king_pos = current_board.index(BKING)

                if (isinCheck(current_board, king_pos)):
                    target_square.remove(new_piece_pos)
                
                moves.update({keys: target_square})
                current_board = board
    return moves


def legal_move_gen(board, color = None):
    moves = []
    if (board[64] == BLACK or color == BLACK):
        king_pos = board_sqs[board.index(BKING)]

    elif (board[64] == WHITE or color == WHITE):
        king_pos = board_sqs[board.index(WKING)]

    o_o,o_o_o = (castle(king_pos, board, 'O-O', out=0),  castle(king_pos, board, 'O-O-O', out=0)) 
    if (o_o == True):
        moves.append('O-O')

    if (o_o_o == True):
        moves.append('O-O-O')

    pseudo_legal_moves = generatePseudoLegalMoves(board,piece=None,color=color)
    legal_moves        = filterPseudolegalmoves(pseudo_legal_moves, board, color)
    if (moves != []):
        legal_moves.update({'castle': moves})
    return legal_moves 


def isCheckMate(board, turn):
    if (turn == WHITE):
        king_pos = board.index(WKING)
        oppent_legal_moves = legal_move_gen(board,BLACK)
    elif (turn == BLACK):
        king_pos = board.index(BKING)
        oppent_legal_moves = legal_move_gen(board,WHITE)

    else:
        return f'Invalid Value in the turn:{turn} '
    ## variables 
    legal_moves = legal_move_gen(board)

    king_has_moves = None
    possible_stalemate = None
    
    pieces_with_no_moves = 0
    has_no_moves         = False

    if (len(legal_moves) == 1):
        has_no_moves = True 
    if (has_no_moves == True and len(oppent_legal_moves) == 1):
        return [0,0,1]  # [mate, stalemate, insufficent material]
    print(isinCheck(board,king_pos))
    if (not king_pos in legal_moves):
        if (isinCheck(board, king_pos) == True):
            king_has_moves = False
        elif (isinCheck(board,king_pos) == False):
            possible_stalemate = True
        else:
            return isinCheck(board,king_pos)

    
    if (king_has_moves == False and has_no_moves == True):
        return [1,0,0]
    elif (possible_stalemate == True and has_no_moves == True):
        return [0,1,0]

    return [0,0,0]

def convert_to_san(moves, board):
    starting_squares    = list(moves.keys())
    squares             = list(moves.values())
    piece               = board[board_sqs.index(starting_squares[0])]
    color               = piece[:3]
    enemy_color         = BLACK if color == WHITE else WHITE
    
    brd_cpy             = board.copy()
    enemy_king_pos      = board.index(BKING) if enemy_color == BLACK else board.index(WKING)
    capturing=checking  = False
    mvs                 = []    
    for i,j in enumerate(squares):
        piece               = board[board_sqs.index(starting_squares[i])]
        for x,o in enumerate(j):
            start = board_sqs.index(starting_squares[i])
            san = board_sqs[o]

            if (board[o] != EMPTY):
                if (piece != BPAWN or piece != WPAWN):
                    san = 'x'+san
                else:
                    san = start+'x'+san

            if (piece == WQUEEN or piece == BQUEEN):
                san = 'Q'+san
            if (piece == WKING or piece == BKING):
                san = 'K'+san
            if (piece == WKNIGHT or piece == BKNIGHT):
                san = 'N'+san
            if (piece == WROOK or piece == BROOK):
                san = 'R'+san
            if (piece == WBISHOP or piece == BBISHOP):
                san = 'B'+san
            brd_cpy[start] = EMPTY
            brd_cpy[o]     = piece

            if (isinCheck(board=brd_cpy,king_pos=enemy_king_pos, color=enemy_color)):
                san = san+'+'

            if (san in mvs):
                files,ranks = starting_squares[i]
                if (san.__contains__('x')):
                    san = list(san)
                    san.insert(1,files)
                    san = "".join(san)
                else:
                    san = list(san)
                    san.insert(1,files)
                    san = "".join(san)
            brd_cpy = board.copy()     
            mvs.append(san) 
            
    
    return mvs