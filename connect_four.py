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
        return 0
    else:
        return 1

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
            victory = victory_checker(board, move)
            if victory == True:
                return board, move, victory
            else:
                move += 1
                return board, move, victory
        elif i == 5:
            board[i][column] = symbol
            victory = victory_checker(board, move)
            if victory == True:
                return board, move, victory
            else:
                move += 1
                return board, move, victory

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

def add_points(board, move):
    for i in range(7):
        if board[0][i] == " ":
            t = copy.deepcopy(board)
            t, _, victory = make_move(t, move, i)
            if victory_checker(t, move):
                return 1

    for j in range(7):
        if board[0][j] == " ":
            d = copy.deepcopy(board)
            d, _, victory = make_move(d, move + 1, j)
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
                t, _, victory = make_move(t, move, i)
                score = min_max(t, move + 1, depth - 1, bot_move + 1)
                best_score = max(best_score, score)
        return best_score
    else:  
        best_score = float("inf")
        for i in range(7):
            if board[0][i] == " ":
                t = copy.deepcopy(board)
                t, _, victory = make_move(t, move, i)
                score = min_max(t, move + 1, depth - 1, bot_move + 1)
                best_score = min(best_score, score)
        return best_score


def hard_bot(board, move):
    best_score = -float("inf")
    best_col = None

    for i in range(7):
        if board[0][i] == " ":
            t = copy.deepcopy(board)
            t, _, victory = make_move(t, move, i)
            if victory_checker(t, move):
                return i

    for j in range(7):
        if board[0][j] == " ":
            d = copy.deepcopy(board)
            d, _, victory = make_move(d, move + 1, j)
            if victory_checker(d, move + 1):
                return j

    for x in range(7):
        if board[0][x] == " ":
            t = copy.deepcopy(board)
            t, _, victory = make_move(t, move, x)
            score = min_max(t, move + 1, depth=4, bot_move=1)
            if score > best_score:
                best_score = score
                best_col = x

    return best_col

def play_again(next):
    global next_game
    next_game = next
    root.destroy()


def draw_button(surface, x, y, width, height, text, font, color):
    pygame.draw.rect(surface, color, (x, y, width, height))
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    surface.blit(text_surface, text_rect)


def calculate_cell_size(Y, num_row):
    y = (Y // num_row) - 20
    return y

def draw_grid(surface, cell_size, color, num_row, num_col, symbol_1, symbol_2, board):
    pos_y = 40
    for r in range(num_row):
        pos_x = 40
        for c in range(num_col):
            cell = pygame.Rect(pos_x, pos_y, cell_size, cell_size)
            pygame.draw.rect(surface, color, cell)
            
            if board[r][c] == "O":
                symbol_rect = symbol_1.get_rect(center=cell.center)
                surface.blit(symbol_1, symbol_rect)
            if board[r][c] == "X":
                symbol_rect = symbol_2.get_rect(center=cell.center)
                surface.blit(symbol_2, symbol_rect)
            pos_x += (cell_size + 10)
        pos_y += (cell_size + 10)

def grid_size(num_row, num_col, cell_size):
    start_x, start_y = 40, 40
    width = num_col * cell_size + (num_col - 1) * 10
    height = num_row * cell_size + (num_row - 1) * 10
    return pygame.Rect(start_x, start_y, width, height)


def click_move(cell_size, num_col, board, move):
    mouse = pygame.mouse.get_pos()
    mouse_x = mouse[0] - 40
    

    column = mouse_x // (cell_size + 10)
    if column > (len(board)) or column < 0 or (board[0][column]) != " ":
        print("Invalid column ")
        return board, move
    else:
        
        board, move, victory = make_move(board, move, column)
        
        return board, move, victory, column


if __name__ == "__main__":
    import random
    import tkinter as tk
    import copy
    import pygame

    game_mode = None

    num_row = 6
    num_col = 7

    board = new_board(num_row)

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

    pause = False
    music_playing = True
    global move
    move = choose_symbol()
    bot_id = copy.deepcopy(move)
    bot_id = (bot_id + 1) % 2
    next_game = True
    pygame.init()
    pygame.mixer.init()
    X, Y = 1280, 720
    white = (255, 255, 255)
    blue = (0, 0, 128)
    gray = (128, 128, 128)
    pygame.display.set_caption("Simulation")
    pauza = pygame.image.load("Pauza.png")
    wyjscie = pygame.image.load("Exit.png")
    wyjscie_rect = wyjscie.get_rect(center=(X//2 + 150, Y//2 + 60))
    wyjscie_clicked = False

    # dzwiek = pygame.image.load("Sound.png")
    # Nie_dzwiek = pygame.image.load("Not_sound.png")
    # dzwiek_rect = dzwiek.get_rect(center=(X//2 - 150, Y//2 + 60))

    display_surface = pygame.display.set_mode((X, Y))
    font = pygame.font.Font('freesansbold.ttf', 18)

    cell_size = calculate_cell_size(Y, num_row)
    grid_rect = grid_size(num_row, num_col, cell_size)

    # pygame.mixer.music.load("muzyka.mp3")
    # pygame.mixer.music.set_volume(0.5)
    # pygame.mixer.music.play(-1)


    blue_circle = pygame.image.load("blue_circle.png").convert_alpha()
    red_circle = pygame.image.load("red_circle.png").convert_alpha()
    player_symbol_1 = pygame.transform.smoothscale(blue_circle, (cell_size - 20, cell_size - 20))
    player_symbol_2 = pygame.transform.smoothscale(red_circle, (cell_size - 20, cell_size - 20))

    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
            if event.type == pygame.MOUSEBUTTONDOWN:
                if wyjscie_rect.collidepoint(event.pos) and pause:  
                    wyjscie_clicked = True
                if grid_rect.collidepoint(event.pos) and move % 2 != bot_id:
                    board, move, victory, column = click_move(cell_size, num_col, board, move)
                    
                    if victory == True:
                        symbol = get_player_symbol(move)
                        print(f'The player {symbol} won!!!')
                        running = False
        if game_mode != "2p":        
            if move % 2 == bot_id:
                if game_mode == "easy":
                    column = bot_easy(board, column, move)
                if game_mode == "medium":
                    column = medium_bot(board, move)
                if game_mode == "hard":
                    column = hard_bot(board, move)
                board, move, victory = make_move(board, move, column) 
                if victory == True:
                    symbol = get_player_symbol(move)
                    print(f'The player {symbol} won!!!')
                    running = False

        display_surface.fill(gray)
        draw_grid(display_surface, cell_size, white, num_row, num_col, player_symbol_1, player_symbol_2, board)
        
        
        if pause == True:
            pauza_rect = pauza.get_rect(center=(X // 2, Y // 2))
            display_surface.blit(pauza, pauza_rect)
            display_surface.blit(wyjscie, wyjscie_rect)

            # if music_playing:
            #     display_surface.blit(dzwiek, dzwiek_rect)
            # else:
            #     display_surface.blit(Nie_dzwiek, dzwiek_rect)

            if wyjscie_clicked:
                running = False

                # elif dzwiek_rect.collidepoint(event.pos) and pause: 
                #     if music_playing:
                #         pygame.mixer.music.pause()
                #         music_playing = False
                #     else:
                #         pygame.mixer.music.unpause()
                #         music_playing = True

        pygame.display.flip()
    pygame.quit()

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

    # while next_game == True:
    #     board = new_board(num_row)
    #     print_board(board, move)
    #     victory = False
    #     if game_mode != "2p":
    #         while victory != True:
    #             symbol = get_player_symbol(move)
    #             print(f'Player {symbol} move')
    #             if move % 2 == bot_id:
    #                 if game_mode == "easy":
    #                     column = bot_easy(board, column, move)
    #                 if game_mode == "medium":
    #                     column = medium_bot(board, move)
    #                 if game_mode == "hard":
    #                     column = hard_bot(board, move)
    #             else:
    #                 column = player_input(board)
    #             make_move(board, move, column)
    #             print_board(board, move)
    #             victory = victory_checker(board, move)
    #             move += 1
    #     else:
    #         while victory != True:
    #             symbol = get_player_symbol(move)
    #             print(f'Player {symbol} move')
    #             column = player_input(board)
    #             make_move(board, move, column)
    #             print_board(board, move)
    #             victory = victory_checker(board, move)
    #             move += 1
    #     print(board)
    #     print(f'The player {symbol} won!!!')

    

       
