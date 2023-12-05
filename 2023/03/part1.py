import numpy as np

#data = np.loadtxt('test', dtype=str)

f = open('input', 'r')
data = []
for line in f:
    line = line.strip()
    data.append(line)
data = np.array(data)


N = data.shape[0]
M = len(data[0])

nums_part = 0 

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
            for s in str_line:
                if s != '.':
                    if not s.isdigit():
                        part_number = True
                        num = int(nums[k])
            nums_part += num


print(nums_part)