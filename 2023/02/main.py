import numpy as np

f = open('input', 'r')

numlims = {'red': 12, 'green': 13, 'blue': 14}

games = []
i = 1
for line in f:
    line = line.split(':')[-1]
    reveals = line.split(';')

    for rev in reveals:
        x = rev.split(',')
        for xi in x:
            xi = xi.split()
            num = int(xi[0])
            color = xi[1]
            if num > numlims[color]:
                games.append(i)
                print(i, line)
    i += 1

games = np.array(games)
games = np.unique(games)

print(games, np.sum(games))

games_good = np.arange(1,101)
games_good = np.setdiff1d(games_good, games)

print(games_good)
print(np.sum(games_good))