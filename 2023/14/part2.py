import numpy as np

def sum_grid(grid):
    gridscore = np.copy(grid)
    gridscore[gridscore != 1] = 0
    gridscore = gridscore * np.arange(1,grid.shape[0]+1)[::-1,None]
    return gridscore.sum()

def tilt(grid):
    for j in range(grid.shape[1]):
        gridj = grid[:,j]
        cubes = np.where(gridj==0)[0]
        if len(cubes) >= 1:
            for k in range(len(cubes)+1):
                if k == 0:
                    idx_low = 0
                else:
                    idx_low = cubes[k-1]
                if k == len(cubes):
                    idx_high = len(gridj)
                else:
                    idx_high = cubes[k]
                block = gridj[idx_low:idx_high]
                block = np.sort(block)
                gridj[idx_low:idx_high] = block
        else:
            gridj = np.sort(gridj)
        grid[:,j] = gridj
    return grid

fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

grid = []
for line in infile:
    grid.append(list(line.strip()))

grid = np.array(grid)
print(grid)

#data = np.loadtxt(fname, dtype=str)
grid[grid=='#'] = 0
grid[grid=='.'] = 2
grid[grid=='O'] = 1

grid = grid.astype(int)
grid_orig = np.copy(grid)

grid_sifted = tilt(grid)
gridscore = grid_sifted
gridscore[gridscore != 1] = 0
gridscore = gridscore * np.arange(1,grid.shape[0]+1)[::-1,None]

print(gridscore)
print(gridscore.sum())


# Part 2
Niters = 1000000000
grids = np.zeros( (1000, grid.shape[0], grid.shape[1] ) )

grids[0] = grid_orig
grid = np.copy(grid_orig)
gridscores = []

# Search for a repetition of the cycle
# Final value will be at a multiple of cycles, with some burn-in time subtracted
for i in range(1,Niters):
    for j in range(4):
        grid = tilt(np.copy(grid))
        grid = np.rot90(grid, -1)

    g = np.sum(np.sum(np.abs(grids[:i] - grid), axis=-1), axis=-1)
    if np.any(g==0):
        i_start = np.where(g==0)[0][0]
        i_repeat = i - i_start
        print("repeat:", i_start, i_repeat)
        break
    grids[i] = grid

    gridscore = sum_grid(grid)
    gridscores.append(gridscore)


# Compute final version
i_final = (Niters-i_start) % i_repeat + i_start
print(gridscores[i_final-1])