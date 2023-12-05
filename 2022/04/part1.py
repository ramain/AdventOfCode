import numpy as np

f = open("input", "r")
count_contained = 0
count_overlap = 0
for line in f:
    line=line.split(',')
    elf1 = line[0].split('-')
    sec1 = np.arange(int(elf1[0]), int(elf1[1])+1)

    elf2 = line[1].split('-')
    sec2 = np.arange(int(elf2[0]), int(elf2[1])+1)

    if np.in1d(sec1, sec2).all() or np.in1d(sec2, sec1).all():
        count_contained += 1

    if np.in1d(sec1, sec2).any():
        count_overlap += 1

print(count_contained)
print(count_overlap)