from Chess.vars import *
from pieces.bishop import bishop
from pieces.king import king
from pieces.queen import queen
from pieces.pawn import pawn
from pieces.rook import rook
from pieces.knight import knight
def generatePseudoLegalMoves(board):
    all_pseudo_moves    = [] 
    turn                = board[-1]
    for i,j in enumerate(board):
        print(i)
        if (j != EMPTY):
            if (turn == BLACK):
                if (j == BKNIGHT):
                    all_pseudo_moves.append(f'black-knight on {board_sqs[i]} : {knight(board_sqs[i], board)}')
                if (j == BKING):               
                    all_pseudo_moves.append(f'black-king on {board_sqs[i]} : {king(board_sqs[i], board)}')
                if (j == BROOK):
                    all_pseudo_moves.append(f'black-rook on {board_sqs[i]} : {rook(board_sqs[i], board)}')
                if (j == BBISHOP): 
                    all_pseudo_moves.append(f'black-bishop on {board_sqs[i]} : {bishop(board_sqs[i], board)}')
                if (j == BPAWN): 
                    all_pseudo_moves.append(f'black-pawn on {board_sqs[i]} : {pawn(board_sqs[i], board)}')
                if (j == BQUEEN):        
                    all_pseudo_moves.append(f'black-queen on {board_sqs[i]} : {queen(board_sqs[i], board)}')
            else:
                if (j == WKNIGHT):                     
                    all_pseudo_moves.append(f'white-knight on {board_sqs[i]}: {knight(board_sqs[i], board)}')
                if (j == WKING):              
                    all_pseudo_moves.append(f'white-king on {board_sqs[i]} : {king(board_sqs[i], board)} ')
                if (j == WROOK):
                    all_pseudo_moves.append(f'white-rook on {board_sqs[i]} : {rook(board_sqs[i], board)} ')
                if (j == WBISHOP): 
                    all_pseudo_moves.append(f'white-bishop on {board_sqs[i]} {bishop(board_sqs[i], board)} ')
                if (j == WPAWN): 
                    all_pseudo_moves.append(f'white-pawn on {board_sqs[i]} : {pawn(board_sqs[i], board)} ')
                if (j == WQUEEN):       
                    all_pseudo_moves.append(f'white-queen on {board_sqs[i]} : {queen(board_sqs[i], board)} ')
                    
    return all_pseudo_moves
