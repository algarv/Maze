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

while solution[x][y] != 3:
    x = x + 1 
    if maze[x][y] == 0:
        solution[x][y] = 0
        break
    elif maze[x][y] == 1:
        solution[x][y] = 1
        break

    if solution[x][y] == 0:
        x = x + 1
        

