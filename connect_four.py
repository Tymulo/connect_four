def make_board(num_lns):
    board = []
    for i in range(num_lns):
        board.append([" "," "," "," "," "," "," "])
    return board

def print_board(board):
    for line in board:
        print(line)

if __name__ == "__main__":
    num_col = 8
    num_lns = 6
    board = make_board(num_lns)
    move = 0

    print_board(board)


