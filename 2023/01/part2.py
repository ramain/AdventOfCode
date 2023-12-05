import numpy as np

f = open("input", "r")

digits = np.arange(1,10)
numstrings = ['one','two','three','four','five','six','seven','eight','nine']

cal = 0
for line in f:
    indeces = []
    numbers = []
    for dig in digits:
        idx = line.find(str(dig))
        idx2 = line.rfind(str(dig))
        if idx >= 0:
            indeces.append(idx)
            numbers.append(dig)
        if idx != idx2 and idx2 >= 0:
            indeces.append(idx2)
            numbers.append(dig)   
    for j,numstring in enumerate(numstrings):
        idx = line.find(numstring)
        idx2 = line.rfind(numstring)
        if idx >= 0:
            indeces.append(idx)
            numbers.append(digits[j])  
        if idx != idx2 and idx2 >= 0:
            indeces.append(idx2)
            numbers.append(digits[j])          

    numbers = np.array(numbers)
    indeces = np.array(indeces)
    n = numbers[np.argsort(indeces)].astype('str')

    if len(n) >= 2:
        n = n[0] + n[-1]
    if len(n) == 1:
        n = n[0] + n[0]

    n = int(n)
    print(line, n)

    cal += n
print(cal)
