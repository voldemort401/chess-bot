__all__ = ["chess",  "Board", "vars"]

from . import vars
class Chess():
    def __init__(self,fen):
        from .Board import board
        brd = board(fen)
        self.board = brd.__get_current_board__() 

    def __Board__(self, fen:str=None):
        from .Board import board
        return board(fen)

    def get_pseudo_legal_move(self,board,color=None):
        from pieces.king import castle
        from .chess import generatePseudoLegalMoves

        cstle = []
        pseudo_moves = generatePseudoLegalMoves(board,color=color)
        if (board[64] == vars.BLACK):
            king_pos = vars.board_sqs[board.index(vars.BKING)]
        elif (board[64] == vars.WHITE):
            king_pos = vars.board_sqs[board.index(vars.WKING)]

        if (type(castle(king_pos, board, 'O-O')) != str):
            cstle.append('O-O')
        if (type(castle(king_pos, board, 'O-O-O')) != str):
            cstle.append('O-O-O')
        if (cstle != []):
            pseudo_moves.update({'castle' : cstle})
        return pseudo_moves 


    def get_moves(self):
        from .chess import legal_move_gen, convert_to_san
        legal_moves = legal_move_gen(self.board)
        legal_moves = convert_to_san(legal_moves, self.board)
        return legal_moves 