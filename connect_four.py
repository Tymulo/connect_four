def new_board(num_lns):
    board = []
    for i in range(num_lns):
        board.append(["","","","","","",""])
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

    for i in reversed(range(6)):
        if board[i -1][column] != " " or i == 0:
            if move % 2 == 1:
                board[i][column] = "X"
            else:
                board[i][column] = "O"
            move += 1
            return board, move

def check_hor(board, move):
    line = 0
    while line != 6:
        column = 0
        while column + 3 != 6:
            if board[line][column] + board[line][column+1] + board[line][column+2] + board[line][column+3] == move * 4:
                return True
            else:
                column += 1
        line += 1

# def check_ver(board, move):


if __name__ == "__main__":
    num_lns = 6
    board = new_board(num_lns)
    move = 1
    print_board(board)
    x = 0
    while x != 5:
        make_move(board, move)
        x += 1

    line = 5
    column = 0
    print_board(board)
    
    vic = check_hor(board, move)
    print(vic)

