import pygame
import random
import time
import numpy

from maze_generator import *

pygame.init()

##
##maze = [[3, 1, 0, 0, 0],
##        [0, 0, 0, 1, 0],
##        [0, 1, 1, 0, 0],
##        [1, 0, 0, 0, 1],
##        [0, 0, 1, 0, 4]]

print(maze)
size = numpy.size(maze,1)
walls = []
path = []

screen = pygame.display.set_mode([size*60,size*60])
screen.fill((255,255,255))       

for i in range(0,size):
    try: 
        y = maze[i].index(2)
        x = i
        break
    except:
        continue
    
print((x,y))
walls.append((x,y))

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
    pygame.draw.rect(screen,(0,0,255),pygame.Rect(y*60,x*60,60,60))
    pygame.display.flip()

    if maze[x][y] == 3:
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
            walls.append((x,y))
            x = a
            y = b
            continue
        elif x == size:
            walls.append((x,y))
            x = a
            y = b
            continue
        elif y < 0:
            walls.append((x,y))
            x = a
            y = b
            continue
        elif y == size:
            walls.append((x,y))
            x = a
            y = b
            continue
        elif maze[x][y] == 1:
            walls.append((x,y))
            x = a
            y = b
            continue
        elif ((x,y) in path) and (((a+1,b) in walls or (a+1,b) in path) and ((a-1,b) in walls or (a-1,b) in path) and ((a,b+1) in walls or (a,b+1) in path) and ((a,b-1) in walls or (a,b-1) in path)):
            walls.append((a,b))
            pygame.draw.rect(screen, [0,255,255], pygame.Rect(b*60,a*60,60,60))
            pygame.display.flip()
            break
        elif (x,y) in path:
            x = a
            y = b
            continue
        else:
            path.append((x,y))
            break
    print((x,y))
    time.sleep(.5)

