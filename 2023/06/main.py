import numpy as np
f = open('input', 'r')
#f = open('test', 'r')

times = []
distances = []
time_comb = ''
distance_comb = ''

for i,line in enumerate(f):
    line = line.split()
    print(line)
    if i == 0:
        for l in line[1:]:
            times.append(int(l))
            time_comb += l
    else:
        for l in line[1:]:
            distances.append(int(l))
            distance_comb += l
            
print(distances, distance_comb)
print(times, time_comb)

# Part 1
Wlens = 1
for i in range(len(times)):
    W = []
    D = distances[i]
    T = times[i]
    
    c_range = np.arange(T)
    for c in c_range:
        d = c*(T-c)
        if d > D:
            W.append(d)
    Wlens *= len(W)
print(Wlens)

# Part 2
W = []
T = int(time_comb)
D = int(distance_comb)
c_range = np.arange(T)
for c in c_range:
    d = c*(T-c)
    if d > D:
        W.append(d)
print(len(W))