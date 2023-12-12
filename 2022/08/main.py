import numpy as np
import matplotlib.pyplot as plt

fname = "input.txt"
#fname = "test.txt"

def rotate(grid, n=1):
    return np.rot90(grid, n)

def find_visible_trees(treegrid):
    # edges are visible
    visible_trees = np.zeros_like(treegrid)
    for i in range(4):
        visible_trees[0] = 1
        visible_trees = rotate(visible_trees)

    for i in range(4):
        treegrid = rotate(treegrid)
        visible_trees = rotate(visible_trees)
        for i in range(treegrid.shape[0]):
            for j in range(1, treegrid.shape[1]-1):
                if treegrid[i,j] > np.max(treegrid[i, :j]):
                    visible_trees[i,j] = 1
    return visible_trees

def find_scenic_score(treegrid, i, j):
    # Look along 4 directions, stop when hitting a tree as tall
    # or taller than the current tree
    Lslice = treegrid[i, :j][::-1]
    Rslice = treegrid[i, j+1:]
    Uslice = treegrid[:i, j][::-1]
    Dslice = treegrid[i+1:, j]
    Ns = []
    s0 = treegrid[i,j]
    for s in [Lslice, Rslice, Uslice, Dslice]:
        N = 1
        if len(s) > 1:
            for k in range(len(s)):
                if s[k] < s0:
                    N += 1
                else:
                    break
        N = np.min([N, len(s)])
        Ns.append(N)
    scenic_score = Ns[0]*Ns[1]*Ns[2]*Ns[3]
    return scenic_score
    

data = np.loadtxt(fname, dtype=str)
treegrid = np.zeros((len(data), len(data[0])), dtype=int)
for i in range(len(data)):
    for j in range(len(data[0])):
        treegrid[i][j] = int(data[i][j])

visible_trees = find_visible_trees(treegrid)
print(visible_trees)
print(np.sum(visible_trees))

# Loop through and find scenic score for each tree
score_best = 0
for i in range(1,treegrid.shape[0]-1):
    for j in range(1,treegrid.shape[1]-1):
        score = find_scenic_score(treegrid, i, j)
        if score > score_best:
            score_best = score
print(score_best)
