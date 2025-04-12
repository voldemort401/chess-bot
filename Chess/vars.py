WROOK   =   "0x0010"
WKNIGHT =   "0x0111" 
WBISHOP =   "0x0101"   
WKING   =   "0x0000"  
WQUEEN  =   "0x0110"   
WPAWN   =   "0x0100"
BROOK =     "0x1010" 
BKNIGHT =   "0x1111"  
BBISHOP =   "0x1101" 
BKING =     "0x1000" 
BQUEEN =    "0x1110" 
BPAWN =     "0x1011"  

EMPTY = "-0x1"
BLACK = "0x1" 
WHITE = "0x0"
board      = []

moves_played = []
captured_pieces = [] 
king_moved, rook_moved = [[0,0], [0,0]]
half_move_clock = 0

board_sqs = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
             'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
             'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
             'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
             'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 
             'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
             'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',    
             'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',]                            

board_color = [WHITE,  BLACK,  WHITE, BLACK, WHITE, BLACK, WHITE,   BLACK,
               BLACK,  WHITE,  BLACK, WHITE, BLACK, WHITE, BLACK,   WHITE,
               WHITE,  BLACK,  WHITE, BLACK, WHITE, BLACK, WHITE,   BLACK,
               BLACK,  WHITE,  BLACK, WHITE, BLACK, WHITE, BLACK,   WHITE,
               WHITE,  BLACK,  WHITE, BLACK, WHITE, BLACK, WHITE,   BLACK,
               BLACK,  WHITE,  BLACK, WHITE, BLACK, WHITE, BLACK,   WHITE,
               WHITE,  BLACK,  WHITE, BLACK, WHITE, BLACK, WHITE,   BLACK,
               BLACK,  WHITE,  BLACK, WHITE, BLACK, WHITE, BLACK,   WHITE]

edges = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",
        "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
        "a2", "a3", "a4", "a5", "a6", "a7",
        "h2", "h3", "h4", "h5", "h6", "h7"]