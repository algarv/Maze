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

start = B

for x in range(size):
    print(maze_list[x])

#Add that cell's neighbors to the wall list.
    
wall_list = []

for coordinates in [[B[0]+1, B[1]],[B[0], B[1]+1],[B[0]-1, B[1]],[B[0], B[1]-1]]:
    if coordinates[0] < 0 or coordinates[0] >= size or coordinates[1] <0 or coordinates[1] >= size:
        continue
    else:
        wall_list.append(coordinates)

print(f"Wall List: {wall_list}")


#While the wall list is not empty:
while len(wall_list)>1:
    
#for x in range(size*3):
    print(B)
    #   Randomly choose a wall C from the wall list
    C = random.choice(wall_list)
    print(f"Cell C: {C}")

    while True:
        if C[0] == 0 or C[1] == 0 or C[0] == size-1 or C[1] == size-1: #C on edge of maze (could be trouble)
            if B[0] == 0 or B[1] == 0 or B[0] == size-1 or B[1] == size-1: #B on edge of maze (this is okay)
                if (C[0]==0 and C[1]==0) or (C[0] == 0 and C[1] == size-1) or (C[0]==size-1 and C[1]==0) or (C[0]==size-1 and C[1]==size-1):
                    print('Corner!')
                    while C in wall_list: 
                        for coordinates in wall_list:
                            if coordinates == C:
                                wall_list.remove(coordinates) 
                    C = random.choice(wall_list)
                else:
                    break
            else: #C on edge of maze, but B is not (means A will be off maze!!!)
                while C in wall_list: 
                    for coordinates in wall_list:
                        if coordinates == C:
                            wall_list.remove(coordinates) 
                C = random.choice(wall_list)
        else:
            break
        print(f"Try Again Cell C: {C}")

    #The wall divides two cells, A and B.

    if B[0] == C[0] and B[1] > C[1]:
        A = [B[0], C[1]-1]
    elif B[0] == C[0] and B[1] < C[1]:
        A = [B[0], C[1]+1]
    elif B[1] == C[1] and B[0] > C[0]:
        A = [C[0]-1, B[1]]
    elif B[1] == C[1] and B[0] < C[0]:
        A = [C[0]+1, B[1]]

    #trying to account for negative As
    #if A[0] < 0 or A[0] > size-1 or A[1] < 0 or A[1] > size-1: 
    #    A = C

    print(f"Cell A: {A}")

    #   If either A or B is a wall
    #   Let D be whichever of A and B that is the wall
##    if maze_list[A[0]][A[1]] == 1:
##        D = A
##    elif maze_list[B[0]][B[1]] == 1:
##        D = B
##    else:
##        break

    #print(f"Cell D: {D}")

    #   Make C free
    maze_list[C[0]][C[1]] = 0

    #   Make D free
    maze_list[A[0]][A[1]] = 0

    for x in range(size):
        print(maze_list[x])

    #   Make A the new B
    B = A

    for coordinates in [[B[0]+1, B[1]],[B[0], B[1]+1],[B[0]-1, B[1]],[B[0], B[1]-1]]:
        if coordinates in wall_list:
            continue
        elif coordinates[0] < 0 or coordinates[0] >= size or coordinates[1] <0 or coordinates[1] >= size:
            continue
        else:
            wall_list.append(coordinates)


    while C in wall_list: 
        for coordinates in wall_list:
            if coordinates == C:
                wall_list.remove(coordinates) 
    
    print(f"Adjusted Wall List: {wall_list}")


maze_list[A[0]][A[1]]=3
maze_list[start[0]][start[1]]=2
maze = maze_list

print(f"End of Loop wall_list: {wall_list}")

print("Maze Generated!")


