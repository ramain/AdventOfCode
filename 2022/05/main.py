import numpy as np

def parse_input(f):
    header = []
    for line in f:
        if line == '\n':
            break
        header.append(line)

    n_move = []
    n_from = []
    n_to = []
    for line in f:
        lineparse = line.split()
        n_move.append(int(lineparse[1]))
        n_from.append(int(lineparse[3]) - 1)
        n_to.append(int(lineparse[5]) - 1)

    return header, n_move, n_from, n_to


def move_boxes(boxes, n_move, n_from, n_to, CrateMover=9000):
    # write box moving
    s1 = boxes[n_from]
    s2 = boxes[n_to]
    smove = s1[:n_move]
    if CrateMover == 9000:
        smove = smove[::-1]
    s2 = smove + s2
    s1 = s1[n_move:]
    boxes[n_from] = s1
    boxes[n_to] = s2
    return boxes


def main(CrateMover=9000):

    f = open("input", "r")
    header, n_move, n_from, n_to = parse_input(f)

    headerparse = []
    for i in range(len(header)):
        hi = list(header[i])
        headerparse.append(hi)

    headerparse = np.array(headerparse)
    key = headerparse[-1]
    key = np.argsort(key)[-9:]
    boxes = headerparse[:-1, key]

    print(boxes)
    boxes = boxes.T
    boxlist = []
    for i in range(boxes.shape[0]):
        box = boxes[i]
        boxstring = ''
        for s in box:
            if s != ' ':
                boxstring += s
        boxlist.append(boxstring)

    N_instr = len(n_move)
    for i in range(N_instr):

        boxlist = move_boxes(boxlist, n_move[i], n_from[i], n_to[i], CrateMover=CrateMover)

    print(boxlist)
    final_crates = ''
    for box in boxlist:
        final_crates += box[0]
    print(final_crates)

if __name__ == "__main__":
    main(CrateMover=9000)
    main(CrateMover=9001)