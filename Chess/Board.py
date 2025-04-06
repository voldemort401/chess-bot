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
        turn = self.board[64]
            
        Piece_is_pawn = False
        if (move.rfind('x')  != -1):
            isCapturing = True
            move = move.replace('x','')

        if (move.rfind('+')  != -1):
            isChecking = True    
            move = move.replace('+','')

        if (move[0] in ('a','b','c','d','e','f','g','h')):
            Piece_is_pawn=True 

        if (len(move) > 3):
            return 'ERR: Incorrect notation'

        piece = move[0] if Piece_is_pawn == False else ''
        target_square = move[1:]

        Plegal_moves  = generatePseudoLegalMoves(board, piece) 

        if (turn == WHITE):
            if (piece == 'N' or piece == 'n'):                    
                piece = WKNIGHT                                                                                          
            elif (piece == 'K' or piece == 'k'):              
                piece = WKING
            elif (piece == 'R' or piece == 'r'):
                piece = WROOK
            elif (piece == 'B' or piece == 'b'): 
                piece = WBISHOP
            elif (piece == ''): 
                piece = WPAWN
            elif (piece == 'Q' or piece == 'q'):       
                piece = WQUEEN
        else:
            if (j  == 'N' or piece == 'n'):
                piece = BKNIGHT
            elif ( piece == 'K' or piece == 'k'):               
                piece = BKING
            elif ( piece == 'R' or piece == 'r'):
                piece = BROOK
            elif ( piece == 'B' or piece == 'b'): 
                piece = BBISHOP
            elif ( piece == ''): 
                piece = BPAWN
            elif ( piece == 'Q' or piece == 'q'):        
                piece = BQUEEN
                                                                                          

        for i,j in enumerate(Plegal_moves):
            if (j.__contains__(str(board_sqs.index(target_square)))):    
              j = j.split(':') # splitting into 2 part eg: ['a2', '[moves]'] makes it easier to only get the moves portion
              old_piece_pos = board_sqs.index(j[0].lstrip())
              new_piece_pos = board_sqs.index(target_square)
              self.board.pop(old_piece_pos)
              self.board.insert(old_piece_pos, EMPTY)
              self.board.insert(new_piece_pos, piece)
              
              ## updating the turn and move counter
              if (turn == WHITE):
                move_counter=self.board[-1]
                move_counter+=1
                self.board.pop(64)
                self.board.insert(64, BLACK)
                
                self.board.pop(65)
                self.board.insert(65, move_counter)

              elif (turn == BLACK):
                self.board.pop(64)
                self.board.insert(64, BLACK)

              break

        if (board == self.board):
            return 'Illegal move'

        return self.board

    

    def __call__(self):
        return self.__create_board__()
