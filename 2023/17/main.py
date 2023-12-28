import numpy as np
from queue import PriorityQueue

def navigate_grid(grid, max_steps=3, min_steps=1):
    gridscore = np.zeros(grid.shape)+1000000

    queue = PriorityQueue()
    i_max = grid.shape[0] - 1
    j_max = grid.shape[1] - 1

    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    for direction in directions:
        # (score, i, j, direction)
        queue.put((0, 0, 0, direction))

    visited = set()

    while queue:
        score, i, j, direction = queue.get()
        # goes until it hits the x,y endpoint
        if (i == i_max) and (j == j_max):
            break
        if (i, j, direction) in visited:
            continue

        visited.add((i, j, direction))

        for Nstep in range(max_steps):
            j_new = j + (Nstep+1) * direction[1]
            i_new = i + (Nstep+1) * direction[0]

            # break if out of bounds
            if (j_new < 0) or (i_new < 0) or (j_new > j_max) or (i_new > i_max):
                break
            # gridscore only for visualization
            if score < gridscore[i_new, j_new]:
                gridscore[i_new, j_new] = score

            score += grid[i_new, j_new]
            # head in either perpendicular direction, if minimum number of steps taken (for part 2)
            directions = [(direction[1], direction[0]), (-direction[1], -direction[0])]
            if Nstep >= (min_steps-1):
                for dir in directions:
                    if ((i_new, j_new, dir)) not in visited:
                        queue.put((score, i_new, j_new, dir))

    return score, gridscore


fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

data = []
for line in infile:
    data.append(list(line.strip()))

data = np.array(data).astype(int)

score, gridscore = navigate_grid(data, max_steps=3, min_steps=1)
if fname == "test.txt":
    correct = 102
    if score == correct:
        print(f"correct answer of {correct} on test input")
print("Part1: ", score)

score, gridscore = navigate_grid(data, max_steps=10, min_steps=4)
if fname == "test.txt":
    correct = 94
    if score == correct:
        print(f"correct answer of {correct} on test input")
print("Part2: ", score)
