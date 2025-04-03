from Chess.vars import *
from pieces.bishop import bishop
from pieces.king import king
from pieces.queen import queen
from pieces.pawn import pawn
from pieces.rook import rook
from pieces.knight import knight
def generatePseudoLegalMoves(board):
    all_pseudo_moves    = {} 
    turn                = board[-1]
    for i,j in enumerate(board):
        print(i)
        if (j != EMPTY):
            if (turn == BLACK):
                if (j == BKNIGHT):
                    all_pseudo_moves.update({'black-knight': f'{knight(board_sqs[i], board)}'})
                if (j == BKING):                     
                    all_pseudo_moves.update({'black-king': f'{king(board_sqs[i], board)}'})
                if (j == BROOK):
                    all_pseudo_moves.update({'black-rook': f'{rook(board_sqs[i], board)}'})
                if (j == BBISHOP): 
                       all_pseudo_moves.update({'black-bishop': f'{bishop(board_sqs[i], board)}'})
                if (j == BPAWN): 
                    all_pseudo_moves.update({'black-pawn': f'{pawn(board_sqs[i], board)}'})
                if (j == BQUEEN):              
                    all_pseudo_moves.update({'black-queen': f'{queen(board_sqs[i], board)}'})
            else:
                if (j == WKNIGHT):                     
                    all_pseudo_moves.update({'white-knight': f'{knight(board_sqs[i], board)}'})
                if (j == WKING):              
                    all_pseudo_moves.update({'white-king': f'{king(board_sqs[i], board)}'})
                if (j == WROOK):
                    all_pseudo_moves.update({'white-rook': f'{rook(board_sqs[i], board)}'})
                if (j == WBISHOP): 
                    all_pseudo_moves.update({'white-bishop': f'{bishop(board_sqs[i], board)}'})
                if (j == WPAWN): 
                    all_pseudo_moves.update({'white-pawn': f'{pawn(board_sqs[i], board)}'})
                if (j == WQUEEN):             
                    all_pseudo_moves.update({'white-queen': f'{queen(board_sqs[i], board)}'})
                    
    return str(all_pseudo_moves)
