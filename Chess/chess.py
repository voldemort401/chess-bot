from Chess.vars import *
from pieces.bishop import bishop
from pieces.king import king
from pieces.queen import queen
from pieces.pawn import pawn
from pieces.rook import rook
from pieces.knight import knight
def generatePseudoLegalMoves(board, piece:str=None):
    all_pseudo_moves    = [] 
    turn                = board[64]
    if (piece != None):
        for i,j in enumerate(board):
         print(i)
         if (j != EMPTY):
             if (turn == BLACK):
                 if (j == BKNIGHT and piece == 'N' or piece == 'n'):
                     all_pseudo_moves.append(f'{board_sqs[i]} : {knight(board_sqs[i], board)}')
                 elif (j == BKING and piece == 'K' or piece == 'k'):               
                     all_pseudo_moves.append(f'{board_sqs[i]} : {king(board_sqs[i], board)}')
                 elif (j == BROOK and piece == 'R' or piece == 'r'):
                    all_pseudo_moves.append(f'{board_sqs[i]} : {rook(board_sqs[i], board)}')
                 elif (j == BBISHOP and piece == 'B' or piece == 'b'): 
                     all_pseudo_moves.append(f'{board_sqs[i]} : {bishop(board_sqs[i], board)}')
                 elif (j == BPAWN and piece == ''): 
                     all_pseudo_moves.append(f'{board_sqs[i]} : {pawn(board_sqs[i], board)}')
                 elif (j == BQUEEN and piece == 'Q' or piece == 'q'):        
                     all_pseudo_moves.append(f'{board_sqs[i]} : {queen(board_sqs[i], board)}')
             else:
                 if (j == WKNIGHT and piece == 'N' or piece == 'n'):                     
                     all_pseudo_moves.append(f'{board_sqs[i]}: {knight(board_sqs[i], board)}')
                 elif (j == WKING and piece == 'K' or piece == 'k'):              
                     all_pseudo_moves.append(f'{board_sqs[i]} : {king(board_sqs[i], board)} ')
                 elif (j == WROOK and piece == 'R' or piece == 'r'):
                     all_pseudo_moves.append(f'{board_sqs[i]} : {rook(board_sqs[i], board)} ')
                 elif (j == WBISHOP and piece == 'B' or piece == 'b'): 
                     all_pseudo_moves.append(f'{board_sqs[i]} {bishop(board_sqs[i], board)} ')
                 elif (j == WPAWN and piece == ''): 
                     all_pseudo_moves.append(f'{board_sqs[i]} : {pawn(board_sqs[i], board)} ')
                 elif (j == WQUEEN and piece == 'Q' or piece == 'q'):       
                     all_pseudo_moves.append(f'{board_sqs[i]} : {queen(board_sqs[i], board)} ')
    
     
    else:
        for i,j in enumerate(board):
         print(i)
         if (j != EMPTY):
             if (turn == BLACK):
                 if (j == BKNIGHT):
                     all_pseudo_moves.append(f'{board_sqs[i]} : {knight(board_sqs[i], board)}')
                 if (j == BKING):               
                     all_pseudo_moves.append(f'{board_sqs[i]} : {king(board_sqs[i], board)}')
                 if (j == BROOK):
                     all_pseudo_moves.append(f'{board_sqs[i]} : {rook(board_sqs[i], board)}')
                 if (j == BBISHOP): 
                     all_pseudo_moves.append(f'{board_sqs[i]} : {bishop(board_sqs[i], board)}')
                 if (j == BPAWN): 
                     all_pseudo_moves.append(f'{board_sqs[i]} : {pawn(board_sqs[i], board)}')
                 if (j == BQUEEN):        
                     all_pseudo_moves.append(f'{board_sqs[i]} : {queen(board_sqs[i], board)}')
             else:
                 if (j == WKNIGHT):                     
                     all_pseudo_moves.append(f'{board_sqs[i]}: {knight(board_sqs[i], board)}')
                 if (j == WKING):              
                     all_pseudo_moves.append(f'{board_sqs[i]} : {king(board_sqs[i], board)} ')
                 if (j == WROOK):
                     all_pseudo_moves.append(f'{board_sqs[i]} : {rook(board_sqs[i], board)} ')
                 if (j == WBISHOP): 
                     all_pseudo_moves.append(f'{board_sqs[i]} {bishop(board_sqs[i], board)} ')
                 if (j == WPAWN): 
                     all_pseudo_moves.append(f'{board_sqs[i]} : {pawn(board_sqs[i], board)} ')
                 if (j == WQUEEN):       
                     all_pseudo_moves.append(f'{board_sqs[i]} : {queen(board_sqs[i], board)} ')
                     
    return all_pseudo_moves
    