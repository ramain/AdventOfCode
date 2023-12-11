import numpy as np
import matplotlib.pyplot as plt
import os

def expand_space(grid, empty_rows, empty_cols):
    N = grid.shape[0] + len(empty_rows)
    M = grid.shape[1] + len(empty_cols)

    # expand in rows, then in columns
    grid_xexpanded = np.zeros((N, grid.shape[1]), dtype=int)

    j = 0
    for i in range(grid.shape[0]):
        if i in empty_rows:
            j += 1
        grid_xexpanded[j] = grid[i]
        j += 1

    # expand in columns
    grid_xyexpanded = np.zeros((N, M), dtype=int)
    j = 0
    for i in range(grid.shape[1]):
        if i in empty_cols:
            j += 1
        grid_xyexpanded[:, j] = grid_xexpanded[:, i]
        j += 1

    return grid_xyexpanded

def find_expanded_galaxies(galaxies, voids):
    Ngal = galaxies.shape[0]
    galaxies_expanded = np.zeros_like(galaxies)

    for i in range(Ngal):
            # tedious indexing to get right when j indeces < i indeces
            gali_x = galaxies[i][0]
            gali_y = galaxies[i][1]

            Nvoidsx = np.sum(voids[:gali_x, galaxies[i][1]])
            Nvoidsy = np.sum(voids[galaxies[i][0], :gali_y])
            galaxies_expanded[i][0] = gali_x + Nvoidsx
            galaxies_expanded[i][1] = gali_y + Nvoidsy
    
    return galaxies_expanded
            

fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

data = np.loadtxt(fname, dtype=str, comments='//')

grid = np.zeros((len(data), len(data[0])), dtype=int)

for i in range(len(data)):
    for j in range(len(data[0])):
        x = data[i][j]
        if x == '#':
            grid[i][j] = 1

empty_rows = np.argwhere(np.sum(grid, axis=1) == 0)
empty_cols = np.argwhere(np.sum(grid, axis=0) == 0)

# -1 to definition to match test case
# get part 1 for free, setting to 1


voids = np.zeros_like(grid)
expansion = np.linspace(0, 6, 100, endpoint=True, dtype=float)
void_factors = 10**expansion

for i,voidfactor in enumerate(void_factors):

    voids[empty_rows] = voidfactor
    voids[:, empty_cols] = voidfactor


    galaxies = np.where(grid == 1)
    # reorder to np array
    galarray = np.zeros((len(galaxies[0]), 2), dtype=int)
    galarray[:,0] = galaxies[0]
    galarray[:,1] = galaxies[1]

    galaxies_expanded = find_expanded_galaxies(galarray, voids)
    plt.figure(figsize=(5,5))
    plt.scatter(galaxies_expanded[:,0], galaxies_expanded[:,1], marker='.', s=1, c='k')
    plt.xticks([])
    plt.yticks([])
    plt.savefig(f"plot_{i:02}.png")
    plt.close()

os.system("convert -delay 5 -loop 0 -duplicate 1,-2-1 plot*png expansion.gif")
os.system("rm plot*png")