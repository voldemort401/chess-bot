__all__ = ["chess",  "Board", "vars"]

from . import vars
class Chess():
    def Board(self, fen:str=None):
        from .Board import board
        return board(fen)

    def PseudolegalMovegen(self,board,color=None):
        from pieces.king import castle
        from .chess import generatePseudoLegalMoves

        moves = []
        if (board[64] == vars.BLACK):
            king_pos = vars.board_sqs[board.index(vars.BKING)]
        elif (board[64] == vars.WHITE):
            king_pos = vars.board_sqs[board.index(vars.WKING)]

        if (type(castle(king_pos, board, 'O-O')) != str):
            moves.append('O-O')
        if (type(castle(king_pos, board, 'O-O-O')) != str):
            moves.append('O-O-O')

        return generatePseudoLegalMoves(board, color=color) + moves
    def LegalMoves(self,board):
        from .chess import legal_move_gen
        return legal_move_gen(board) 