from Chess.vars import * ## importing the variables
from Chess.chess import generatePseudoLegalMoves
class board():
    def __init__(self,fen:str = None):
        self.fen = fen
        self.board=[]
        if (fen != None):
            self.fen = fen
        else:
            self.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" 

    def __create_board__(self):
        if (self.fen.find('w') == -1 and self.fen.find(' b ') == -1):
            return -1 
        turn = WHITE if (self.fen.find('w') != -1) else BLACK
        board=[]
        move_counter = 0
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
        board.append(move_counter)
        self.board = board
        return board

    def __get_current_board__(self):
        if (self.board == []):
            return self.__create_board__()
        else:
            return self.board
    
    def Move(self, move: str):
        board = self.__get_current_board__()
        print(self.fen)
        ## N x d 4 + 
        if (len(move) > 5):
            return 'ERR: Incorrect notation'

        Plegal_moves  = generatePseudoLegalMoves(board, piece) 

        for i,j in enumerate(Plegal_moves):
            if (target_square in j):
                print('hallop')



    def __call__(self):
        return self.__create_board__()