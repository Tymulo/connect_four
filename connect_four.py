def new_board(num_lns):
    board = []
    for i in range(num_lns):
        board.append([" "," "," "," "," "," "," "])
    return board

def print_board(board):
    print("  1    2    3    4    5    6    7")
    for line in board:
        print(line)
        
def wybierz():
    x = 3
    while x != 1 and x !=2:
        x = int(input("Chose O (nr 1) or X (nr. 2). To chose click on your keyboard 1 or 2 "))
        if x!= 1 and x!= 2:
            print("There's no option ", x)
    if x == 1:
        return 0
    else:
        return 1
        
def make_move(board, move):
    symbol = get_player_symbol(move)
    column = (int(input("Column you want to place in ")) - 1)
    while column > (len(board)) or column < 0 or (board[0][column]) != " ":
        print("Invalid column ")
        new_column = (int(input("Column you want to place in ")) - 1)
        column = new_column

    for i in range(6):
        if board[i][column] != " ":
            board[i-1][column] = symbol
            move += 1
            return board, move
        elif i == 5:
            board[i][column] = symbol
            move += 1
            return board, move

def check_hor(board, move):
    move = get_player_symbol(move)
    line = 0
    while line != 6:
        column = 0
        while column + 3 != 7:
            if board[line][column] + board[line][column+1] + board[line][column+2] + board[line][column+3] == move * 4:
                return True
            else:
                column += 1
        line += 1
    return False

def check_ver(board, move):
    move = get_player_symbol(move)   
    line = 0
    while line + 3 != 6:
        column = 0
        while column != 7:
            if board[line][column] + board[line+1][column] + board[line+2][column] + board[line+3][column] == move * 4:
                return True
            else:
                column += 1
        line += 1
    return False

def check_diag(board, move):
    move = get_player_symbol(move)
    line = 0
    while line + 3 != 6:
        column = 0
        while column + 3 != 7:
            if board[line][column] + board[line+1][column+1] + board[line+2][column+2] + board[line+3][column+3] == move * 4:
                return True
            if board[line][column+3] + board[line+1][column+2] + board[line+2][column+1] + board[line+3][column] == move * 4:
                return True
            else:
                column += 1
        line += 1
    return False


def victory_checker(board, move):
    hor = check_hor(board, move)
    ver = check_ver(board, move)
    diag = check_diag(board,move)
    if hor == True or ver == True or diag == True:
        return True
    else:
        return False


def get_player_symbol(move):
    if move % 2 == 1:
        return "X"
    else:
        return "O"


if __name__ == "__main__":
    num_lns = 6
    board = new_board(num_lns)
    
    print_board(board)
    move = wybierz()

    victory = False
    while victory != True:
        symbol = get_player_symbol(move)
        print(f'Player {symbol} move')
        make_move(board, move)
        print_board(board)
        victory = victory_checker(board, move)
        move += 1

    print(f'The player {symbol} won!!!')
    

    # hor = check_hor(board, move)
    # ver = check_ver(board, move)
    # diag = check_diag(board,move)

    # print(f'Horizontal victory: {hor}')
    # print(f'Vertical victory: {ver}')
    # print(f'Diagonal victory: {diag}')

