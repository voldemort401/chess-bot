__all__ = ["chess", "PseudolegalMoves", "isLegalMove", "Board", "vars"]

from . import vars
from .Board import board
class Chess():
    def Board(self, fen:str=None):
        return board(fen)() 