def gravity(t, x, move):
    x = x-1
    if t[x][5] != " ":
        print("ten rzad jet pelny, wybierz inny")
        return t, move
    for i in reversed(range(5)):
        if t[x][i] != " " or i == 0:
            if move % 2 == 1:
                t[x][i] = "X"
            else:
                t[x][i] = "O"
            move += 1
            return t, move
