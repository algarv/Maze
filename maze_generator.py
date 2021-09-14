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

#Randomly choose a cell B and mark it as free.
B = [random.randint(0,size-1), random.randint(0,size-1)]
print(f"Cell B: {B}")
maze_list[B[0]][B[1]] = 2

for x in range(size):
    print(maze_list[x])

#Add that cell's neighbors to the wall list.
wall_list = [[B[0]+1, B[1]],
            [B[0], B[1]+1],
            [B[0]-1, B[1]],
            [B[0], B[1]-1]]


wall_list_size = [0, 1, 2, 3]

###Remove neighbors who are out of maze range
##print(f"Wall List: {wall_list}")
##for x in wall_list_size:
##    for y in range(2):
##        if wall_list[x][y] < 0 or wall_list[x][y] >= size:
##            wall_list.pop(x)
##            wall_list_size.pop()
##print(f"Adjusted Wall List: {wall_list}")

##suggestion##
for coordinates in wall_list:
    if coordinates[0] < 0 or coordinates[0]>size-1 or coordinates[1]<0 or coordinates[1]>size-1:
        wall_list.remove(coordinates)

for coordinates in wall_list:
    if coordinates[0] < 0 or coordinates[0]>size-1 or coordinates[1]<0 or coordinates[1]>size-1:
        wall_list.remove(coordinates)

print(f"Adjusted Wall List: {wall_list}")
##############


#While the wall list is not empty:
for x in range(size*3):

    #   Randomly choose a wall C from the wall list
    C = wall_list[random.randint(0,len(wall_list)-1)]
    print(f"Cell C: {C}")

    #   The wall divides two cells, A and B.

    if B[0] == C[0] and B[1] > C[1]:
        A = [B[0], C[1]-1]
    elif B[0] == C[0] and B[1] < C[1]:
        A = [B[0], C[1]+1]
    elif B[1] == C[1] and B[0] > C[0]:
        A = [C[0]-1, B[1]]
    elif B[1] == C[1] and B[0] < C[0]:
        A = [C[0]+1, B[1]]

    #trying to account for negative As
    if A[0] < 0 or A[0] > size-1 or A[1] < 0 or A[1] > size-1: 
        A = C

    print(f"Cell A: {A}")

    #   If either A or B is a wall
    #   Let D be whichever of A and B that is the wall
    if maze_list[A[0]][A[1]] == 1:
        D = A
    elif maze_list[B[0]][B[1]] == 1:
        D = B

    print(f"Cell D: {D}")

    #   Make C free
    maze_list[C[0]][C[1]] = 0

    #   Make D free
    maze_list[D[0]][D[1]] = 0

    for x in range(size):
        print(maze_list[x])

    #   Make D the new B
    B = D

    #   Add the walls of D to the wall list
    #wall_list_size = [0,1,2]
    wall_list = [[D[0]+1, D[1]],
                [D[0], D[1]+1],
                [D[0]-1, D[1]],
                [D[0], D[1]-1]]

    ##suggestion##
    for coordinates in wall_list:
        if coordinates[0] < 0 or coordinates[0]>size-1 or coordinates[1]<0 or coordinates[1]>size-1:
            wall_list.remove(coordinates)

    for coordinates in wall_list:
        if coordinates[0] < 0 or coordinates[0]>size-1 or coordinates[1]<0 or coordinates[1]>size-1:
            wall_list.remove(coordinates)

    for coordinates in wall_list:
        if coordinates == C:
            wall_list.remove(coordinates)
    
    print(f"Adjusted Wall List: {wall_list}")
    ##############

    #Remove C from the wall list
    #for x in wall_list_size:
    #    if wall_list[x][0] == C[0] and wall_list[x][1] == C[1]:
    #        wall_list.pop(x)

maze_list[C[0]][C[1]]=3
maze = maze_list
##maze = [[1, 3, 1, 0],
##        [1, 0, 1, 0],
##        [0, 0, 0, 0],
##        [0, 1, 1, 4]]


