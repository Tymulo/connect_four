def new_board(num_lns):
    board = []
    for i in range(num_lns):
        board.append([" "," "," "," "," "," "," "])
    return board

def print_board(board, move):
    print(" ")
    print("move: ", move + 1)
    print("  1    2    3    4    5    6    7")
    for line in board:
        print(line)
        
def choose_symbol():
    x = 3
    while x != 1 and x !=2:
        x = int(input("Chose O (nr 1) or X (nr. 2). To chose click on your keyboard 1 or 2 "))
        if x!= 1 and x != 2:
            print("There's no option ", x)

    if x == 1:
        return 0, False
    else:
        return 1, False

def get_player_symbol(move):
    if move % 2 == 1:
        return "X"
    else:
        return "O"
    

def make_move(board, move, column):
    symbol = get_player_symbol(move)
    for i in range(6):
        if board[i][column] != " ":
            board[i-1][column] = symbol
            move += 1
            return board, move
        elif i == 5:
            board[i][column] = symbol
            move += 1
            return board, move

def player_input(board):
    column = (int(input("Column you want to place in ")) - 1)
    while column > (len(board)) or column < 0 or (board[0][column]) != " ":
        print("That column is full ")
        new_column = (int(input("Column you want to place in ")) - 1)
        column = new_column
    return column

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


def set_mode(mode):
    global game_mode
    game_mode = mode
    root.destroy()
    if game_mode == "2p":
        print("2p")
    elif game_mode == "easy":
        print("easy")
    elif game_mode == "medium":
        print("medium")
    elif game_mode == "hard":
        print("hard")


def bot_easy(board, x, move):
    if move < 5:
        column = random.randint(2, 4)
    else:
        z = random.randint(0, 100)
        if z%5 == 0:
            column = random.randint(1, 7)
        elif z%5 == 1 or z%5 == 2:
            column = x
        else:
            column = x + random.choice([-1, 1])
    while column > (len(board)) or column < 0 or (board[0][column]) != " ":
        new_column = column = bot_easy(board, x, move)
        column = new_column
    return column

def medium_bot(board, move):
    for i in range(7):
        if board[0][i] == " ":
            t = copy.deepcopy(board)
            make_move(t, move, i)
            if victory_checker(t, move):
                return i
    for j in range(7):
        if board[0][j] == " ":
            d = copy.deepcopy(board)
            make_move(d, move + 1, j)
            if victory_checker(d, move + 1):
                return j
    if move < 4:
        column = random.randint(2, 4)
        return column
    elif move >4 and move <8:
        column = random.randint(1, 5)
    else:
        column = random.randint(0, 6)
    return column

def play_again(next):
    global next_game
    next_game = next
    root.destroy()


if __name__ == "__main__":
    import random
    import tkinter as tk
    import copy
    import pygame

    game_mode = None

    num_lns = 6
    board = new_board(num_lns)
    move = 0

    root = tk.Tk()
    root.title("Choose game mode")
    root.geometry("350x250")

    label = tk.Label(root, text="Chose game mode:", font=("Arial", 14))
    label.pack(pady=20)

    btn1 = tk.Button(root, text="2 Players", width=10, command=lambda: set_mode("2p"))
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Easy Bot", width=10, command=lambda: set_mode("easy"))
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Medium Bot", width=10, command=lambda: set_mode("medium"))
    btn3.pack(pady=5)

    btn4 = tk.Button(root, text="Hard Bot", width=10, command=lambda: set_mode("hard"))
    btn4.pack(pady=5)

    root.mainloop()

    print_board(board, move)

    move, bot = choose_symbol()
    bot_id = copy.deepcopy(move)
    bot_id = (bot_id + 1) % 2
    next_game = True

    while next_game == True:
        board = new_board(num_lns)
        print_board(board, move)
        victory = False
        if game_mode != "2p":
            while victory != True:
                symbol = get_player_symbol(move)
                print(f'Player {symbol} move')
                if move % 2 == bot_id:
                    if game_mode == "easy":
                        column = bot_easy(board, column, move)
                    if game_mode == "medium":
                        column = medium_bot(board, move)
                    if game_mode == "hard":
                        column = medium_bot(board, move)
                else:
                    column = player_input(board)
                make_move(board, move, column)
                print_board(board, move)
                victory = victory_checker(board, move)
                move += 1
        else:
            while victory != True:
                symbol = get_player_symbol(move)
                print(f'Player {symbol} move')
                column = player_input(board)
                make_move(board, move, column)
                print_board(board, move)
                victory = victory_checker(board, move)
                move += 1
        print(board)
        print(f'The player {symbol} won!!!')

    

        root = tk.Tk()
        root.title("Play again")
        root.geometry("350x250")

        label = tk.Label(root, text="Do you want to play again", font=("Arial", 14))
        label.pack(pady=20)

        btn1 = tk.Button(root, text="Yes", width=10, command=lambda: play_again(True))
        btn1.pack(pady=5)
        btn2 = tk.Button(root, text="No", width=10, command=lambda: play_again(False))
        btn2.pack(pady=5)
        root.mainloop()