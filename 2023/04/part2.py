import numpy as np

infile = 'test'
infile = 'input'

f = open(infile, 'r')

def match(winning, nums):
    N = 0
    for w in winning:
        for n in nums:
            if w == n:
                N += 1
    return N

i = 0
for line in f:
    i += 1
cards = np.ones(i)

f = open(infile, 'r')
for i,line in enumerate(f):
    j = i+1
    winning = []
    nums = []
    line = line.strip()
    line = line.split(':')[1]
    ws = line.split('|')[0].split(' ')
    for w in ws:
        if w.isdigit():
            winning.append(int(w))
    ns = line.split('|')[1].split(' ')
    for n in ns:
        if n.isdigit():
            nums.append(int(n))
    N = match(winning, nums)
    j_copies = slice(j, j+N)
    cards[j_copies] += cards[i]
    print(j, N, j_copies)
print(np.sum(cards))
