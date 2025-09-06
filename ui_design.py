import pygame
pygame.init()
pygame.mixer.init()

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
            pygame.draw.rect(surface, color, cell)  # draw border only (1px) so we can see symbols
            # place symbol_1 centered in the cell
            if board[r][c] == "O":
                symbol_rect = symbol_1.get_rect(center=cell.center)
                surface.blit(symbol_1, symbol_rect)
            if board[r][c] == "X":
                symbol_rect = symbol_2.get_rect(center=cell.center)
                surface.blit(symbol_2, symbol_rect)
            pos_x += (cell_size + 10)
        pos_y += (cell_size + 10)

def grid_size(num_row, num_col):
    pos_y = 40
    for r in range(num_row):
        pos_x = 40
        for c in range(num_col):
            pos_x += (cell_size + 10)
    pos_y += (cell_size + 10)
    return pygame.Rect(40, 40, pos_x, pos_y)


def click_move(cell_size, num_row, num_col):
    mouse = pygame.mouse.get_pos()
    mouse_x = mouse[0]
    mouse_x = mouse_x - 40 - 10 * num_col
    column = mouse_x // cell_size
    



pause = False
music_playing = True
# player_symbol_1 = (255, 0, 0)
# player_symbol_2 = (0, 0, 255)


num_row = 6
num_col = 7
board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['O', ' ', ' ', ' ', ' ', ' ', ' '], ['O', ' ', ' ', ' ', ' ', ' ', ' '], ['O', 'X', 'X', ' ', 'X', ' ', ' '], ['O', 'O', 'X', 'X', 'O', ' ', ' ']]

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
grid_rect = grid_size(num_row, num_col)
# pygame.mixer.music.load("muzyka.mp3")
# pygame.mixer.music.set_volume(0.5)
# pygame.mixer.music.play(-1)

cell_size = calculate_cell_size(Y, num_row)
blue_circle = pygame.image.load("blue_circle.png").convert_alpha()
red_circle = pygame.image.load("red_circle.png").convert_alpha()
player_symbol_1 = pygame.transform.smoothscale(blue_circle, (cell_size - 20, cell_size - 20))
player_symbol_2 = pygame.transform.smoothscale(red_circle, (cell_size - 20, cell_size - 20))


clock = pygame.time.Clock()
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
            if grid_rect.collidepoint(event.pos):
                pygame.mouse.get_pos()


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
    # clock.tick(30)
pygame.quit()