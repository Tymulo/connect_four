def new_board(num_lns):
    board = []
    for i in range(num_lns):
        board.append(["q","","","","","",""])
    return board

def print_board(board):
    for line in board:
        print(line)

def make_move(board, move):
    column = (int(input("Column you want to place in ")) - 1)

    while column > (len(board) - 1) or column < 0 or (board[0][column]) != "":
        print("Invalid column ")
        new_column = (int(input("Column you want to place in ")) - 1)
        column = new_column

    for i in reversed(range(5)):
        if board[i][column] != "":
            if move == "X":
                board[i+1][column] = "X"
                return board
            if move == "O":
                board[i+1][column] = "O"
                return board
        if i == 0:
            if move == "X":
                board[i][column] = "X"
                return board
            if move == "O":
                board[i][column] = "O"
                return board

# def check_victory_hov(board, last_move):
#     # last move




if __name__ == "__main__":
    num_col = 8
    num_lns = 6
    board = new_board(num_lns)
    move = "X"
    print_board(board)
    move = make_move(board, move)
    print(move)