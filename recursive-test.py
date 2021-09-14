from maze1 import maze
import random
import pygame
import time

pygame.init()

x = 0
y = 0
size = 5
solution = [[0] * size for j in range(size)]

screen = pygame.display.set_mode([size*60,size*60])
screen.fill((255,255,255))  

while True:
    for r in range(0,size):
        for c in range(0,size):
            if maze[r][c] == 0:
                color = (255,255,255)
            elif maze[r][c] == 1:
                color = (0,0,0)
            elif maze[r][c] == 2:
                color = (0,255,0)
            elif maze[r][c] == 3:
                color = (255,0,0)
            pygame.draw.rect(screen, color, pygame.Rect(c*60,r*60,60,60))
            pygame.display.flip()
    pygame.draw.rect(screen,(0,0,255),pygame.Rect(x*60,y*60,60,60))
    pygame.display.flip()

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
            solution[y][x] = maze[y][x]
        elif maze[y][x] == 1:
            solution[y][x] = maze[y][x]
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
            solution[y][x] = maze[y][x]
        elif maze[y][x] == 1:
            solution[y][x] = maze[y][x]
            y = y - z         
        print(solution)  # for debugging
        print(y)

    if maze[y][x] == 3:
            solution[y][x] = maze[y][x]
            print(solution)
            break

    time.sleep(.5)

