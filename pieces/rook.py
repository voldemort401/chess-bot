def rook(self,pos_piece: str, board: list[str], q=0) -> list[int | None]:
    pos = []
    piece = board[self.board_sqs.index(pos_piece)]

    piece_index = board.index(piece)
    piece_index2 = board.index(piece)
    
    piece_sq = self.board_sqs[piece_index] # find the pos of the piece in algebric notation 
    file,rank = piece_sq
    
    color = piece[:3]

    if (piece != self.BROOK and piece != self.WROOK and q==0):
        return [-1] 

    # vertical movements 
    for i in range(8):
        piece_index -= 8
        if (piece_index > 0):
            if (self.board_sqs[piece_index][0] == file):
                if ( board[piece_index] == self.EMPTY):
                    pos.append(piece_index)
                elif (board[piece_index][:3] != color):
                    pos.append(piece_index)
                    break
                elif (board[piece_index][:3] == color):
                    break

        piece_index2 += 8
        if (piece_index2 < 63):
            if (self.board_sqs[piece_index2][0] == file):
                if (board[piece_index2] == self.EMPTY):
                    pos.append(piece_index2)
                
                elif (board[piece_index2][:3] != color):
                    pos.append(piece_index2)
                    break 
                
                elif (board[piece_index2][:3] == color):
                    break
    


    piece_index = board.index(piece)
    piece_index2 = board.index(piece)
    # horizontal movements
    for i in range(8):
        piece_index  -= 1
        piece_index2 += 1 
        if (piece_index > 0):
            if (self.board_sqs[piece_index][1] == rank):
                if ( board[piece_index] == self.EMPTY or board[piece_index][:3] != color):
                    pos.append(piece_index)
        
                elif (board[piece_index][:3] != color):
                    pos.append(piece_index)
                    break
                
                elif (board[piece_index][:3] == color):
                    break


        if (piece_index2 < 63):
            if (self.board_sqs[piece_index2][1] == rank):
                if (board[piece_index2] == self.EMPTY):
                    pos.append(piece_index2)
                
                elif (board[piece_index2][:3] != color):
                    pos.append(piece_index2)
                    break 
                
                elif (board[piece_index2][:3] == color):
                    break
    
    return pos 

