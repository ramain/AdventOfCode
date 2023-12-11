import numpy as np

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

def find_galaxy_pairs(galaxies):
    Ngal = galaxies.shape[0]

    corr_matrix = np.zeros((Ngal, Ngal), dtype=int)

    for i in range(Ngal):
        for j in range(i+1, Ngal):
            corr_matrix[i][j] = np.sum( np.abs(galaxies[i] - galaxies[j]) )
    
            print(galaxies[i], galaxies[j], corr_matrix[i][j])
    return corr_matrix
            

fname = "input.txt"
fname = "test.txt"
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

grid = expand_space(grid, empty_rows, empty_cols)

galaxies = np.where(grid == 1)
# reorder to np array
galarray = np.zeros((len(galaxies[0]), 2), dtype=int)
galarray[:,0] = galaxies[0]
galarray[:,1] = galaxies[1]

corr_matrix = find_galaxy_pairs(galarray)

print("sum of shortest paths:" , np.sum(corr_matrix))

#shortest_paths = np.min(corr_matrix, axis=0)
#print(shortest_paths, np.sum(shortest_paths))
