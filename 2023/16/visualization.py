import os
import numpy as np
import matplotlib.pyplot as plt

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

def plot_grid(grid, illum, index, start=[0,0], markersize=6, color='cyan'):
    plt.figure(figsize=(5,5))
    plt.imshow(illum, cmap='afmhot', vmax=1.6, alpha=0.8)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] == '/':
                marker=(2, 0, -45)
                plt.plot(j, i, color=color, marker=marker, markersize=markersize)
            elif grid[i,j] == '\\':
                marker=(2, 0, 45)
                plt.plot(j, i, color=color, marker=marker, markersize=markersize)
            elif grid[i,j] == '-':
                plt.plot(j, i, '_', color=color, markersize=markersize)
            elif grid[i,j] == '|':
                plt.plot(j, i, '|', color=color, markersize=markersize)

    if (start[0] < 0) or (start[0] >= grid.shape[0]):
        marker = (2, 0, 90)
    else:
        marker = (2, 0, 0)
    plt.plot(start[0], start[1], marker=marker, color='orange', markersize=markersize)
    plt.axis('off')
    plt.xlim(-1, grid.shape[0]+1)
    plt.ylim(grid.shape[1]+1, -1)

    plt.savefig(f'plot_{index:03}.png')
    plt.close()

fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

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
    # as seen_states is a list, have to reset it to empty each time (learned the hard way..)
    illum = navigate_grid(grid.T, illum.T, i=0, j=l, direction=(1, 0), seen_states=[])
    if illum.sum() > total_illum:
        total_illum = illum.sum()
    plot_grid(grid, illum.T, grid.shape[0]-l, start=[-1,l])

    illum = np.zeros(grid.shape, dtype=int)
    illum = navigate_grid(grid.T, illum.T, i=grid.shape[0]-1, j=l, direction=(-1, 0), seen_states=[])
    if illum.sum() > total_illum:
        total_illum = illum.sum()
    plot_grid(grid, illum.T, l+2*grid.shape[0], start=[grid.shape[0],l])


for k in range(grid.shape[0]):
    illum = np.zeros(grid.shape, dtype=int)
    illum = navigate_grid(grid.T, illum, i=k, j=0, direction=(0, 1), seen_states=[])
    if illum.sum() > total_illum:
        total_illum = illum.sum()
    plot_grid(grid, illum.T, k+grid.shape[0], start=[k,-1])

    illum = np.zeros(grid.shape, dtype=int)
    illum = navigate_grid(grid.T, illum.T, i=k, j=grid.shape[1]-1, direction=(0, -1), seen_states=[])
    if illum.sum() > total_illum:
        total_illum = illum.sum()
    plot_grid(grid, illum.T, 4*grid.shape[0]-k, start=[k,grid.shape[1]])

os.system("convert -delay 8 -loop 1 plot*png illuminations.gif")
os.system("rm plot*png")