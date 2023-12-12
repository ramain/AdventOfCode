import numpy as np

fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

for line in infile:
    print(line)

#data = np.loadtxt(fname, dtype=str)
