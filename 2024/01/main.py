import numpy as np

fname = "input.txt"
#fname = "test.txt"

data = np.loadtxt(fname, dtype=int)

list1 = data[:,0]
list2 = data[:,1]

list1 = np.sort(list1)
list2 = np.sort(list2)

## Part 1
dist = np.abs(list1 - list2)
distsum = np.sum(dist)
print("Part 1:", distsum)

## Part 2
score = 0
for i, x in enumerate(list1):
    i_intersect = np.argwhere(list2 == x)
    N = len(i_intersect)
    score += N * x
print("Part 2:", score)
