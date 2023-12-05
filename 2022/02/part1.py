
import numpy as np

data=np.loadtxt('input', dtype='str')

player = data[:,1]
player[player=='X'] = 1
player[player=='Y'] = 2
player[player=='Z'] = 3
player = player.astype('int')

opponent = data[:,0]
opponent[opponent=='A'] = 1
opponent[opponent=='B'] = 2
opponent[opponent=='C'] = 3
opponent = opponent.astype('int')

def rps(o,p):
    diff = p - o
    if diff==0:
        #result = 'Draw'
        result = 3
    elif (diff==-1) or (diff==2):
        #result = 'Loss'
        result = 0
    else:
        result = 6
        #result = 'Win'
    return result
    
    
scores = []
for i in range(len(player)):
    o = opponent[i]
    p = player[i]
    result = rps(o,p)
    score = result + p
    scores.append(score)
    
scores = np.array(scores)
score_total = np.sum(scores)
print(score_total)
