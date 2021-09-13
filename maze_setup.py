import pygame
import random

pygame.init()

size = 5

screen = pygame.display.set_mode([size*60,size*60])
screen.fill((255,255,255))

maze = [[2, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 0, 1, 0, 3]]


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
        x = r * 60
        y = c * 60
        pygame.draw.rect(screen, color, pygame.Rect(y,x,60,60))
        pygame.display.flip()           

    


    

