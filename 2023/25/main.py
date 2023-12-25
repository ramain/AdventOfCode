import networkx as nx
import matplotlib.pyplot as plt

fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")

connections = {}
for line in infile:
    line = line.strip().split()
    key = line[0][:-1]
    vals = line[1:]
    connections[key] = vals

plt.figure(figsize=(10,10))
G = nx.Graph(connections)
nx.draw_networkx(G, with_labels=True)
plt.show()

"""
From visualization, 3 connected nodes are:
kzx: qmr
nvb: fts
zns: jff
"""

vals = connections["kzx"]
vals.remove("qmr")
connections["kzx"] = vals

vals = connections["nvb"]
vals.remove("fts")
connections["nvb"] = vals

vals = connections["zns"]
vals.remove("jff")
connections["zns"] = vals

# remake graph, observe that it is now disconnected
plt.figure(figsize=(10,10))
G = nx.Graph(connections)
nx.draw_networkx(G, with_labels=True)
plt.show()

N = nx.node_connected_component(G, 'kzx')
M = nx.node_connected_component(G, 'qmr')
print(len(N)*len(M))