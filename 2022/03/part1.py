import numpy as np

def get_letter_value(letter):
    value = ord(letter)
    if value >= 97:
        value = value - 96
        return value
    elif value >= 65:
        value = value - 64 + 26
    return value

def find_overlap(s1, s2):
    s_overlap = []
    for s in s1:
        if s in s2:
            s_overlap.append(s)
    s_overlap = np.unique(s_overlap)
    if len(s_overlap) > 1:
        print(f"there should only be one overlapping letter, found {len(s_overlap)}")
    return s_overlap[0]

rucksacks = np.loadtxt('input', dtype=str)

letter_values = np.zeros(len(rucksacks)).astype('int')
for i,rucksack in enumerate(rucksacks):
    N = len(rucksack) // 2
    sack1 = rucksack[:N]
    sack2 = rucksack[N:]
    letter_common = find_overlap(sack1, sack2)
    letter_value = get_letter_value(letter_common)
    letter_values[i] = letter_value

value = np.sum(letter_values)
print(value)