from Chess.vars import *
def knight(piece_pos:str, board:list[str]):
    current_pos = board_sqs.index(piece_pos)+16
    current_pos2 = board_sqs.index(piece_pos)+16
    possible_moves = set() 

    if (board[current_pos-16] != BKNIGHT and board[current_pos-16]!= WKNIGHT):
        return -1 
    # create a kind of circle around the knight
    for i in range(8):
        if (i == 0):
            current_pos-=1
            current_pos2+=1
        else:
            if (i == 1):
                if (current_pos2 > current_pos):
                    current_pos-=9
                    current_pos2-=7
                else:
                    current_pos2-=9
                    current_pos-=7
            if (i in (2,3)):
                current_pos-=8
                current_pos2-=8
                possible_moves.add(current_pos)
                possible_moves.add(current_pos2)

            if (i == 3):
                if (current_pos2 > current_pos):
                    current_pos-=7
                    current_pos2-=9
                else:
                    current_pos2-=7
                    current_pos-=9
         
        possible_moves.add(current_pos)
        possible_moves.add(current_pos2)
    possible_moves = list(possible_moves)

    for i,j in enumerate(possible_moves[:]):
        if (j<0):
            possible_moves.remove(j)
        elif (j>63):
            possible_moves.remove(j)
        else:
            try:
                if (board_color[j] == board_color[board_sqs.index(piece_pos)]):
                    possible_moves.remove(j)
            except IndexError:
                pass

    for i in possible_moves[:]:
        if(board[i][:3] == board[board_sqs.index(piece_pos)][:3]):
            possible_moves.remove(i)
    

    ## prevents the warping of circle all the way around when the piece is in the edge
    ##PS:: I am not a great explainer if you dont get it just comment this block out and run the test again
    ranks = ["a","b","c","d","e","f","g","h"]
    for i in possible_moves[:]:
        current_pos=board_sqs.index(piece_pos)
        curr_rank = board_sqs[current_pos][0]
        r_pm_l    = board_sqs[i][0]
        if (ranks.index(curr_rank)+1 ==   ranks.index(r_pm_l) or ranks.index(curr_rank)-1 == ranks.index(r_pm_l)):
            pass
        elif (ranks.index(curr_rank)+2 == ranks.index(r_pm_l) or ranks.index(curr_rank)-2 == ranks.index(r_pm_l)):
            pass
        else:
            possible_moves.remove(i)
    return set(possible_moves)
