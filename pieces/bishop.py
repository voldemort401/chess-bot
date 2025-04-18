from Chess.vars import *
def bishop(piece_pos: str, board: list[str], q=0 ): 
        if (board[board_sqs.index(piece_pos)] != BBISHOP and board[board_sqs.index(piece_pos)] != WBISHOP and q == 0):
            return -1 
        current_pos = board_sqs.index(piece_pos)
        color       = board[current_pos][:3]
        PIECE_POS = board_sqs.index(piece_pos)
        possible_pos = [] 
        pve9 = True 
        pve7 = False 

        nve9 = True
        nve7 = False 

        #comments time ::: pve9 or pve7  is to say like hey we can do +7 or +9 and get the actual squares the bishop can move and if the 
        # values are false it means stop right there dont do anymore we already got the values we need 

        for i in range(8):
            if (board_sqs[current_pos] in edges):
                if (current_pos > PIECE_POS):  
                    current_pos=PIECE_POS
                    pve7 = True
                    pve9 = False 
            
            if (current_pos+9 >64 or current_pos < 0):
                pve9=False
            if (current_pos+7 > 64 or current_pos <0):
                pve7=False

            if (current_pos-9 >64 or current_pos < 0):
                nve9=False
            if (current_pos-7 > 64 or current_pos <0):
                nve7=False

            if (pve9):    
                current_pos+=9
                if (board[current_pos] == EMPTY):
                    possible_pos.append(current_pos)
                elif (board[current_pos][:3] == color):
                    pve9 = False 

                elif (board[current_pos][:3] != color):
                    possible_pos.append(current_pos)
                    pve9 = False 
            if (pve7):
                current_pos+=7
                if (board[current_pos] == EMPTY):
                    possible_pos.append(current_pos)

                elif (board[current_pos][:3] != color ):
                    possible_pos.append(current_pos)
                    pve7 = False 
                elif (board[current_pos][:3] == color):
                    pve7 = False
                elif (board_sqs[current_pos] in edges):
                    possible_pos.append(current_pos)
                    pve7 = False


        current_pos = PIECE_POS
        for i in range(8):
            if (current_pos-9 >64 or current_pos < 0):
                nve9=False
            if (current_pos-7 > 64 or current_pos <0):
                nve7=False

            if (current_pos > 0 and current_pos < 64):
                if (board_sqs[current_pos] in edges):
                    if (current_pos < PIECE_POS):
                        current_pos=PIECE_POS
                        nve9 = False 
                        nve7 = True

            if (nve9):    
                current_pos -= 9
                if (board[current_pos] == EMPTY):
                    possible_pos.append(current_pos)
                elif (board[current_pos][:3] == color):
                    nve9 = False 

                elif (board[current_pos][:3] != color):
                    possible_pos.append(current_pos)
                    nve9 = False 

            if (nve7):
                current_pos -= 7
                if (board[current_pos] == EMPTY):
                    possible_pos.append(current_pos)
                elif (board[current_pos][:3] != color ):
                    possible_pos.append(current_pos)
                    nve7 = False 
                elif (board[current_pos][:3] == color):
                    nve7 = False
                elif (board_sqs[current_pos] in edges):
                    possible_pos.append(current_pos)
                    nve7 = False



        possible_pos=set(possible_pos)
        Cpossible_pos=set(possible_pos)
        for i,j in enumerate(Cpossible_pos):
            if (j > 63):
                possible_pos.remove(j)
            if (j < 0):
                possible_pos.remove(j)
        
        return list(possible_pos)
