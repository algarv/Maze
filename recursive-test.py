from maze1 import maze
import random

x = 0
y = 0
size = 5
solution = [[0] * size for i in range(size)]

while True:
    i = random.choice(("x", "y"))
    print(i) # for debugging

    if i == "x":
        z = random.choice((-1,1))
        x = x + z
        print(x) # for debugging
        if x < 0:
            x = x - z
            continue
        elif x > size - 1:
            x = x - z
            continue
        if maze[y][x] == 0:
            solution[y][x] = 0
        elif maze[y][x] == 1:
            solution[y][x] = 1
            x = x - z
        print(solution)  # for debugging
        print(x)

        
    if i == "y":
        z = random.choice((-1,1))
        y = y + z
        print(y)  # for debugging
        if y < 0:
            y = y - z
            continue
        elif y > size - 1:
            y = y - z
            continue
        if maze[y][x] == 0:
            solution[y][x] = 0
        elif maze[y][x] == 1:
            solution[y][x] = 1
            y = y - z         
        print(solution)  # for debugging
        print(y)

    # if solution[size][size] == 3:
       # break
