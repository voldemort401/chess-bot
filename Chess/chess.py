from Chess.vars import *
from pieces.bishop import bishop
from pieces.king import king
from pieces.queen import queen
from pieces.pawn import pawn
from pieces.rook import rook
from pieces.knight import knight
def generatePseudoLegalMoves(board, piece:str=None, color=None):
    all_pseudo_moves    = [] 
    turn                = board[64]
    if (piece != None):
        for i,j in enumerate(board):
         if (j != EMPTY):
             if (turn == BLACK or color == BLACK):
                 if (j == BKNIGHT and piece == 'N'):
                     all_pseudo_moves.append(f'{board_sqs[i]}: {knight(board_sqs[i], board)}')
                 elif (j == BKING and piece == 'K'):               
                     all_pseudo_moves.append(f'{board_sqs[i]}: {king(board_sqs[i], board)}')
                 elif (j == BROOK and piece == 'R'):  
                    all_pseudo_moves.append(f'{board_sqs[i]}: {rook(board_sqs[i], board)}')
                 elif (j == BBISHOP and piece == 'B'): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {bishop(board_sqs[i], board)}')
                 elif (j == BPAWN and piece == ''): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {pawn(board_sqs[i], board)}')
                 elif (j == BQUEEN and piece == 'Q'):        
                     all_pseudo_moves.append(f'{board_sqs[i]}: {queen(board_sqs[i], board)}')
             elif (turn == WHITE and color == WHITE):
                 if (j == WKNIGHT and piece == 'N'):                     
                     all_pseudo_moves.append(f'{board_sqs[i]}: {knight(board_sqs[i], board)}')
                 elif (j == WKING and piece == 'K'):              
                     all_pseudo_moves.append(f'{board_sqs[i]}: {king(board_sqs[i], board)} ')
                 elif (j == WROOK and piece == 'R'):
                     all_pseudo_moves.append(f'{board_sqs[i]}: {rook(board_sqs[i], board)} ')
                 elif (j == WBISHOP and piece == 'B'): 
                     all_pseudo_moves.append(f'{board_sqs[i]} {bishop(board_sqs[i], board)} ')
                 elif (j == WPAWN and piece == ''): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {pawn(board_sqs[i], board)} ')
                 elif (j == WQUEEN and piece == 'Q'):       
                     all_pseudo_moves.append(f'{board_sqs[i]}: {queen(board_sqs[i], board)} ')
     
    else:
        for i,j in enumerate(board):
         if (j != EMPTY):
             if (turn == BLACK or color == BLACK):
                 if (j == BKNIGHT):
                     all_pseudo_moves.append(f'{board_sqs[i]}: {knight(board_sqs[i], board)}')
                 if (j == BKING):               
                     all_pseudo_moves.append(f'{board_sqs[i]}: {king(board_sqs[i], board)}')
                 if (j == BROOK):
                     all_pseudo_moves.append(f'{board_sqs[i]}: {rook(board_sqs[i], board)}')
                 if (j == BBISHOP): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {bishop(board_sqs[i], board)}')
                 if (j == BPAWN): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {pawn(board_sqs[i], board)}')
                 if (j == BQUEEN):        
                     all_pseudo_moves.append(f'{board_sqs[i]}: {queen(board_sqs[i], board)}')
             elif (turn == WHITE or color == WHITE):
                 if (j == WKNIGHT):                     
                     all_pseudo_moves.append(f'{board_sqs[i]}: {knight(board_sqs[i], board)}')
                 if (j == WKING):              
                     all_pseudo_moves.append(f'{board_sqs[i]}: {king(board_sqs[i], board)} ')
                 if (j == WROOK):
                     all_pseudo_moves.append(f'{board_sqs[i]}: {rook(board_sqs[i], board)} ')
                 if (j == WBISHOP): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {bishop(board_sqs[i], board)} ')
                 if (j == WPAWN): 
                     all_pseudo_moves.append(f'{board_sqs[i]}: {pawn(board_sqs[i], board)} ')
                 if (j == WQUEEN):       
                     all_pseudo_moves.append(f'{board_sqs[i]}: {queen(board_sqs[i], board)} ')
                     
    return all_pseudo_moves
 

def isinCheck(board, king_pos) -> bool | str:
    color = board[king_pos][:3]
    if (color == WHITE):
        enmy_color = BLACK
    elif (color == BLACK):
        enmy_color == WHITE
    else:
        return 'ERR: Failed to get color'

    if (king(board_sqs[king_pos], board) == []):
        return False

    black_moves = generatePseudoLegalMoves(board=board, piece=None, color=enmy_color)

    for i,j in enumerate(black_moves):
        # just getting the moves to check if anyone is seeing the other king 
        j = j.split(':')
        j = j[1].replace('[]','') # removing the empty moves
        j = j.strip('[ ]') ## removing [ and ] 
        j = j.split(',') 
        for k in j:
            if (k == king_pos):
                return True

def filterPseudolegalmoves(moves:list, board):
    current_turn = board[64]
    current_board = board
    if (current_turn == WHITE):
        king_pos = board.index(WKING)
    elif (current_turn == BLACK):
        king_pos = board.index(BKING)

    for i,j in enumerate(moves):
        k = j.split(':') # splitting into 2 part eg: ['a2', '[moves]'] makes it easier to only get the moves portion
        old_piece_pos = board_sqs.index(k[0].lstrip())
        target_square = k[1].replace('[]','').strip('[ ]').split(',')

        if (target_square == ['']):
            moves.remove(j)
        else:
            piece         = board[old_piece_pos]
            for z in target_square:
              new_piece_pos = int(z)
              current_board = [EMPTY if x == old_piece_pos else o for x,o in enumerate(current_board)]
              current_board = [piece if x == new_piece_pos else o for x,o in enumerate(current_board)]
              if (isinCheck(board, king_pos)):
                moves.remove(z)
              current_board = board
    return moves