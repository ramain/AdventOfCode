import numpy as np

def possible_steps(stepgrid, mask):
    s_up = np.roll(stepgrid, 1, axis=0)
    s_down = np.roll(stepgrid, -1, axis=0)
    s_left = np.roll(stepgrid, 1, axis=1)
    s_right = np.roll(stepgrid, -1, axis=1)
    s_up[0] = 0
    s_down[-1] = 0
    s_left[:,0] = 0
    s_right[:,-1] = 0

    new_stepgrid = np.zeros(stepgrid.shape)
    new_stepgrid += s_up
    new_stepgrid += s_down
    new_stepgrid += s_left
    new_stepgrid += s_right
    new_stepgrid *= mask
    new_stepgrid[new_stepgrid > 1] = 1
    return new_stepgrid


fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

grid = []
for line in infile:
    grid.append(list(line.strip()))

grid = np.array(grid)

stepgrid = np.zeros(grid.shape)
stepgrid[grid == "S"] = 1

mask = np.ones(grid.shape)
mask[grid == "#"] = 0


Nsteps = 64
for i in range(Nsteps):
    stepgrid = possible_steps(stepgrid, mask)
print(stepgrid.sum())
