from Chess.vars import *
from pieces.bishop import bishop
from pieces.king import king, castle
from pieces.queen import queen
from pieces.pawn import pawn
from pieces.rook import rook
from pieces.knight import knight
def generatePseudoLegalMoves(board, piece=None, color=None):
    all_pseudo_moves    = [] 
    turn                = board[64]
    if (piece != None):
        for i,j in enumerate(board):
         if (j != EMPTY and i < 64):
             if (turn == BLACK or color == BLACK):
                 if (j == BKNIGHT and piece == 'N'):
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(knight(board_sqs[i], board)))}')
                 elif (j == BKING and piece == 'K'):               
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(king(board_sqs[i], board)))}')
                 elif (j == BROOK and piece == 'R'):  
                    all_pseudo_moves.append(f'{board_sqs[i]}:  {list(set(rook(board_sqs[i], board)))}')
                 elif (j == BBISHOP and piece == 'B'): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(bishop(board_sqs[i], board)))}')
                 elif (j == BPAWN and piece == ''): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(pawn(board_sqs[i], board)))}')
                 elif (j == BQUEEN and piece == 'Q'):        
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(queen(board_sqs[i], board)))}')

             elif (turn == WHITE and color == WHITE):
                 if (j == WKNIGHT and piece == 'N'):                     
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(knight(board_sqs[i], board)))}')
                 elif (j == WKING and piece == 'K'):              
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(king(board_sqs[i], board)))}')
                 elif (j == WROOK and piece == 'R'):
                     all_pseudo_moves.append(f'{board_sqs[i]}:  {list(set(rook(board_sqs[i], board)))}')
                 elif (j == WBISHOP and piece == 'B'): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(bishop(board_sqs[i], board)))}')
                 elif (j == WPAWN and piece == ''): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(pawn(board_sqs[i], board)))}')
                 elif (j == WQUEEN and piece == 'Q'):       
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(queen(board_sqs[i], board)))}')
     
    else:
        for i,j in enumerate(board):
         if (j != EMPTY and i < 64):
             if (turn == BLACK or color == BLACK):
                 if (j == BKNIGHT):
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(knight(board_sqs[i], board)))}')
                 if (j == BKING):               
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(king(board_sqs[i], board)))}')
                 if (j == BROOK):
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(rook(board_sqs[i], board)))}')
                 if (j == BBISHOP): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(bishop(board_sqs[i], board)))}')
                 if (j == BPAWN): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(pawn(board_sqs[i], board)))}')
                 if (j == BQUEEN):        
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(queen(board_sqs[i], board)))}')

             elif (turn == WHITE or color == WHITE):
                 if (j == WKNIGHT):                     
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(knight(board_sqs[i], board)))}')
                 if (j == WKING):              
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(king(board_sqs[i], board)))} ')
                 if (j == WROOK):
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(rook(board_sqs[i], board)))} ')
                 if (j == WBISHOP): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(bishop(board_sqs[i], board)))} ')
                 if (j == WPAWN): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(pawn(board_sqs[i], board)))} ')
                 if (j == WQUEEN):       
                     all_pseudo_moves.append(f'{board_sqs[i]}: {list(set(queen(board_sqs[i], board)))} ')
    return all_pseudo_moves
 

def isinCheck(board, king_pos) -> bool | str:
    color = board[king_pos][:3]
    if (color == WHITE):
        enmy_color = BLACK
    elif (color == BLACK):
        enmy_color = WHITE
    else:
        return f'ERR: Failed to get color color={color}'

    if (king(board_sqs[king_pos], board) == []):
        return False

    black_moves = generatePseudoLegalMoves(board=board, piece=None, color=enmy_color)
    for i,j in enumerate(black_moves):
        k = j.split(':')
        for z,o in enumerate(k):
            if (z == 1):
                o = o.replace('[','')
                o = o.replace(']','')
                o = o.replace(',', '')
                if str(king_pos) in o:
                    return True

    return False 

def filterPseudolegalmoves(moves:list, board):
    current_turn = board[64]
    current_board = board
    
    for i,j in enumerate(moves):
        k = j.split(':') # splitting into 2 part eg: ['a2', '[moves]'] makes it easier to only get the moves portion
        old_piece_pos = board_sqs.index(k[0])
        target_square = k[1].replace('[]','')

        target_square = target_square.replace('[','')
        target_square = target_square.replace(']', '')
        target_square = target_square.lstrip()
        target_square = target_square.rstrip()
        target_square = target_square.split(',')
        if (target_square == ''):
            moves.remove(j)
        else:
            piece         = board[old_piece_pos]
            for z in target_square:
                if (z != ''): 
                    new_piece_pos = int(z)
                    current_board = [EMPTY if x == old_piece_pos else o for x,o in enumerate(current_board)]
                    current_board = [piece if x == new_piece_pos else o for x,o in enumerate(current_board)]
                    if (current_turn == WHITE):
                        king_pos = current_board.index(WKING)
                    elif (current_turn == BLACK):
                        king_pos = current_board.index(BKING)

                    if (isinCheck(current_board, king_pos)):
                        moves[i] = moves[i].replace(str(z), ' ')
                    current_board = board
    return moves

def legal_move_gen(board):
    moves = []
    if (board[64] == BLACK):
        king_pos = board_sqs[board.index(BKING)]
    elif (board[64] == WHITE):
        king_pos = board_sqs[board.index(WKING)]

    if (type(castle(king_pos, board, 'O-O')) != str):
        moves.append('O-O')
    if (type(castle(king_pos, board, 'O-O-O')) != str):
        moves.append('O-O-O')
    pseudo_legal_moves = generatePseudoLegalMoves(board)
    return filterPseudolegalmoves(pseudo_legal_moves, board)+moves


def isCheckMate(board, turn):
    if (turn == WHITE):
        king_pos = board.index(WKING)
    elif (turn == BLACK):
        king_pos = board.index(BKING)
    else:
        return 'invalid turn'
    
    king_moves = king(king_pos,board)
    legal_moves = legal_move_gen(board)
    for i,j in enumerate(legal_moves):
        k = j.split(':') # splitting into 2 part eg: ['a2', '[moves]'] makes it easier to only get the moves portion
        if (len(k) > 1):
            possible_square = k[1].replace('[]','')
            possible_square = possible_square.replace('[','')
            possible_square = possible_square.replace(']', '')
            possible_square = possible_square.lstrip()
            possible_square = possible_square.rstrip()
            possible_square = possible_square.split(',')

        else: ## basically this only applies for the castleing moves 
            possible_square = k
        ##WIP 