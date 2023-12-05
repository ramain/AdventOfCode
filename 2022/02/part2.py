
import numpy as np

data=np.loadtxt('input', dtype='str')

opponent = data[:,0]
opponent[opponent=='A'] = 1
opponent[opponent=='B'] = 2
opponent[opponent=='C'] = 3
opponent = opponent.astype('int')

results = data[:,1]
results[results=='X'] = 0
results[results=='Y'] = 3
results[results=='Z'] = 6
results = results.astype('int')

def rps(o, result):
    r = result // 3
    if r==1:
        #"draw"
        p = o
        print('draw', o, p)
    elif r==0:
        #"loss"
        p = o - 1
        if p == 0:
            p = 3
        print('loss', o, p)
    elif r==2:
        #"win"
        p = (o % 3) + 1
        print('win', o, p)
    else:
        print('result must be 0, 3, or 6')
    return p

    
scores = []
for i in range(len(results)):
    oi = opponent[i]
    ri = results[i]
    pi = rps(oi, ri)
    score = ri + pi
    scores.append(score)
    
scores = np.array(scores)
score_total = np.sum(scores)
print(score_total)
