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


def set_mode(mode, root):
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
        while board[0][column] != " ":
            column = random.randint(1, 5)
    else:
        column = random.randint(0, 6)
        while board[0][column] != " ":
            column = random.randint(0, 6)
    return column

def evaluate_window(window, symbol):
    if (symbol == "X"):
        opp_symbol = "O"
    else:
        opp_symbol = "X"
        
    score = 0

    if window.count(symbol) == 4:        
        score += 1000
    elif window.count(symbol) == 3 and window.count(" ") == 1:
        score += 10                      
    elif window.count(symbol) == 2 and window.count(" ") == 2:
        score += 5                      

    if window.count(opp_symbol) == 3 and window.count(" ") == 1:
        score -= 80                     
    elif window.count(opp_symbol) == 2 and window.count(" ") == 2:
        score -= 10 

    return score


def evaluate(board, symbol):
    score = 0
    rows = len(board)
    cols = len(board[0])

    center_col = cols // 2
    center_array = [board[r][center_col] for r in range(rows)]
    score += center_array.count(symbol) * 6
    
    for r in range(rows):
        for c in range(cols - 3):
            window = board[r][c:c+4]
            score += evaluate_window(window, symbol)

    for c in range(cols):
        for r in range(rows - 3):
            window = [board[r+i][c] for i in range(4)]  
            score += evaluate_window(window, symbol)

    for r in range(rows - 3):
        for c in range(cols - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, symbol)

    for r in range(rows - 3):
        for c in range(3, cols):
            window = [board[r+i][c-i] for i in range(4)]
            score += evaluate_window(window, symbol)

    return score

def is_terminal(board):
    return (victory_checker(board, 0) or victory_checker(board, 1) or  all(board[0][c] != " " for c in range(7)))
                                            
def min_max(board, depth, alpha, beta, maximizing, symbol):
    valid_moves = [c for c in range(7) if board[0][c] == " "]

    if (symbol == "X"):
        bot_parity = 1
    else:
        bot_parity = 0
    opp_parity = 1 - bot_parity
        
    if depth == 0 or is_terminal(board):
        return evaluate(board, symbol), None  

    if maximizing:
        value = -float("inf")  
        best_col = random.choice(valid_moves)
        for col in valid_moves:
            b_copy = copy.deepcopy(board)
            make_move(b_copy, bot_parity, col)   
            new_score, _ = min_max(b_copy, depth-1, alpha, beta, False, symbol)
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:  
                break
        return value, best_col

    else:
        value = float("inf")  
        best_col = random.choice(valid_moves)
        for col in valid_moves:
            b_copy = copy.deepcopy(board)
            make_move(b_copy, opp_parity, col)  
            new_score, _ = min_max(b_copy, depth-1, alpha, beta, True, symbol)
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:  
                break
        return value, best_col


def hard_bot(board, move):
    if move<=2:
        return random.randint(2,4)
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
    symbol = get_player_symbol(move)
    _, best_col = min_max(board, depth = 6, alpha = -float("inf"), beta = float("inf"), maximizing = True, symbol = symbol)

    for col in range(7):
        if board[0][col] == " ":
            tmp = copy.deepcopy(board)
            make_move(tmp, move, col)
            for opp_col in range(7):
                if tmp[0][opp_col] == " ":
                    tmp2 = copy.deepcopy(tmp)
                    make_move(tmp2, move + 1, opp_col)
                    if victory_checker(tmp2, move + 1):
                        if col == best_col:
                            valid = [c for c in range(7) if board[0][c] == " " and c != best_col]
                            if valid:
                                return random.choice(valid)
                        break

    return best_col

def play_again(next, root):
    global next_game
    next_game = next
    root.destroy()
    

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


def click_move(cell_size, board, move):
    mouse = pygame.mouse.get_pos()
    mouse_x = mouse[0] - 40
    column = mouse_x // (cell_size + 10)
    if column > (len(board)) or column < 0 or (board[0][column]) != " ":
        print("Invalid column ")
        return board, move
    else:
        board, move, victory = make_move(board, move, column)
        return board, move, victory, column

def play_again_window():
    root = tk.Tk()
    root.title("Play again")
    root.geometry("350x250")
    label = tk.Label(root, text="Do you want to play again", font=("Arial", 14))
    label.pack(pady=20)
    btn1 = tk.Button(root, text="Yes", width=10, command=lambda: play_again(True, root))
    btn1.pack(pady=5)
    btn2 = tk.Button(root, text="No", width=10, command=lambda: play_again(False, root))
    btn2.pack(pady=5)
    root.mainloop()


def game_mode_menu():
    root = tk.Tk()
    root.title("Choose game mode")
    root.geometry("350x250")
    label = tk.Label(root, text="Chose game mode:", font=("Arial", 14))
    label.pack(pady=20)

    btn1 = tk.Button(root, text="2 Players", width=10, command=lambda: set_mode("2p", root))
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Easy Bot", width=10, command=lambda: set_mode("easy", root))
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Medium Bot", width=10, command=lambda: set_mode("medium", root))
    btn3.pack(pady=5)

    btn4 = tk.Button(root, text="Hard Bot", width=10, command=lambda: set_mode("hard", root))
    btn4.pack(pady=5)
    root.mainloop()


def button_size(X, Y):
    button_ratio = [4,2]
    button_width = (X * 0.2) * button_ratio[0] / (button_ratio[0] + button_ratio[1])
    button_height = (Y * 0.2) * button_ratio[1] / (button_ratio[0] + button_ratio[1])
    return int(button_width), int(button_height)


def main_menu(X, Y, button_width, button_height , font):
    pygame.display.set_caption("Play")
    display_surface = pygame.display.set_mode((X, Y))
    music_playing = False
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play_rect.collidepoint(event.pos):
                    play_menu()
                    running = False
                if options_button.collidepoint(event.pos):
                    options_menu(music_playing, X, Y, button_width, button_height , font)

        display_surface.fill(gray)
        button_play_rect = draw_button(display_surface, X//2, Y//2 - button_height - 10, button_width, button_height, "Play", font, (34,34,34))
        options_button = draw_button(display_surface, X//2, Y//2, button_width, button_height, "Options", font, (34,34,34))
        but_3 = draw_button(display_surface, X//2, Y//2 + button_height + 10, button_width, button_height, "Exit", font, (34,34,34))
        
        pygame.display.flip()
    pygame.quit

def draw_button(surface, x, y, width, height, text, font, color):
    button_rect = pygame.Rect(0, 0, width, height)
    button_rect.center = (x, y)
    pygame.draw.rect(surface, color, button_rect)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    surface.blit(text_surface, text_rect)
    return button_rect


def play_menu():
    global move
    pygame.display.set_caption("Play")
    display_surface = pygame.display.set_mode((X, Y))
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_red.collidepoint(event.pos):
                    move = 0
                    running = False
                    game_mode_menu()
                    
                if button_blue.collidepoint(event.pos):
                    move = 1
                    running = False
                    game_mode_menu()
        display_surface.fill(gray)
        button_blue = draw_button(display_surface, X//2 + button_width + 10, Y//2 , button_width, button_height, "Blue", font, (34,34,34))
        button_red = draw_button(display_surface, X//2, Y//2, button_width, button_height, "Red", font, (34,34,34))
        pygame.display.flip()
    pygame.quit


def options_menu(music_playing, X, Y, button_width, button_height , font):
    pygame.display.set_caption("Options")
    display_surface = pygame.display.set_mode((X, Y))
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_music_rect.collidepoint(event.pos):
                    if music_playing == True:
                        pygame.mixer.music.pause()
                        music_playing = False
                    else:
                        pygame.mixer.music.unpause()
                        music_playing = True
                if back_button.collidepoint(event.pos):
                    running = False
                    main_menu(X, Y, button_width, button_height , font)

        display_surface.fill(gray)
        if music_playing == False:
            button_music_rect = draw_button(display_surface, X//2, Y//2 - button_height - 10, button_width, button_height, "Music", font, red)
        if music_playing == True:
            button_music_rect = draw_button(display_surface, X//2, Y//2 - button_height - 10, button_width, button_height, "Music", font, green)
        back_button = draw_button(display_surface, X//2, Y//2, button_width, button_height, "Back", font, (34,34,34))
        
        pygame.display.flip()
    pygame.quit
if __name__ == "__main__":
    import random
    import tkinter as tk
    import copy
    import pygame

    game_mode = None

    num_row = 6
    num_col = 7

    board = new_board(num_row)

    pause = False
    music_playing = True
    
    next_game = True
    
    
    white = (255, 255, 255)
    blue = (0, 0, 128)
    gray = (128, 128, 128)
    green = (0, 128, 0)
    red = (255,0,0)
    X, Y = 1280, 720

    pygame.init()
    pygame.mixer.init()


    pygame.display.set_caption("Play")
    pauza = pygame.image.load("Pauza.png")
    wyjscie = pygame.image.load("Exit.png")
    display_surface = pygame.display.set_mode((X, Y))
    font = pygame.font.Font('freesansbold.ttf', 18)

    wyjscie_rect = wyjscie.get_rect(center=(X//2 + 150, Y//2 + 60))
    wyjscie_clicked = False

    # dzwiek = pygame.image.load("Sound.png")
    # Nie_dzwiek = pygame.image.load("Not_sound.png")
    # dzwiek_rect = dzwiek.get_rect(center=(X//2 - 150, Y//2 + 60))
    pygame.mixer.music.load("muzyka.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    display_surface = pygame.display.set_mode((X, Y))
    font = pygame.font.Font('freesansbold.ttf', 18)
    button_width, button_height = button_size(X, Y)
    cell_size = calculate_cell_size(Y, num_row)
    grid_rect = grid_size(num_row, num_col, cell_size)

    blue_circle = pygame.image.load("blue_circle.png").convert_alpha()
    red_circle = pygame.image.load("red_circle.png").convert_alpha()

    player_symbol_1 = pygame.transform.smoothscale(blue_circle, (cell_size - 20, cell_size - 20))
    player_symbol_2 = pygame.transform.smoothscale(red_circle, (cell_size - 20, cell_size - 20))

    
    main_menu(X, Y, button_width, button_height, font)
    bot_id = (copy.deepcopy(move) + 1) % 2
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
            if event.type == pygame.MOUSEBUTTONDOWN and pause == False:
                if grid_rect.collidepoint(event.pos) and move % 2 != bot_id or game_mode == "2p":
                    board, move, victory, column = click_move(cell_size, board, move)
                    draw_grid(display_surface, cell_size, white, num_row, num_col, player_symbol_1, player_symbol_2, board)
                    if victory == True:
                        symbol = get_player_symbol(move)
                        print(board)
                        print(f'The player {symbol} won!!!')

                        display_surface.fill(gray)
                        draw_grid(display_surface, cell_size, white, num_row, num_col, player_symbol_1, player_symbol_2, board)
                        pygame.display.flip()

                        if next_game == True:
                            board = new_board(num_row)
                            move = 0
                        else:
                            running = False
                        play_again_window()
                    elif victory == False and move>41:
                        print("Draw")
                        play_again_window()
                        
                        if next_game == True:
                            board = new_board(num_row)
                            move = 0
                        else:
                            running = False
                            
            elif event.type == pygame.MOUSEBUTTONDOWN and pause == True:
                if wyjscie_rect.collidepoint(event.pos) and pause:  
                    wyjscie_clicked = True
                elif dzwiek_rect.collidepoint(event.pos) and pause: 
                    if music_playing:
                        pygame.mixer.music.pause()
                        music_playing = False
                    else:
                        pygame.mixer.music.unpause()
                        music_playing = True
                

        if game_mode != "2p":        
            if move % 2 == bot_id:
                if game_mode == "easy":
                    column = bot_easy(board, column, move)
                if game_mode == "medium":
                    column = medium_bot(board, move)
                if game_mode == "hard":
                    column = hard_bot(board, move)
                board, move, victory = make_move(board, move, column) 
                draw_grid(display_surface, cell_size, white, num_row, num_col, player_symbol_1, player_symbol_2, board)

                if victory == True:
                    symbol = get_player_symbol(move)
                    print(board)
                    print(f'The player {symbol} won!!!')
                
                    display_surface.fill(gray)
                    draw_grid(display_surface, cell_size, white, num_row, num_col, player_symbol_1, player_symbol_2, board)
                    pygame.display.flip()

                    play_again_window()
                    if next_game == True:
                        board = new_board(num_row)
                        move = 0
                    else:
                        running = False
                elif victory == False and move>41:
                        print("Draw")
                        play_again_window()
                        
                        if next_game == True:
                            board = new_board(num_row)
                            move = 0
                        else:
                            running = False
                

        display_surface.fill(gray)
        draw_grid(display_surface, cell_size, white, num_row, num_col, player_symbol_1, player_symbol_2, board)
        
        if pause == True:
            pauza_rect = pauza.get_rect(center=(X // 2, Y // 2))
            display_surface.blit(pauza, pauza_rect)
            display_surface.blit(wyjscie, wyjscie_rect)
            if music_playing:
                display_surface.blit(dzwiek, dzwiek_rect)
            else:
               display_surface.blit(Nie_dzwiek, dzwiek_rect)
               
            if wyjscie_clicked == True:
                running = False
            

        pygame.display.flip()
    pygame.quit()
