##This file generates a random block maze to be solved
import random

print('Welcome to the maze generator!')
size = int(input("Please enter maze size: "))

#All cells are walls.
maze_list = []
for x in range(size):
    inner_list = []
    for y in range(size):
        inner_list.append(1)
    maze_list.append(inner_list)

#for x in range(size):
#    print(maze_list[x])

#Randomly choose a cell B and mark it as free.
B = [random.randint(0,size-1), random.randint(0,size-1)]
print(f"Cell B: {B}")
maze_list[B[0]][B[1]] = 0

for x in range(size):
    print(maze_list[x])

#Add that cell's neighbors to the wall list.
wall_list = [[B[0]+1, B[1]],
            [B[0], B[1]+1],
            [B[0]-1, B[1]],
            [B[0], B[1]-1]]


#While the wall list is not empty:
#    Randomly choose a wall C from the wall list

#    The wall divides two cells, A and B.
#    If either A or B is a wall
#    Let D be whichever of A and B that is the wall
#    Make C free
#    Make D free
#    Add the walls of D to the wall list
#    Remove C from the wall list

maze = [[1, 3, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 4]]

