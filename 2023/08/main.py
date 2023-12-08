import numpy as np

f = open('input', 'r')
#f = open('test', 'r')

startkeys = []
mapping = {}
for i,line in enumerate(f):
    if i == 0:
        LRinstructions = line.strip()
    elif i >= 2:            
        #line = line.split("=")
        key = line[0:3]
        if i == 2:
            key0 = key
        L = line[7:10]
        R = line[12:15]
        mapping[key]=(L, R)
        if key[-1] == 'A':
            startkeys.append(key)
        
key = key0
nLR = len(LRinstructions)
LRinstructions = LRinstructions*10000

outputk = []
output = []

key = 'AAA'
for i in range(len(LRinstructions)):

    ins = LRinstructions[i]
    outputk.append(key)
    output.append(ins)
    if ins == "L":
        key = mapping[key][0]
    elif ins == "R":
        key = mapping[key][1]
    else:
        print("ERROR")
        break

    if key == 'ZZZ':
        print("Part1: ZZZ", i+1)
        break

# part 2
steps = []
for key_i in startkeys:
    key = key_i

    for i in range(len(LRinstructions)):

        ins = LRinstructions[i]
        outputk.append(key)
        output.append(ins)
        if ins == "L":
            key = mapping[key][0]
        elif ins == "R":
            key = mapping[key][1]
        else:
            print("ERROR")
            break

        if key[-1] == 'Z':
            print(key_i, key, i+1)
            steps.append(i+1)
            break

steps = np.array(steps)
lcm = np.lcm.reduce(steps)

print("Part2 :", lcm)