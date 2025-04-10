from Chess.vars import * ## importing the variables
from Chess.chess import generatePseudoLegalMoves, filterPseudolegalmoves
from pieces.king import castle
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
        if (move == ''):
            return "Invalid move"
        bmove = move  
        Piece_is_pawn = False
        if (move.lstrip().rstrip() == 'O-O'):
            if (turn == WHITE):
                king_pos = board.index(WKING)
            elif (turn == BLACK):
                king_pos = board.index(BKING)
            else:
                return 'Unexpected error occured'
            if (type(castle(king_pos, self.board, move.lstrip().rstrip())) == str):
                return 'Illegal move'
            
            self.board = castle(king_pos, self.board, move.lstrip().rstrip)

        elif (move.lstrip().rstrip() == 'O-O-O'):
            if (turn == WHITE):
                king_pos = board.index(WKING)
            elif (turn == BLACK):
                king_pos = board.index(BKING)
            else:
                return 'Unexpected error occured'
            if (type(castle(king_pos, self.board, move.lstrip().rstrip())) == str):
                return 'Illegal move'
            
            self.board = castle(king_pos, self.board, move.lstrip().rstrip())


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
        target_square = move[1:] if Piece_is_pawn == False else move
        Plegal_moves  = set(generatePseudoLegalMoves(board,piece,turn))
        Plegal_moves  = filterPseudolegalmoves(list(Plegal_moves), self.board) 
        if (turn == WHITE):
            if (piece == 'N' or piece == 'n'):                    
                piece = WKNIGHT                                                                                          
            elif (piece == 'K' or piece == 'k'):              
                piece = WKING
                king_moved[0] = 1 
            elif (piece == 'R' or piece == 'r'):
                piece = WROOK
                rook_moved[0] = 1
            elif (piece == 'B' or piece == 'b'): 
                piece = WBISHOP
            elif (piece == ''): 
                piece = WPAWN
            elif (piece == 'Q' or piece == 'q'):       
                piece = WQUEEN
        else:
            if (piece  == 'N' or piece == 'n'):
                piece = BKNIGHT
            elif ( piece == 'K' or piece == 'k'):               
                piece = BKING
                king_moved[1] = 1 
            elif ( piece == 'R' or piece == 'r'):
                piece = BROOK
                rook_moved[1] = 1
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

              if (self.board[new_piece_pos][:3] != turn and self.board[new_piece_pos] != EMPTY):
                captured_pieces.append(self.board[new_piece_pos])
              self.board = [EMPTY if x == old_piece_pos else o for x,o in enumerate(self.board)]
              self.board = [piece if x == new_piece_pos else o for x,o in enumerate(self.board)]
              ## updating the turn and move counter
              if (turn == WHITE):
                print(self.board[65])
                move_counter = self.board[65]
                self.board[64] = BLACK
                self.board[65] = int(move_counter)+1 

              elif (turn == BLACK):
                self.board[64] = WHITE
              break

        move_counter = int(self.board[65])
        if (turn == WHITE):
            moves_played.append(['', ''])
            moves_played[move_counter-1][0] = bmove
        elif (turn == BLACK):
            moves_played[move_counter-1][1] = bmove
        else:
            return f'turn value "{turn}" is not valid'
        return self.board

    
    def __call__(self):
        return self.__get_current_board__()
