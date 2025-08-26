import random

def medium_bot(board, move):
    if move < 6:
        column = random.randint(2, 4)
        return column
    elif move >6 and move <10:
        column = random.randint(1, 5)
    else:
        column = random.randint(0, 6)
    for i in range(7):
        if(board[5][i] == " "):
            t = copy.deepcopy(board)
            make_move(t, move, i)
            if victory_checker(t, move):
                return i
            else:
                for j in range(7):
                    if(board[5][j] == " "):
                        d = copy.deepcopy(t)
                        make_move(d, move + 1, j)
                        if victory_checker(t, move + 1):
                            if i != j:
                                return j
    return column
                                
                    
