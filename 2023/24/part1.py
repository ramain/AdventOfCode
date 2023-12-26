import numpy as np

def compute_intersect(posi, posj, veli, velj):
    xi = posi[0]
    yi = posi[1]
    xj = posj[0]
    yj = posj[1]
    vxi = veli[0]
    vyi = veli[1]
    vxj = velj[0]
    vyj = velj[1]

    mi = vyi / vxi
    mj = vyj / vxj
    bi = yi - mi * xi
    bj = yj - mj * xj

    x_intersect = (bj - bi) / (mi - mj)
    y_intersect = mi * x_intersect + bi
    t_intersect1 = (x_intersect - xi) / vxi
    t_intersect2 = (x_intersect - xj) / vxj
    t_intersect = min(t_intersect1, t_intersect2)


    return x_intersect, y_intersect, t_intersect

fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

positions = []
velocities = []

for line in infile:
    line = line.strip()
    line = line.split("@")
    poss = []
    vels = []
    for pos in line[0].split(','):
        poss.append(int(pos))
    for vel in line[1].split(','):
        vels.append(int(vel))
    velocities.append(vels)
    positions.append(poss)

positions = np.array(positions)
velocities = np.array(velocities)
if fname == "test.txt":
    posrange = [7, 27]
elif fname == "input.txt":
    posrange = [200000000000000, 400000000000000]

count = 0
for i in range(positions.shape[0]-1):
    posi = positions[i,:]
    veli = velocities[i,:]
    for j in range(i+1, positions.shape[0]):
        posj = positions[j,:]
        velj = velocities[j,:]
        x_intersect, y_intersect, t_intersect = compute_intersect(posi, posj, veli, velj)
        if (x_intersect > posrange[0]) and (x_intersect < posrange[1]):
            if (y_intersect > posrange[0]) and (y_intersect < posrange[1]):
                if t_intersect > 0:
                    count += 1

print(count)