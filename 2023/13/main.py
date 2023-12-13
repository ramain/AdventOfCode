import numpy as np

fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

def find_symmetry(parray, horizontal=True, match=0):
    N = parray.shape[0]
    for i in range(1,parray.shape[0]):
        len = min(i, N-i)
        i_start = max(0, i-len)
        i_end = min(N, i+len)

        parray_main = parray[i_start:i]
        parray_reflect = parray[i:i_end][::-1]
        if np.sum(np.abs(parray_main - parray_reflect)) == match:
            print(i, horizontal)
            if horizontal:
                return(100*i)
            else:
                return i
    return 0

patterns = []
pattern = []
for line in infile:
    if len(line.strip()) == 0:
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(list(line.strip()))

patterns.append(pattern)
data = np.loadtxt(fname, dtype=str)

count = 0
count_smudge = 0
for pattern in patterns:
    parray = np.array(pattern)

    parray[parray=='#'] = '1'
    parray[parray=='.'] = '0'
    parray = parray.astype(int)

    h = find_symmetry(parray, horizontal=True)
    v = find_symmetry(parray.T, horizontal=False)
    count += h
    count += v

    h = find_symmetry(parray, horizontal=True, match=1)
    v = find_symmetry(parray.T, horizontal=False, match=1)
    count_smudge += h
    count_smudge += v

    if h+v == 0:
        print(parray)

print(count)
print(count_smudge)