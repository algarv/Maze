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
    i = random.choice("x", "y'")
    if i == "x":
        x = x + random.choice((-1,1))
    if i == "y":
        y = y + random.choice((-1,1))

    if x < 0:
        x = 0
    if x == size:
        x = x - 1

    if y < 0:
        y = 0
    if y == size:
        y = x - 1

    if maze[x][y] == 3:
        break