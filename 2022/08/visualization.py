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

data = np.loadtxt(fname, dtype=str)
treegrid = np.zeros((len(data), len(data[0])), dtype=int)
for i in range(len(data)):
    for j in range(len(data[0])):
        treegrid[i][j] = int(data[i][j])

visible_trees = find_visible_trees(treegrid)
print(visible_trees)

VisibleImage = treegrid * visible_trees
plt.figure(figsize=(10.5, 5))
plt.subplot(1,2,1)
plt.title("Forest tree heights")
plt.imshow(treegrid, cmap='Greens')
plt.xticks([])
plt.yticks([])

plt.subplot(1,2,2)
plt.title("Trees Visible from outside")
plt.imshow(VisibleImage, cmap='Greens')
plt.xticks([])
plt.yticks([])
plt.show()