import numpy as np
import itertools

fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

def find_idx(str, ch):
    return [i for i, c in enumerate(str) if c == ch]

def split_and_count(cogline):
    cogsplit = cogline.split('.')
    cogcount = []
    for cog in cogsplit:
        if len(cog) >= 1:
            cogcount.append(len(cog))
    return cogcount

def count_arrangements(cogline, num):
    Narr = 0
    i_unknown = find_idx(cogline, '?')
    combinations = list(itertools.product(['.', '#'], repeat=len(i_unknown)))
    for c in combinations:
        cogline = list(cogline)
        for i in range(len(i_unknown)):
            cogline[i_unknown[i]] = str(c[i])
        cogline = ''.join(cogline)
        cogcount = split_and_count(cogline)
        if cogcount == num:
            Narr += 1
    return Narr


    

cogs = []
nums = []

for line in infile:
    line = line.split()
    cogs.append(line[0])
    nums_line = line[1].split(",")
    numsi = []
    for num in nums_line:
        numsi.append(int(num))
    nums.append(numsi)

print(cogs)
print(nums)

Narr_total = 0
for i in range(len(cogs)):
    Narr = count_arrangements(cogs[i], nums[i])
    #print(Narr)
    Narr_total += Narr
print(Narr_total)