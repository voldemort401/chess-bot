from pieces.bishop import bishop
from pieces.rook import rook
def queen(piece_pos,board):
    return bishop(piece_pos,board, 1) + rook(piece_pos, board,1)