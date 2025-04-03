from Chess.vars import *
def king(piece_pos: str, board: list[str]):
    current_pos = board_sqs.index(piece_pos)
    if (board[current_pos] != WKING and board[current_pos] != BKING):
        return -1
 
    color = board[current_pos][:3] 
    possible_moves = []    
    pve9 = pve7 = pve1 = pve8 = True
    nve9 = nve7 = nve1 = nve8 = True

    for i in range(0,10):
        if (i == 1 or i == 7 or i == 8 or i == 9):
            if (current_pos+i > 64 or current_pos+i < 0):
                if (i == 9):
                    pve9 = False  
                if (i == 1):
                    pve1 = False  
                if (i == 7):
                    pve7 = False  
                if (i == 8):
                   pve8 = False  
 
            if (current_pos-i > 64 or current_pos-i < 0):
                if (i == 9):
                    nve9 = False  
                if (i == 1):
                    nve1 = False  
                if (i == 7):
                    nve7 = False  
                if (i == 8):
                    nve8 = False         
    if (pve9): 
            if(board[current_pos+9][:3] != color):
                possible_moves.append(current_pos+9)
    if (nve9): 
            if(board[current_pos-9][:3] != color):
                possible_moves.append(current_pos-9)
    if (pve8): 
            if(board[current_pos+8][:3] != color):
                possible_moves.append(current_pos+8)
    if (nve8): 
            if(board[current_pos-8][:3] != color):
                possible_moves.append(current_pos-8)
    if (pve7): 
            if(board[current_pos+7][:3] != color):
                possible_moves.append(current_pos+7)
    if (nve7): 
            if(board[current_pos-7][:3] != color):
                possible_moves.append(current_pos-7)
    if (pve1): 
            if(board[current_pos+1][:3] != color):
                possible_moves.append(current_pos+1)
    if (nve1): 
            if(board[current_pos-1][:3] != color):
                possible_moves.append(current_pos-1)
 
 
    if (pve9):
        possible_moves.append(current_pos+9)
    if (nve9):
        possible_moves.append(current_pos-9)
    if (pve8):
        possible_moves.append(current_pos+8)
    if (nve8):
        possible_moves.append(current_pos-8)
    if (pve7):
        possible_moves.append(current_pos+7)
    if (nve7):
        possible_moves.append(current_pos-7)
    if (pve1):
        possible_moves.append(current_pos+1)
    if (nve1):
        possible_moves.append(current_pos-1)
 
    for i in possible_moves[:]:
        if (board[i][:3] == color):
            possible_moves.remove(i)
 
    ## casteling
       
    return possible_moves
 
