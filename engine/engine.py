class Engine():
    def __init__(self,board,LegalMoves):
        self.LegalMoves = LegalMoves
        self.board      = board 

    def eval(self) -> float:
        return 0.0
   
