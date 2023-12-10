import numpy as np

def move_forward(move, prev_dir):
    ### need to handle 1,1 cases
    dir_next = np.copy(moves[move])
    if move in ['L', 'J', '7', 'F']:
        if prev_dir[0] != 0:
            dir_next[0] = 0
        elif prev_dir[1] != 0:
            dir_next[1] = 0
    if move in ['|', '-']:
        dir_next = moves[move]*np.sign(prev_dir)

    return dir_next

infile = 'input'
#infile = 'test2'
f = open(infile, 'r')
lines = f.readlines()

grid = []
for line in lines:
    grid.append(list(line.strip()))

grid = np.array(grid)
grid = grid[:,::-1]
grid = np.pad(grid, 1, 'constant', constant_values='.')

moves = {
    '|': [0, 1],
    '-': [1, 0],
    'L': [-1, -1],
    'J': [1, -1],
    '7': [1, 1],
    'F': [-1, 1],
    'S': [0, 0]
}


start = np.where(grid=='S')
j_start = start[0][0]
i_start = start[1][0]
i = i_start
j = j_start

# find starting direction

smove = np.array([[1,0], [0,-1], [-1,0], [0,1]])
s_directions = []

for sm in smove:
    if grid[j+sm[0], i+sm[1]] in moves:
        i_move = np.argwhere(np.abs(sm)>0)[0][0]
        print(i_move)
        move = grid[j+sm[0], i+sm[1]]
        if sm[i_move] == moves[move][i_move]:
            s_directions.append(sm)

dir = s_directions[0]

# follow path

length = []
path = []
path_ij = []

for k in range(100000):
    dir0 = dir
    print(dir, grid[j, i])
    path_ij.append([j, i])
    i += dir[0]
    j += dir[1]
    dir = moves[grid[j, i]]
    path.append(grid[j, i])
    length.append(k)
    if grid[j,i] == 'S':
        break
    dir = move_forward(grid[j, i], dir0)

Nmid = int(len(length)//2)
letter = path[Nmid]
print(letter, Nmid)



# Part 2
loop_enclosed = 0
for j in range(grid.shape[0]):
    line = grid[j]

    for i in range(grid.shape[1]):
        if [j, i] not in path_ij:
            count = 0
            for k,l in enumerate(line[:i]):
                if l in ['L', 'J', '|', 'S']:
                    if [j, k] in path_ij:
                        count += 1
            if count % 2 == 1:
                loop_enclosed += 1
                #print(line, grid[j, i])

print(loop_enclosed)

# Can do something clever with floodfill, I feel this is almost working
# Worked for test, but not on input
"""mask = np.zeros(grid.shape) 
for ij in path_ij:
    mask[ij[0], ij[1]] = 1

from skimage.measure import label

labels = label(mask, connectivity=1, background=1)
print(labels)
print(len(np.argwhere(labels>1)))"""