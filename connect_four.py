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
        if t[i -1][column] != " " or i == 0:
            if move % 2 == 1:
                t[i][column] = "X"
            else:
                board[i][column] = "O"
            move += 1
            return board, move

# def check_victory_hov(board, last_move):
#     # last move




if __name__ == "__main__":
    num_lns = 6
    board = new_board(num_lns)
    move = 0
    print_board(board)


    print_board(board)



