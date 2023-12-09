import numpy as np

def create_tree(sequence):
    tree = []
    tree.append(sequence)
    seqi = sequence
    for i in range(len(sequence)):
        seqi = np.diff(seqi)
        tree.append(seqi)
        if np.all(seqi==0):
            break
    
    return tree


def extend_tree(tree):
    for i in np.arange(len(tree))[::-1]:
        if i == len(tree) - 1:
            pad = 0
        else:
            pad = tree[i][-1] + tree[i+1][-1]
        tree[i] = np.append(tree[i], pad)
    return tree

def extend_tree_backwards(tree):
    for i in np.arange(len(tree))[::-1]:
        if i == len(tree) - 1:
            pad = 0
        else:
            pad = tree[i][0] - tree[i+1][0]
        tree[i] = np.append(pad, tree[i])
    return tree


infile = 'input'
#infile = 'test'

data = np.loadtxt(infile, dtype='int')

num_end = 0
num_front = 0
for i in range(len(data)):
    d = data[i]

    tree = create_tree(d)
    tree = extend_tree(tree)
    num_end += tree[0][-1]

    tree = create_tree(d)
    tree = extend_tree_backwards(tree)
    num_front += tree[0][0]



print(num_end)
print(num_front)