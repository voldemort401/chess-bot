from Chess.vars import * ## importing the variables
class board():
    def __init__(self,fen:str = None):
        self.fen = fen
        if (fen != None):
            self.fen = fen
        else:
            self.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" 

    def __create_board__(self):
        if (self.fen.find('w') == -1 and self.fen.find(' b ') == -1):
            return -1 
        turn = WHITE if (self.fen.find('w') != -1) else BLACK
        board=[]
        for i,j in enumerate(self.fen):
            if (i <= self.fen.find('w') or i<= self.fen.find(' b ')):
                try:
                    for k in range(int(self.fen[i])):
                        board.append(EMPTY)                

                except ValueError:
                    ## LOWERCASE BLACK    UPPERCASE WHITE 
                    if (j == 'n'):
                        board.append(BKNIGHT)
                    if (j == 'k'):                     
                        board.append(BKING)
                    if (j == 'r'):
                        board.append(BROOK)
                    if (j == 'b'): 
                        board.append(BBISHOP)
                    if (j == 'p'): 
                        board.append(BPAWN)
                    if (j == 'q'):                    
                        board.append(BQUEEN)
                    if (j == 'N'):                     
                        board.append(WKNIGHT)
                    if (j == 'K'):                    
                        board.append(WKING)
                    if (j == 'R'):
                        board.append(WROOK)
                    if (j == 'B'): 
                        board.append(WBISHOP)
                    if (j == 'P'): 
                        board.append(WPAWN)
                    if (j == 'Q'):                   
                        board.append(WQUEEN)
        board.append(turn)
        return board
    def __call__(self):
        return self.__create_board__()