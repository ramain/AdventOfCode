import numpy as np
from numba import njit, prange

f = open('input', 'r')
#f = open('test', 'r')

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

# using numba to make brute-force tractable (shameful, but it works!)
# wanted to use parallel=True, but had race conditions
@njit
def seed_mapping_loop(seeds_low, seeds_ran, mappings):
    final_location = int(1000000000)
    for i_s in prange(len(seeds_low)):
        print(f"seed {i_s} of {len(seeds_low)}")
        i_range = seeds_ran[i_s]

        for j in range(i_range):
            i_seed = seeds_low[i_s] + j

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
            if i_seed < final_location:
                final_location = i_seed
    return final_location


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

seeds_low = seeds[::2]
seeds_ran = seeds[1::2]

mappings = [seedtosoil, soiltofertilizer, fertilizertowater, watertolight, lighttotemperature, temperaturetohumidity, humiditytolocation]

final_location = seed_mapping_loop(seeds_low, seeds_ran, mappings)
print(final_location)
