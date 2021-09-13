from maze1 import maze
import random

solution = [[2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3]]

start = maze[0][0]
finish = maze[4][4]
x = 0
y = 0
size = 5

while solution[x][y] != 3:
    i = random.choice(("x", "y"))
    print(i) # for debugging

    if i == "x":
        x = x + random.choice((-1,1))
        print(x) # for debugging
        if x <= 0:
            x = 0
            solution[x][y] = 0
        elif x >= size:
            x = x - 1
        elif x == 1:
            solution[x][y] = 1
        
    if i == "y":
        y = y + random.choice((-1,1))
        print(y)  # for debugging
        if y < 0:
            y = 0
            solution[x][y] = 0
        elif y >= size:
            y = y - 1
        elif y == 1:
            solution[x][y] = 1
