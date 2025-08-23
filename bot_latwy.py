import random
def bot_easy(move, last_column):
    if move < 6:
        column = random.randint(3, 5)
    elif move > 6 and move < 10:
        column = random.randint(2, 6)
    else:
        z = random.randit(0, 100)
        if z % 5 == 0:
            column = random.randint(1, 7)
        elif z % 5 == 1 or z % 5 == 2:
            column = last_column
        else:
            column = last_column + random.choice(-1, 1)
    return column
            
