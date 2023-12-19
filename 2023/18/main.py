import numpy as np
import matplotlib.pyplot as plt

def step_forward(trench, i, j, direction, steps):
    if direction == "R":
        dir = (1, 0)
    elif direction == "L":
        dir = (-1, 0)
    elif direction == "U":
        dir = (0, -1)
    elif direction == "D":
        dir = (0, 1)

    for k in range(steps):
        i += dir[0]
        j += dir[1]
        trench[i, j] = 1
    return trench, i, j


fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

directions = []
steps = []
colours = []
for line in infile:
    line = line.strip().split()
    directions.append(line[0])
    steps.append(int(line[1]))
    colours.append(line[2][1:-1])

print(directions)
print(steps)
print(colours)


N = 1000
i = N//2
j = N//2
trench = np.zeros((N,N), dtype=int)
trench[i, j] = 1

for k in range(len(directions)):
    print(directions[k], steps[k])
    trench, i, j = step_forward(trench, i, j, directions[k], steps[k])


plt.imshow(trench)
plt.show()

# trying with floodfill again - always works in test but not input..
from skimage.measure import label
labels = label(trench, connectivity=1, background=1)

# flood fill put bg as 1, fill as 2, trench as 0.  Simply sum the non-1 values
print(len(np.argwhere(labels!=1)) )

plt.imshow(labels)
plt.colorbar()
plt.show()