from Chess.vars import * ## importing the variables
from Chess.chess import generatePseudoLegalMoves, filterPseudolegalmoves, isCheckMate
from pieces.king import castle
class board():
    def __init__(self,fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" ):
        self.board=[]
        if (fen.find('w') != -1):
            pointer = fen.find('w')
        else:
            pointer = fen.find('b')
        
        self.fen = dict()
        self.fen.update({fen[:pointer]: fen[pointer:]})
    
    def __create_board__(self):
        fen_board = list(self.fen.keys())[0].lstrip().rstrip()
        met       = list(self.fen.values())[0]
        if (len(met) < 9):
            return 'Invalid Fen'
        met = met.split(' ')
        ## checking if fen is valid 
        if (len(fen_board.split('/')) != 8):
            return 'Invalid Fen'
        if (not 'w' in met and not 'b' in met):
            return 'Invalid Fen'

        if ('w' in met): 
            turn = WHITE
        else:
            turn = BLACK

        move_counter       = int(met[-1])
        half_move_clock    = int(met[3])
        castle_rights      = met[1]   
        en_passant_squares = met[2]

        # create the board
        board=[]
        for i in range(len(fen_board)):
            piece = fen_board[i]
            if (piece != '/'):
                if (piece == 'n'):
                    board.append(BKNIGHT)
                elif (piece == 'k'):                     
                    board.append(BKING)
                elif (piece == 'r'):
                    board.append(BROOK)
                elif (piece == 'b'): 
                    board.append(BBISHOP)
                elif (piece == 'p'): 
                    board.append(BPAWN)
                elif (piece == 'q'):                    
                    board.append(BQUEEN)
                elif (piece == 'N'):                     
                    board.append(WKNIGHT)
                elif (piece == 'K'):                    
                    board.append(WKING)
                elif (piece == 'R'):
                    board.append(WROOK)
                elif (piece == 'B'): 
                    board.append(WBISHOP)
                elif (piece == 'P'): 
                    board.append(WPAWN)
                elif (piece == 'Q'):                   
                    board.append(WQUEEN)
                
                else:
                    empty_squares = int(piece)
                    for k in range(empty_squares):
                        board.append(EMPTY)
        
        board.append(turn)
        board.append(move_counter)
        board.append(half_move_clock)
        board.append(castle_rights)
        board.append(en_passant_squares)

        self.board = board
        return board

    def __get_current_board__(self):
        if (self.board == []):
            return self.__create_board__()
        else:
            return self.board

    def by_insufficent_material(self):
        board  = self.__get_current_board__()
        result = isCheckMate(board=board,turn=board[64])
        if (result == [0,0,1]):
            return True
        
        return False
    
    def checkmate(self):
        board = self.__get_current_board__()
        result = isCheckMate(board=board, turn=board[64]) 
        if (result == [1,0,0]):
            return True
        
        return False
    
    def stalemate(self):
        board = self.__get_current_board__()
        result = isCheckMate(board=board, turn=board[64])
        if (result == [0,1,0]):
            return True
        
        return False
    
    def draw(self):
        board = self.__get_current_board__()
        result = isCheckMate(board=board, turn=board[64])

        if (result == [1,0,0] or result == [0,0,0]):
            return False
        
        return True


    def move(self, move: str):
        board = self.__get_current_board__()
        if (not self.draw() and not self.checkmate()):

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
                move = move.replace('x','')
            if (move.rfind('+')  != -1):
                move = move.replace('+','')


            if (move[0] in ('a','b','c','d','e','f','g','h')):
                Piece_is_pawn=True 

            if (len(move) > 3):
                return 'ERR: Incorrect notation'

            piece = move[0] if Piece_is_pawn == False else ''
            target_square = move[1:] if Piece_is_pawn == False else move
            Plegal_moves  = generatePseudoLegalMoves(board,piece,turn)
            Plegal_moves  = filterPseudolegalmoves(Plegal_moves, self.board) 

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
             
            for indx,keys in enumerate(Plegal_moves):
                squares                = Plegal_moves.get(keys)
                old_piece_pos          = board_sqs.index(keys)
                new_piece_pos          = board_sqs.index(target_square)

                if (new_piece_pos in squares):    
                    if (self.board[new_piece_pos][:3] != turn and self.board[new_piece_pos] != EMPTY):
                        captured_pieces.append(self.board[new_piece_pos])

                    ## updating the turn and move counter
                    if (turn == WHITE):
                        print(self.board[65])
                        move_counter = self.board[65]
                        self.board[64] = BLACK
                        self.board[65] = int(move_counter)+1 

   
                    elif (turn == BLACK):
                        self.board[64] = WHITE
                    self.board = [EMPTY if x == old_piece_pos else o for x,o in enumerate(self.board)]
                    self.board = [piece if x == new_piece_pos else o for x,o in enumerate(self.board)]


                    if (piece == ''):
                        board[66] = 0
                    if(board[new_piece_pos]!= EMPTY and board[new_piece_pos][:3] != turn):
                        board[66] =0 

                    board[66]==board[66]+1
 


            if (not self.draw() and not self.checkmate()):
                return self.board
            else:
                return f'GameOver: {isCheckMate(board=self.board, turn=self.board[64])}' 


        else:
           return f'GameOver: {isCheckMate(board=board, turn=board[64])}' 
    
    def __call__(self):
        return self.__get_current_board__()

    