import numpy as np
from functools import cache

# Needed completely different strategy, part1 brute force blew up my computer

@cache    
def recursive_springcombo(conditions, numtuple):
    # Learning recursion, ouch my brain
    # Followed tutorial, explains recursive structure, and importance of cache 
    # https://realpython.com/python-thinking-recursively/
    
    
    # Base cases: Once there are no more numbers, check if any more # exist
    # If there are damaged springs (#), then the combination is invalid
    # The converse is true, if no "#" remain, then the combination is valid
    
    #print(conditions, numtuple)
    if not numtuple:
        if '#' in conditions:
            return 0
        else:
            return 1
    
    # Once there are no more '.#?' characters, check if more numbers exist
    if not conditions:
        if numtuple:
            return 0
        else:
            return 1
    
    # For '.', peel off and run recursive_func
    # For #, see if current num fits in the block.
    # If it hits the end of the current block, move past current # block in 
    # string (num steps forward) and to next grouping number (numtuple[1]).
    # For ?, run both
    Ncomb = 0
    if conditions[0] in '.?':
        Ncomb += recursive_springcombo(conditions[1:], numtuple)
    
    if conditions[0] in '#?':
        num = numtuple[0]
        len_c = len(conditions)
        
        if num <= len_c and "." not in conditions[:num]: 
            if (num == len_c or conditions[num] != "#"):
                Ncomb += recursive_springcombo(conditions[num+1:], numtuple[1:])
                 
    return Ncomb


fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

cogs = []
nums = []
Nextend = 5

for line in infile:
    line = line.split()
    linestr = line[0]
    for i in range(Nextend-1):
        linestr += '?'
        linestr += line[0]
    cogs.append(linestr)
    nums_line = line[1].split(",")
    numsi = []
    for num in nums_line:
        numsi.append(int(num))
    nums.append(numsi*Nextend)


total = 0
for (cog, num) in zip(cogs, nums):
    total += recursive_springcombo(cog, tuple(num))
    
print(total)
