def ascii_score(string):
    val = 0
    for s in string:
        val += ord(s)
        val *= 17
        val = val % 256

    return val

fname = "input.txt"
fname = "test.txt"
infile = open(fname, "r")
sequence = infile.read().strip()
sequence = sequence.split(",")

total_val = 0
for string in sequence:
    val = ascii_score(string)
    print(string, val)
    total_val += val

print(total_val)
#data = np.loadtxt(fname, dtype=str)
