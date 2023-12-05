import numpy as np

f = open('input', 'r')
data = f.read()
cals = data.split('\n')

elf_index = 0
elf_cals = 0
cal_sums = []

for cal in cals:
    try:
        cal = float(cal)
        elf_cals+=cal
    except:
        cal_sums.append(elf_cals)
        elf_index += 1
        elf_cals = 0
        
cal_sums = np.array(cal_sums)
cal_sums_sorted = np.sort(cal_sums)[::-1]
print(f"The Elf with the most food has {cal_sums_sorted[0]} calories" )

print(f"The three Elves with the most food have {cal_sums_sorted[:3].sum()} calories" )
