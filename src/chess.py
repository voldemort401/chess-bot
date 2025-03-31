class chess:
    def __init__(self):
       self.WROOK   =   "0x0010"
       self.WKNIGHT =   "0x0111" 
       self.WBISHOP =   "0x0101"   
       self.WKING   =   "0x0000"  
       self.WQUEEN  =   "0x0110"   
       self.WPAWN   =   "0x0100"
       self.BROOK =     "0x1010" 
       self.BKNIGHT =   "0x1111"  
       self.BBISHOP =   "0x1101" 
       self.BKING =     "0x1000" 
       self.BQUEEN =    "0x1110" 
       self.BPAWN =     "0x1011"  

       self.EMPTY = "-0x1"
       self.BLACK = "0x1" 
       self.WHITE = "0x0"
       self.board      = []
       #self.board_color = [self.WHITE,  self.BLACK,  self.WHITE, self.BLACK, self.WHITE, self.BLACK, self.WHITE,  self.BLACK,
       #                    self.BLACK,  self.WHITE,  self.BLACK, self.WHITE, self.BLACK, self.WHITE, self.BLACK,  self.WHITE,
       #                    self.WHITE,  self.BLACK,  self.WHITE, self.BLACK, self.WHITE, self.BLACK, self.WHITE,  self.BLACK,
       #                    self.BLACK,  self.WHITE,  self.BLACK, self.WHITE, self.BLACK, self.WHITE, self.BLACK,  self.WHITE,
       #                    self.WHITE,  self.BLACK,  self.WHITE, self.BLACK, self.WHITE, self.BLACK, self.WHITE,  self.BLACK,
       #                    self.BLACK,  self.WHITE,  self.BLACK, self.WHITE, self.BLACK, self.WHITE, self.BLACK,  self.WHITE,
       #                    self.WHITE,  self.BLACK,  self.WHITE, self.BLACK, self.WHITE, self.BLACK, self.WHITE,  self.BLACK,
       #                    self.BLACK,  self.WHITE,  self.BLACK, self.WHITE, self.BLACK, self.WHITE, self.BLACK,  self.WHITE]
       #
       self.board_sqs = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
                    'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
                    'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
                    'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
                    'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 
                    'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
                    'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',    
                    'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',]                            

       #self.edges = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",
       #             "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
       #             "a2", "a3", "a4", "a5", "a6", "a7",
       #             "h2", "h3", "h4", "h5", "h6", "h7"]



    def Board(self, fen:str):
        from src.Board import board
        board = board(fen)
        return board.create_brd()

    def generatePseudoLegalMoves(self,board):
        from src.PseudolegalMoves import PseudoLegalMoves
        all_pseudo_moves    = {} 
        turn                = board[-1]
        PseudoLegal         = PseudoLegalMoves()
        for i,j in enumerate(board):
            if (j != self.EMPTY):
                if (turn == self.BLACK):
                    if (j == self.BKNIGHT):
                        all_pseudo_moves.update({'black-knight': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                    if (j == self.BKING):                     
                        all_pseudo_moves.update({'black-king': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                    if (j == self.BROOK):
                        all_pseudo_moves.update({'black-rook': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                    if (j == self.BBISHOP): 
                        all_pseudo_moves.update({'black-bishop': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                    if (j == self.BPAWN): 
                        all_pseudo_moves.update({'black-pawn': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                    if (j == self.BQUEEN):              
                        all_pseudo_moves.update({'black-queen': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                else:
                    if (j == self.WKNIGHT):                     
                        all_pseudo_moves.update({'white-knight': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                    if (j == self.WKING):              
                        all_pseudo_moves.update({'white-king': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                    if (j == self.WROOK):
                        all_pseudo_moves.update({'white-rook': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                    if (j == self.WBISHOP): 
                        all_pseudo_moves.update({'white-bishop': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                    if (j == self.WPAWN): 
                        all_pseudo_moves.update({'white-pawn': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                    if (j == self.WQUEEN):             
                        all_pseudo_moves.update({'white-queen': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
        return str(all_pseudo_moves)
