import numpy as np

f = open('input', 'r')

numlims = {'red': 12, 'green': 13, 'blue': 14}

powers = []

for line in f:
    line = line.split(':')[-1]
    reveals = line.split(';')
    reds = [0]
    greens = [0]
    blues = [0]
    for rev in reveals:

        x = rev.split(',')
        for xi in x:
            xi = xi.split()
            num = int(xi[0])
            color = xi[1]
            if color == 'red':
                reds.append(num)
            elif color == 'green':
                greens.append(num)
            elif color == 'blue':
                blues.append(num)

    power = max(reds) * max(greens) * max(blues)
    powers.append(power)

powers = np.array(powers)
print(np.sum(powers))