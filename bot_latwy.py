import random
def bot_latwy(move, x):
    if move < 6:
        y = random.randint(3, 5)
    elif move > 6 and move<10:
        y = random.randint(2, 6)
    else:
        z = random.randit(0, 100)
        if z%5 == 0:
            y = random.randint(1, 7)
        elif z%5 == 1 or z%5 == 2:
            y = x
        else:
            y = x + random.choice(-1, 1)
    return y
            
