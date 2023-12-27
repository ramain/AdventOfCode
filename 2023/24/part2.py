import numpy as np
import sympy as sp
from sympy.solvers import solve

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

"""
The number of unknowns equals the number of equations after 3 hailstones, 
so the system of equations can be solved (provided the equations are linearly independent).
Worked for both the test case ad input.
"""

pos0 = positions[0,:]
pos1 = positions[1,:]
pos2 = positions[2,:]
vel0 = velocities[0,:]
vel1 = velocities[1,:]
vel2 = velocities[2,:]

x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')
vx = sp.Symbol('vx')
vy = sp.Symbol('vy')
vz = sp.Symbol('vz')
t0 = sp.Symbol('t0')
t1 = sp.Symbol('t1')
t2 = sp.Symbol('t2')

eq1 = sp.Eq( (pos0[0]-x) + (vel0[0]-vx)*t0, 0 )
eq2 = sp.Eq( (pos0[1]-y) + (vel0[1]-vy)*t0, 0 )
eq3 = sp.Eq( (pos0[2]-z) + (vel0[2]-vz)*t0, 0 )
eq4 = sp.Eq( (pos1[0]-x) + (vel1[0]-vx)*t1, 0 )
eq5 = sp.Eq( (pos1[1]-y) + (vel1[1]-vy)*t1, 0 )
eq6 = sp.Eq( (pos1[2]-z) + (vel1[2]-vz)*t1, 0 )
eq7 = sp.Eq( (pos2[0]-x) + (vel2[0]-vx)*t2, 0 )
eq8 = sp.Eq( (pos2[1]-y) + (vel2[1]-vy)*t2, 0 )
eq9 = sp.Eq( (pos2[2]-z) + (vel2[2]-vz)*t2, 0 )

sol = solve([eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9], x, y, z, vx, vy, vz, t0, t1, t2 )

print(sol)
print(sol[0][0] + sol[0][1] + sol[0][2])