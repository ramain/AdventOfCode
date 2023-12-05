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
    return s_overlap

rucksacks = np.loadtxt('input', dtype=str)
rucksack_groups = rucksacks.reshape(-1, 3)

letter_values = np.zeros(rucksack_groups.shape[0]).astype('int')
for i, rg in enumerate(rucksack_groups):
    sack1 = rg[0]
    sack2 = rg[1]
    sack3 = rg[2]
    letter_common_12 = find_overlap(sack1, sack2)
    letter_common = find_overlap(letter_common_12, sack3)
    letter_common = letter_common[0]

    letter_value = get_letter_value(letter_common)
    letter_values[i] = letter_value

value = np.sum(letter_values)
print(value)