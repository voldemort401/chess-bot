from src.chess import chess
class isLegalmove:
    def __init__(self,move, board):
        self.move  = move[2:].rstrip('+')
        self.piece = self.move[:2]

        if not (self.move in chess().generatePseudoLegalMoves(board)):
           return 'Invalid move!'
         

    def islegalmove(self):
        print(self.move,self.piece)
