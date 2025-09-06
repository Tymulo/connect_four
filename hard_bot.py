import copy

def add_points(board, move):
    for i in range(7):
        if board[0][i] == " ":
            t = copy.deepcopy(board)
            t, _ = make_move(t, move, i)
            if victory_checker(t, move):
                return 1

    for j in range(7):
        if board[0][j] == " ":
            d = copy.deepcopy(board)
            d, _ = make_move(d, move + 1, j)
            if victory_checker(d, move + 1):
                return -1

    return 0


def min_max(board, move, depth, bot_move):
    if depth == 0 or victory_checker(board, move):
        return add_points(board, move)

    if bot_move % 2 == 0:  
        best_score = -float("inf")
        for i in range(7):
            if board[0][i] == " ":
                t = copy.deepcopy(board)
                t, _ = make_move(t, move, i)
                score = min_max(t, move + 1, depth - 1, bot_move + 1)
                best_score = max(best_score, score)
        return best_score
    else:  
        best_score = float("inf")
        for i in range(7):
            if board[0][i] == " ":
                t = copy.deepcopy(board)
                t, _ = make_move(t, move, i)
                score = min_max(t, move + 1, depth - 1, bot_move + 1)
                best_score = min(best_score, score)
        return best_score


def hard_bot(board, move):
    best_score = -float("inf")
    best_col = None

    for i in range(7):
        if board[0][i] == " ":
            t = copy.deepcopy(board)
            t, _ = make_move(t, move, i)
            if victory_checker(t, move):
                return i

    for j in range(7):
        if board[0][j] == " ":
            d = copy.deepcopy(board)
            d, _ = make_move(d, move + 1, j)
            if victory_checker(d, move + 1):
                return j

    for x in range(7):
        if board[0][x] == " ":
            t = copy.deepcopy(board)
            t, _ = make_move(t, move, x)
            score = min_max(t, move + 1, depth=6, bot_move=1)
            if score > best_score:
                best_score = score
                best_col = x

    return best_col


            
        
    
    
