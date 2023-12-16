import numpy as np
from functools import cache

fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

def navigate_grid(grid, illum, i=0, j=0, direction=(1, 0), seen_states=[]):
    while (0 <= i < grid.shape[0]) and (0 <= j < grid.shape[0]):
        # prevent it from getting stuck in a loop, keeps recursion depth low enough
        if (i,j,direction) in seen_states:
            break
        seen_states.append((i, j, direction))

        illum[i,j] = 1
        # flip direction of / and \, since j=0 is *top* of grid
        if grid[i,j] == '/':
            direction = (-direction[1], -direction[0])
        elif grid[i,j] == '\\':
            direction = (direction[1], direction[0])
        elif grid[i,j] == '-':
            if direction[0] == 0:
                illum = navigate_grid(grid, illum, i, j, direction=(1, 0), seen_states=seen_states)
                direction = (-1, 0)
        elif grid[i,j] == '|':
            if direction[1] == 0:
                illum = navigate_grid(grid, illum, i, j, direction=(0, 1), seen_states=seen_states)
                direction = (0, -1)
        i += direction[0]
        j += direction[1]

    return illum    
    
grid = []
for line in infile:
    grid.append(list(line.strip()))

grid = np.array(grid)
illum = np.zeros(grid.shape, dtype=int)
# transposes because I had x and y flipped in my brain
illum = navigate_grid(grid.T, illum.T, i=0, j=0, direction=(1, 0))

print("Part1 :", illum.sum())

# Part 2
# illuminate the grid from each direction
# Quick enough to brute force

total_illum = 0
for l in range(grid.shape[1]):
    illum = np.zeros(grid.shape, dtype=int)
    illum = navigate_grid(grid.T, illum.T, i=0, j=l, direction=(1, 0), seen_states=[])
    if illum.sum() > total_illum:
        total_illum = illum.sum()

    illum = np.zeros(grid.shape, dtype=int)
    illum = navigate_grid(grid.T, illum.T, i=grid.shape[0]-1, j=l, direction=(-1, 0), seen_states=[])
    if illum.sum() > total_illum:
        total_illum = illum.sum()
        print(l, total_illum)


for k in range(grid.shape[0]):
    illum = np.zeros(grid.shape, dtype=int)
    illum = navigate_grid(grid.T, illum, i=k, j=0, direction=(0, 1), seen_states=[])
    if illum.sum() > total_illum:
        total_illum = illum.sum()

    illum = np.zeros(grid.shape, dtype=int)
    illum = navigate_grid(grid.T, illum.T, i=k, j=grid.shape[1]-1, direction=(1, 0), seen_states=[])
    if illum.sum() > total_illum:
        total_illum = illum.sum()
        print(k, total_illum)

print("Part2 :", total_illum)
