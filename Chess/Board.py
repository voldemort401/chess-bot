from Chess.vars import * ## importing the variables
from Chess.chess import generatePseudoLegalMoves, filterPseudolegalmoves, isCheckMate
from pieces.king import castle
class board():
    def __init__(self,fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" ):
        self.board=[]
        if (fen.find('w') != -1):
            pointer = fen.find('w')
        else:
            pointer = fen.find(' b ')
        
        self.fen = dict()
        self.fen.update({fen[:pointer]: fen[pointer:]})
    
    def __create_board__(self):
        fen_board = list(self.fen.keys())[0].lstrip().rstrip()
        met       = list(self.fen.values())[0].lstrip().rstrip().split(' ')
        ## checking if fen is valid 
        if (len(fen_board.split('/')) != 8):
            return 'Invalid Fen1'
        if (not 'w' in met and not 'b' in met):
            return 'Invalid Fen2'

        if ('w' in met): 
            turn = WHITE
        else:
            turn = BLACK

        if (met[-1] == '-'):
            met.append('0')
            met.append('1')
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

        ## setting castle rights
        if (castle_rights == '-'):
            king_moved[0] = 1
            king_moved[1] = 1

        if (castle_rights.find('k') == -1):
            rook_moved[2] = 1
        if (castle_rights.find('K') == -1):
            rook_moved[0] = 1
        if (castle_rights.find('q') == -1):
            rook_moved[3] = 1
        if (castle_rights.find('Q') == -1):
            rook_moved[1] = 1

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
        
        if board[66] == 100:
            return True 
        return True


    def move(self, move: str, san=1):
        board = self.__get_current_board__()
        
        turn = self.board[64]
        if (move == ''):
            return "Invalid move"
        bmove = move  
        Piece_is_pawn = False
        if (move.lstrip().rstrip() == 'O-O' or move.lstrip().rstrip() == 'O-O-O'):
            if (turn == WHITE):
                king_pos = board.index(WKING)
            elif (turn == BLACK):
                king_pos = board.index(BKING)
            else:
                return 'Unexpected error occured'

            if (castle(king_pos, self.board, move.lstrip().rstrip(), out=0) == False):
                return 'Illegal move'

            self.board = castle(king_pos, self.board, move.lstrip().rstrip())


        if (move.rfind('x')  != -1):
            move = move.replace('x','')
        if (move.rfind('+')  != -1):
            move = move.replace('+','')

        if (san == 1):
            if (move[0] in ('a','b','c','d','e','f','g','h')):
                Piece_is_pawn=True 

            if (len(move) > 3):
                return 'ERR: Incorrect notation'

            piece = move[0] if Piece_is_pawn == False else ''
            target_square = move[1:] if Piece_is_pawn == False else move
            Plegal_moves  = generatePseudoLegalMoves(board,piece,turn)
            piece = piece.upper()

            if (turn == WHITE):
                if (piece == 'N' ):                    
                    piece = WKNIGHT                                                                                          
                elif (piece == 'K' ):              
                    piece = WKING
                    king_moved[0] = 1 
                elif (piece == 'R' ):
                    piece = WROOK
                elif (piece == 'B' ): 
                    piece = WBISHOP
                elif (piece == ''): 
                    piece = WPAWN
                elif (piece == 'Q' ):       
                    piece = WQUEEN
            else:
                if (piece  == 'N' ):
                    piece = BKNIGHT
                elif ( piece == 'K' ):               
                    piece = BKING
                    king_moved[1] = 1 
                elif ( piece == 'R' ):
                    piece = BROOK
                elif ( piece == 'B' ): 
                    piece = BBISHOP
                elif ( piece == ''): 
                    piece = BPAWN
                elif ( piece == 'Q' ):        
                    piece = BQUEEN
             
            for keys in Plegal_moves:
                squares                = Plegal_moves.get(keys)
                if (san == 1):
                    old_piece_pos          = board_sqs.index(keys)
                    new_piece_pos          = board_sqs.index(target_square)

                if (new_piece_pos in squares):    
                    if (self.board[new_piece_pos][:3] != turn and self.board[new_piece_pos] != EMPTY):
                        captured_pieces.append(self.board[new_piece_pos])

                    ## updating the turn and move counter
                    if (turn == WHITE):
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
 

                if (keys == 'a1' and piece == WROOK):
                    rook_moved[1] = 1
                elif (keys == 'h1' and piece == WROOK):
                    rook_moved[0] = 1

                if (keys == 'a8' and piece == WROOK):
                    rook_moved[3] = 1
                elif (keys == 'h8' and piece == WROOK):
                    rook_moved[2] = 1
        return board

    def undoMove(move:str): 
        # move is expected to be in format e2e4
        starting_square = board_sqs.index(move[:2])
        if (move.__contains__('x')):
            ending_square = board_sqs.index(move[3:])
            capturing     = True  
        else:
            ending_square = board_sqs.index(move[2:])
            capturing     = False

        if (list[move] in pieces):
            return 'move format invalid'

        piece_moved                 = self.board[ending_square]        
        self.board[starting_square] = piece_moved

        if (capturing):
            captured_piece = captured_pieces[-1]
            self.board[ending_square] = captured_piece
        else:
            self.board[ending_square] = EMPTY
        
        return self.board
        

    def __call__(self):
        return self.__get_current_board__()

    