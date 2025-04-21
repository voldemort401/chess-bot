from Chess.vars import *
def bishop(piece_pos: str, board: list[str], q=0 ): 
        if (board[board_sqs.index(piece_pos)] != BBISHOP and board[board_sqs.index(piece_pos)] != WBISHOP and q == 0):
            return -1 
        current_pos = board_sqs.index(piece_pos)
        current_pos2 = board_sqs.index(piece_pos)
        color       = board[current_pos][:3]
        PIECE_POS = board_sqs.index(piece_pos)

        possible_pos = [] 

        stop_increasing_current_pos = stop_increasing_current_pos2= False 
        for i in range(8):
            if (not stop_increasing_current_pos):
                current_pos-=9
            if (not stop_increasing_current_pos2):
                current_pos2-=7

            possible_pos.append(current_pos)
            possible_pos.append(current_pos2)

            if (current_pos < 63 and current_pos > 0):
                if (board[current_pos] != EMPTY and board[current_pos][:3] == color):
                    possible_pos.remove(current_pos)
                    stop_increasing_current_pos = True
                if (board[current_pos] != EMPTY and board[current_pos][:3] != color):
                    stop_increasing_current_pos = True
            if (current_pos2 < 63 and current_pos2 > 0):
                if (board[current_pos2] != EMPTY and board[current_pos2][:3] == color):
                    possible_pos.remove(current_pos2)
                    stop_increasing_current_pos2 = True
                if (board[current_pos2] != EMPTY and board[current_pos2][:3] != color):
                    stop_increasing_current_pos2 = True

        current_pos = PIECE_POS
        current_pos2 = PIECE_POS

        stop_increasing_current_pos = stop_increasing_current_pos2= False 

        for i in range(8):
            if (not stop_increasing_current_pos):
                current_pos+=9
            if (not stop_increasing_current_pos2):
                current_pos2+=7

            possible_pos.append(current_pos)
            possible_pos.append(current_pos2)
 
            if (current_pos < 63 and current_pos > 0):
                if (board[current_pos] != EMPTY and board[current_pos][:3] == color):
                    possible_pos.remove(current_pos)
                    stop_increasing_current_pos = True
                if (board[current_pos] != EMPTY and board[current_pos][:3] != color):
                    stop_increasing_current_pos = True
            if (current_pos2 < 63 and current_pos2 > 0):
                if (board[current_pos2] != EMPTY and board[current_pos2][:3] == color):
                    possible_pos.remove(current_pos2)
                    stop_increasing_current_pos2 = True
                if (board[current_pos2] != EMPTY and board[current_pos2][:3] != color):
                    stop_increasing_current_pos2 = True



        possible_pos=list(set(possible_pos))
        for i in possible_pos[:]:
            if (i > 63):
                possible_pos.remove(i)
            elif (i < 0):
                possible_pos.remove(i)
            elif (board[i] != EMPTY and board[i][:3] == color):
                possible_pos.remove(i)

        return set(possible_pos)
