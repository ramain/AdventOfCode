import numpy as np

fname = "input.txt"
#fname = "test.txt"

data = []
infile = open(fname, 'r')
for line in infile:
    data.append(list(line.strip()))
data = np.array(data)
# data is NxN array of letters, need to find all XMAS forwards, backwards, and diagonals

def count_line(line):
    line = ''.join(line)
    Ni = line.count('XMAS')
    print(line, Ni)
    return Ni

def count_wordarray(wordarray, xmascount):
    for i in range(wordarray.shape[0]):
        Ni = count_line(wordarray[i])
        xmascount += Ni
    return xmascount

def count_xmas(wordarray):

    xmascount = 0
    for j in range(4):
        xmascount = count_wordarray(wordarray, xmascount)
        print("ROTATION", j, xmascount)
        wordarray = np.rot90(wordarray)

    print(xmascount)

    print("DIAGONALS")
    for j in range(4):
        for k in range(0, wordarray.shape[0]-3):
            if k == 0:
                line = wordarray.diagonal()
                Ni = count_line(line)
            else:
                line = np.roll(wordarray, -k, axis=1).diagonal()[:-k]
                Ni = count_line(line) + count_line(line[::-1])
            xmascount += Ni
        wordarray = np.rot90(wordarray)
    print(xmascount)

    return xmascount
    
print(data.shape)
xmascount = count_xmas(data)
if xmascount < 2396:
    print("Error: xmascount is too low")
print(xmascount)