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

def find_galaxy_pairs(galaxies, voids):
    Ngal = galaxies.shape[0]
    corr_matrix = np.zeros((Ngal, Ngal), dtype=int)

    for i in range(Ngal):
        for j in range(i+1, Ngal):
            # tedious indexing to get right when j indeces < i indeces
            gali_x = galaxies[i][0]
            galj_x = galaxies[j][0]
            gali_y = galaxies[i][1]
            galj_y = galaxies[j][1]
            xslice = slice(min(gali_x, galj_x), max(gali_x, galj_x))
            yslice = slice(min(gali_y, galj_y), max(gali_y, galj_y))

            galpath = np.sum( np.abs(galaxies[i] - galaxies[j]) )
            Nvoidsx = np.sum(voids[xslice, galaxies[i][1]])
            Nvoidsy = np.sum(voids[galaxies[i][0], yslice])
            voidpath = Nvoidsx + Nvoidsy
            corr_matrix[i][j] = galpath + voidpath
    
    return corr_matrix
            

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

for i,voidfactor in enumerate([1, 1000000 - 1]):

    voids[empty_rows] = voidfactor
    voids[:, empty_cols] = voidfactor


    galaxies = np.where(grid == 1)
    # reorder to np array
    galarray = np.zeros((len(galaxies[0]), 2), dtype=int)
    galarray[:,0] = galaxies[0]
    galarray[:,1] = galaxies[1]

    corr_matrix = find_galaxy_pairs(galarray, voids)

    print(f"part {i+1} sum of shortest paths: {np.sum(corr_matrix)}")
    