import numpy as np

#data = np.loadtxt('test', dtype=str)

f = open('input', 'r')
#f = open('test', 'r')
data = []
for line in f:
    line = line.strip()
    data.append(line)
data = np.array(data)


N = data.shape[0]
M = len(data[0])

nums_part = 0 

gear_nums = []
gear_ix = []
gear_iy = []

for i in range(N):
    di = data[i]
    if i == 0:
        d_low = "." * M
    else:
        d_low = data[i-1]
    if i == N-1:
        d_high = "." * M
    else:
        d_high = data[i+1]

    indeces = []
    for j,d in enumerate(di):
        if d.isdigit():
            indeces.append(j)

    nums = []
    border_idxs = []
    fudge = 0
    if len(indeces) > 0:
    
        idx0 = indeces[0]
        for k,idx in enumerate(indeces):
            numstr = ''
            if k > 0:
                if (int(idx) - int(indeces[k-1]) > 1):
                    idx1 = int(indeces[k-1])
                    s_num = di[idx0:idx1+1+fudge]
                    nums.append(int(s_num))
                    border = slice(max(idx0-1, 0), min(idx1+2+fudge, M))
                    border_idxs.append(border)
                    idx0 = idx
                if (k == len(indeces)-1):
                    s_num = di[idx0:idx+1]
                    nums.append(int(s_num))
                    border = slice(max(idx0-1, 0), min(idx+2, M))
                    border_idxs.append(border)
        

        lspl = di.split('.')

        for k,b in enumerate(border_idxs):
            str_high = d_high[b]
            str_low = d_low[b]
            str_med = di[b]
            str_line = str_low + str_med + str_high
            num = 0
            for ig,s in enumerate(str_line):
                if s == '*':
                    part_number = True
                    gear_index_x =  b.start + ig % len(str_low)
                    gear_index_y = i + ig // len(str_low) - 1
                    gear_num = int(nums[k])
                    gear_nums.append(gear_num)
                    gear_ix.append(gear_index_x)
                    gear_iy.append(gear_index_y)


gear_product_sum = 0

for i in range(len(gear_ix)):
    gear_product = 0
    gear_numi = gear_nums[i]
    ix = gear_ix[i]
    iy = gear_iy[i]

    for j in range(i+1, len(gear_ix)):
        jx = gear_ix[j]
        jy = gear_iy[j]
        if (ix == jx) and (iy == jy):
            print(ix, iy, gear_nums[i], gear_nums[j])
            gear_numj = gear_nums[j]
            if gear_product == 0:
                gear_product = gear_numi * gear_numj
                count = 2
            else:
                gear_product = 0
                #gear_product *= gear_numj


    gear_product_sum += gear_product

print(gear_product_sum)
