import numpy as np

fname = "input.txt"
#fname = "test.txt"

def check_xmas(cross):
    for i in range(4):
        if ''.join(cross) == 'MMSS':
            return 1
        cross = np.roll(cross, 1)
    return 0

data = []
infile = open(fname, 'r')
for line in infile:
    data.append(list(line.strip()))
data = np.array(data)
# data is NxN array of letters, need to find all XMAS forwards, backwards, and diagonals

ix, iy = np.where(data == 'A')

bad = np.argwhere(ix == 0)
ix = np.delete(ix, bad)
iy = np.delete(iy, bad)
bad = np.argwhere(ix == data.shape[0]-1)
ix = np.delete(ix, bad)
iy = np.delete(iy, bad)
bad = np.argwhere(iy == 0)
ix = np.delete(ix, bad)
iy = np.delete(iy, bad)
bad = np.argwhere(iy == data.shape[1]-1)
ix = np.delete(ix, bad)
iy = np.delete(iy, bad)

count = 0
for i in range(len(ix)):
    j = ix[i]
    k = iy[i]
    cross = np.array([data[j-1, k-1], data[j-1, k+1], data[j+1, k+1], data[j+1, k-1]])
    count += check_xmas(cross)

print(count)