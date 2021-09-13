import pygame
import random
import time
import numpy

from maze_generator import *

pygame.init()


##maze = [[2, 1, 0, 0, 0],
##        [0, 0, 0, 1, 0],
##        [0, 1, 1, 0, 0],
##        [1, 0, 0, 0, 1],
##        [0, 0, 1, 0, 3]]

print(maze)
size = numpy.size(maze,1)
walls = []

screen = pygame.display.set_mode([size*60,size*60])
screen.fill((255,255,255))       

for i in range(0,size):
    try: 
        y = maze[i].index(3)
        x = i
        break
    except:
        continue
    
print((x,y))

while True:
    for r in range(0,size):
        for c in range(0,size):
            if maze[r][c] == 0:
                color = (255,255,255)
            elif maze[r][c] == 1:
                color = (0,0,0)
            elif maze[r][c] == 3:
                color = (0,255,0)
            elif maze[r][c] == 4:
                color = (255,0,0)
            pygame.draw.rect(screen, color, pygame.Rect(c*60,r*60,60,60))
            pygame.display.flip()
    pygame.draw.rect(screen,(0,0,255),pygame.Rect(y*60,x*60,60,60))
    pygame.display.flip()

    if maze[x][y] == 4:
        break

    a = x
    b = y
    while True:
        i = random.choice(['x','y'])
        if i == 'x':
            z = random.choice((-1,1))
            x = x + z
        if i == 'y':
            z = random.choice((-1,1))
            y = y + z
        if (x,y) in walls:
            x = a
            y = b
            continue
        elif x < 0:
            x = a
            continue
        elif x == size:
            x = a
            continue
        elif y < 0:
            y = b
            continue
        elif y == size:
            y = b
            continue
        elif maze[x][y] == 1:
            walls.append((x,y))
            x = a
            y = b
        else:
            break

    time.sleep(.5)

