import numpy as np

fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

def count_area(xs, ys):
    # Using trapezoid formula for area from a set of vertices
    count = 0
    for i in range(len(xs)-1):
        x1 = xs[i]
        x2 = xs[i+1]
        y1 = ys[i]
        y2 = ys[i+1]
        count += int((y2+y1)*(x2-x1)/2)
    return count

directions = []
steps = []
colours = []
for line in infile:
    line = line.strip().split()
    colour = line[2][1:-1]

    Nstep = int(colour[1:6], 16)
    steps.append(Nstep)
    direction = int(colour[6])
    if direction == 0:
        directions.append("R")
    elif direction == 1:
        directions.append("D")
    elif direction == 2:
        directions.append("L")
    elif direction == 3:
        directions.append("U")

xs = []
ys = []
yranges = []
i = 0
j = 0
xs.append(i)
ys.append(j)

perimiter = np.sum(steps)
for k in range(len(directions)):
    dir = directions[k]
    step = steps[k]
    if dir == "R":
        i += step
    if dir == "L":
        i -= step
    if dir == "U":
        j += step
    if dir == "D":
        j -= step
    xs.append(i)
    ys.append(j)

count = count_area(xs, ys)
# not sure why perimiter//2 +1 is needed, but it worked on test case and 
# seemed a simple geometric factor
final_count = count + perimiter//2 +1
print(final_count)

# For quick debugging...
if fname == "test.txt":
    correct = 952408144115
    if final_count == correct:
        print("Correct")
    elif final_count < correct:
        print("Too low by", correct - final_count)
    elif final_count > correct:
        print("Too high by", final_count - correct)
        