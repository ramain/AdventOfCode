import numpy as numpy

fname = "input.txt"
infile = open(fname, "r")

for line in infile:
    print(line)

#data = np.loadtxt(fname, dtype=str)
