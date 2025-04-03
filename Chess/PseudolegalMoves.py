from Chess.chess import Chess 
class PseudoLegalMoves(Chess):
    def __init__(self):
        super(PseudoLegalMoves,self).__init__()
        self.board_color = [self.WHITE,  self.BLACK,  self.WHITE, self.BLACK, self.WHITE, self.BLACK, self.WHITE,  self.BLACK,
                           self.BLACK,  self.WHITE,  self.BLACK, self.WHITE, self.BLACK, self.WHITE, self.BLACK,  self.WHITE,
                           self.WHITE,  self.BLACK,  self.WHITE, self.BLACK, self.WHITE, self.BLACK, self.WHITE,  self.BLACK,
                           self.BLACK,  self.WHITE,  self.BLACK, self.WHITE, self.BLACK, self.WHITE, self.BLACK,  self.WHITE,
                           self.WHITE,  self.BLACK,  self.WHITE, self.BLACK, self.WHITE, self.BLACK, self.WHITE,  self.BLACK,
                           self.BLACK,  self.WHITE,  self.BLACK, self.WHITE, self.BLACK, self.WHITE, self.BLACK,  self.WHITE,
                           self.WHITE,  self.BLACK,  self.WHITE, self.BLACK, self.WHITE, self.BLACK, self.WHITE,  self.BLACK,
                           self.BLACK,  self.WHITE,  self.BLACK, self.WHITE, self.BLACK, self.WHITE, self.BLACK,  self.WHITE]
       
        self.edges = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",
                      "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
                      "a2", "a3", "a4", "a5", "a6", "a7",
                      "h2", "h3", "h4", "h5", "h6", "h7"]

    
    def _rook(self,pos_piece: str, board: list[str]) -> list[int | None]:
        from pieces.rook import rook
        return rook(self, pos_piece,board)

    def _bishop(self,piece_pos: str, board: list[str] ) -> list[str]|int: 
        from pieces.bishop import bishop
        return bishop(self,piece_pos,board)

    def _queen(self, piece_pos: str, board: list[str]):
        from pieces.bishop import bishop
        from pieces.rook import rook
        return bishop(self,piece_pos, board, 1) + rook(self,piece_pos,board, 1)


    def _pawn(self,piece_pos:str, board:list[str]):
        from pieces.pawn import pawn
        return pawn(self,piece_pos,board)

    def _king(self, piece_pos: str, board: list[str]):
        from pieces.king import king
        return king(self,piece_pos,board)
    
    def _knight(self,piece_pos: str, board: list[str]):
        from pieces.knight import knight 
        return knight(self,piece_pos,board)

