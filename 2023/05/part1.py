import numpy as np

f = open('input', 'r')
#f = open('test', 'r')

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

for i,line in enumerate(nonblank_lines(f)):
    if i == 0:
        seeds = line.split(':')[-1]
        seeds = seeds.strip().split()
        seeds = np.array(seeds).astype(int)

    if 'seed-to-soil' in line:
        arr = []
    if 'soil-to-fertilizer' in line:
        seedtosoil = np.array(arr).astype('int')
        arr = []
    if 'fertilizer-to-water' in line:
        soiltofertilizer = np.array(arr).astype('int')
        arr = []
    if 'water-to-light' in line:
        fertilizertowater = np.array(arr).astype('int')
        arr = []
    if 'light-to-temperature' in line:
        watertolight = np.array(arr).astype('int')
        arr = []
    if 'temperature-to-humidity' in line:
        lighttotemperature = np.array(arr).astype('int')
        arr = []
    if 'humidity-to-location' in line:
        temperaturetohumidity = np.array(arr).astype('int')
        arr = []    
    
    map = line.split()
    if map[0].isdigit():
        arr.append(map)

humiditytolocation = np.array(arr).astype('int')


mappings = [seedtosoil, soiltofertilizer, fertilizertowater, watertolight, lighttotemperature, temperaturetohumidity, humiditytolocation]
final_locations = []

for i_seed in seeds:
    print("new seeed: \n", i_seed)
    for k in range(len(mappings)):
        mappingi = mappings[k]

        d0 = mappingi[:,0]
        s0 = mappingi[:,1]
        N = mappingi[:,2]

        for i in range(len(s0)):
            s_low = s0[i]
            s_high = s0[i]+N[i]
            d_low = d0[i]
            d_high = d0[i]+N[i]
            if i_seed >= s_low and i_seed < s_high:
                i_seed = d_low + (i_seed-s_low)
                break
        print(i_seed)
    final_locations.append(i_seed)

print(final_locations)
print(np.min(final_locations))

