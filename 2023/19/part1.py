import numpy as np

def run_workflow(workflow_name, xmas):
    x = xmas[0]
    m = xmas[1]
    a = xmas[2]
    s = xmas[3]
    if workflow_name == 'A':
        print("accepted;", xmas, x+m+a+s)
        return x+m+a+s
    elif workflow_name == 'R':
        print("rejected;", xmas, x+m+a+s)
        return 0

    i = np.argwhere(workflow_names == workflow_name)[0][0]
    instructions = workflow_instructions[i]
    dest_default = instructions[-1]
    value = 0

    for instruction in instructions[:-1]:
        dest = instruction.split(':')[-1]
        var = instruction.split(':')[0][0]
        comp = instruction.split(':')[0][1]
        val = int(instruction.split(':')[0][2:])
        if var == 'x':
            xi = x
        elif var == 'm':
            xi = m
        elif var == 'a':    
            xi = a
        elif var == 's':
            xi = s
        print(var, comp, val, dest, xi)

        if comp == '>':
            if xi > val:
                value = run_workflow(dest, xmas)
                return value
        elif comp == '<':
            if xi < val:
                value = run_workflow(dest, xmas)
                return value
    value = run_workflow(dest_default, xmas)
    return value


fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

workflows = []
xmasvals = []

for line in infile:
    line = line.strip()
    if line.startswith('{'):
        xmasval = line.split('{')[1].split('}')[0].split(',')
        xmaslist = []
        for val in xmasval:
            xmaslist.append(int(val.split('=')[1]))
        xmasvals.append(xmaslist)
    else:
        if line:
            workflows.append(line)
workflow_names = []
workflow_instructions = []

for i in range(len(workflows)):
    workflow = workflows[i]
    name = workflow.split('{')[0]
    instructions = workflow.split('{')[1].split('}')[0].split(',')
    workflow_names.append(name)
    workflow_instructions.append(instructions)

workflow_names = np.array(workflow_names)

count = 0
for i in range(len(xmasvals)):

    xmas = xmasvals[i]
    print(xmas)
    counti = run_workflow('in', xmas)
    if counti:
        count += counti
    print(xmas, counti, count)

print(count)