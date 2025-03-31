from src.chess import chess
class board(chess):
    def __init__(self,fen:str):
        super(board,self).__init__()
        self.fen = fen
        if (fen == ""):
            self.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" 

    def move(self,board:list, move: str) -> list | str:
        from src.isLegalMove import isLegalmove
        if(isLegalmove(move,board)):
            pass

        else:
            return 'Invalid move!'
        return board

    def create_brd(self):
        if (self.fen.find('w') == -1 and self.fen.find(' b ') == -1):
            return -1 
        turn = self.WHITE if (self.fen.find('w') != -1) else self.BLACK
        self.board=[]
        for i,j in enumerate(self.fen):
            if (i <= self.fen.find('w') or i<= self.fen.find(' b ')):
                try:
                    for k in range(int(self.fen[i])):
                        self.board.append(self.EMPTY)                

                except ValueError:
                    ## LOWERCASE BLACK    UPPERCASE WHITE 
                    if (j == 'n'):
                        self.board.append(self.BKNIGHT)
                    if (j == 'k'):                     
                        self.board.append(self.BKING)
                    if (j == 'r'):
                        self.board.append(self.BROOK)
                    if (j == 'b'): 
                        self.board.append(self.BBISHOP)
                    if (j == 'p'): 
                        self.board.append(self.BPAWN)
                    if (j == 'q'):                    
                        self.board.append(self.BQUEEN)
                    if (j == 'N'):                     
                        self.board.append(self.WKNIGHT)
                    if (j == 'K'):                    
                        self.board.append(self.WKING)
                    if (j == 'R'):
                        self.board.append(self.WROOK)
                    if (j == 'B'): 
                        self.board.append(self.WBISHOP)
                    if (j == 'P'): 
                        self.board.append(self.WPAWN)
                    if (j == 'Q'):                   
                        self.board.append(self.WQUEEN)

        self.board.append(turn)
        return self.board

    
