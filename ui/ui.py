
## probably deprecated i think i will xboard or something like that later
import pygame
from src.chess import chess
class draw_brd(chess):
    def __init__(self):
        self.height  : int = 518 ## : int makes the warnings go away
        self.breadth : int = 518
        self.running : int = True


        pygame.init() 
        self.screen :  pygame.surface.Surface    = pygame.display.set_mode((self.height, self.breadth), DOUBLEBUF) 
        self.bg     :  pygame.surface.Surface    = pygame.image.load('board.png').convert_alpha()

        self.W_ROOK  : pygame.surface.Surface = pygame.image.load('W_rook.png').convert_alpha() 
        self.W_KNIGHT: pygame.surface.Surface = pygame.image.load('W_knight.png').convert_alpha() 
        self.W_BISHOP: pygame.surface.Surface = pygame.image.load('W_bishop.png').convert_alpha() 

        self.W_KING :  pygame.surface.Surface = pygame.image.load('W_king.png').convert_alpha()
        self.W_QUEEN:  pygame.surface.Surface = pygame.image.load('W_queen.png').convert_alpha()

        self.B_ROOK  : pygame.surface.Surface   =   pygame.image.load('B_rook.png').convert_alpha() 
        self.B_KNIGHT: pygame.surface.Surface   = pygame.image.load('B_knight.png').convert_alpha() 
        self.B_BISHOP: pygame.surface.Surface   = pygame.image.load('B_bishop.png').convert_alpha()
        self.B_KING  : pygame.surface.Surface   =   pygame.image.load('B_king.png').convert_alpha()
        self.B_QUEEN : pygame.surface.Surface   =  pygame.image.load('B_queen.png').convert_alpha()

        self.W_PAWN  : pygame.surface.Surface   = pygame.image.load('W_pawn.png').convert_alpha()
        self.B_PAWN  : pygame.surface.Surface   = pygame.image.load('B_pawn.png').convert_alpha()
         

    def _events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.running = False

    def _main_loop(self, board: list[str], sqs:list[int]):
        self.screen.blit(self.bg)
        pieces = pygame.Rect((0,0,64,64))
        p = pygame.Rect((0,0,64,64))
        color = ""

        mx,my = pygame.mouse.get_pos()
        mouse_sq = pygame.Rect(mx,my,12,12)
        
        for i in range(64):
           ## RENDERING THE PIECES 
            if (board[i] == self.WPAWN):
                self.screen.blit(self.W_PAWN,(pieces.x-10, pieces.y-20)) 
            if (board[i] == self.WBISHOP):
                self.screen.blit(self.W_BISHOP,(pieces.x-10, pieces.y-20)) 
            if (board[i] == self.WROOK):
                self.screen.blit(self.W_ROOK,(pieces.x-10, pieces.y-20)) 
            if (board[i] == self.WKING):
                self.screen.blit(self.W_KING,(pieces.x-10, pieces.y-20)) 
            if (board[i] == self.WQUEEN):
                self.screen.blit(self.W_QUEEN,(pieces.x-10, pieces.y-20)) 
            if (board[i] == self.WKNIGHT):
                self.screen.blit(self.W_KNIGHT,(pieces.x-10, pieces.y-20)) 

            if (board[i] == self.BPAWN):
                self.screen.blit(self.B_PAWN,(pieces.x-10, pieces.y+5)) 
            if (board[i] == self.BBISHOP):
                self.screen.blit(self.B_BISHOP,(pieces.x-10, pieces.y+5)) 
            if (board[i] == self.BROOK):
                self.screen.blit(self.B_ROOK,(pieces.x-10, pieces.y+5)) 
            if (board[i] == self.BKING):
                self.screen.blit(self.B_KING,(pieces.x-10, pieces.y+5)) 
            if (board[i] == self.BQUEEN):
                self.screen.blit(self.B_QUEEN,(pieces.x-10, pieces.y+5))  
            if (board[i] == self.BKNIGHT):
                self.screen.blit(self.B_KNIGHT,(pieces.x-10, pieces.y+5)) 

            if (i in sqs):
                color="green"
                pygame.draw.rect(self.screen,color,pieces)


            pieces.x += 69 
            i+=1
            if (i%8 == 0):
                pieces.y += 69  # nice (¬‿¬)
                pieces.x -= 69*8
            """
            if (pygame.mouse.get_just_pressed()[0] and mouse_sq.colliderect(pieces)):
                clicked = board[i]
                index = i 
                turn = board[-1]
                PseudoMvs=PseudoLegalMoves()
                if (clicked == WROOK or clicked == BROOK):
                    moves = (PseudoMvs._rook(index,board))
                    if (moves == []):
                        break 
                    
                    else:
                        if (index in moves):
                            if (pygame.mouse.get_just_pressed()[0] and mouse_sq.colliderect(pieces)):
                                if (board[i] == EMPTY or board[i][:3] != turn and i in moves):
                                    pass
            """


        pygame.display.flip()

    def exec(self, board:list[str], sqs:list[int]):
        while (self.running):
            self._events()
            self._main_loop(board, sqs)
