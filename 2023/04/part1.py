import numpy as np

f = open('input', 'r')
#f = open('test', 'r')

def match(winning, nums):
    N = 0
    for w in winning:
        for n in nums:
            if w == n:
                N += 1
    if N == 0:
        return 0
    return 2**(N-1)

num_total = 0
for line in f:
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
    num_total += N

print(num_total)