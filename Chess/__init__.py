__all__ = ["chess", "PseudolegalMoves", "isLegalMove", "Board", "vars"]

from . import vars
from .Board import board
from .chess import generatePseudoLegalMoves
class Chess():
    def Board(self, fen:str=None):
        return board(fen)
    def PseudolegalMovegen(self,board):
        return generatePseudoLegalMoves(board)