__all__ = ["chess",  "Board", "vars"]

from . import vars
class Chess():
    def Board(self, fen:str=None):
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

        pseudo_moves.update({'castle' : cstle})
        return pseudo_moves 


    def get_moves(self,board):
        from .chess import legal_move_gen
        legal_moves = legal_move_gen(board)
        for i,j in enumerate(legal_moves):
            piece_pos      = vars.board_sqs[board.index(j[1])]
            target_squares = j[0]
            target_squares = target_sq_cpy = target_squares.replace(' ', '')
            target_squares  = target_squares.split(',')

            for k in target_squares:
                target_sq_cpy.replace(str(k), str(vars.board_sqs[k]))



        return legal_move_gen(board)