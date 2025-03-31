def pawn(self,piece_pos:str, board:list[str]):
    piece_index = self.board_sqs.index(piece_pos)
    file,rank = piece_pos
    color = board[piece_index][:3]

    plegal_sq = []

    canMove2squares = True
    if (color == self.WHITE and file == 2):
        canMove2squares = True
    if (color == self.BLACK and file == 7):
        canMove2squares = True
    
    if (canMove2squares and color == self.WHITE):
        plegal_sq.append(piece_index-8)
        plegal_sq.append(piece_index-16)

    if (canMove2squares and color == self.BLACK):
        plegal_sq.append(piece_index+8)
        plegal_sq.append(piece_index+16)
    
    if (not canMove2squares and color==self.WHITE):
        plegal_sq.append(piece_index-8)
    if (not canMove2squares and color==self.BLACK):
        plegal_sq.append(piece_index+8) 
    

    ## ENPASSANT

    return plegal_sq
