import numpy as np
import matplotlib.pyplot as plt
import os

vis = np.load("vis.npz")
water = vis['vis']
xpath = vis['xpath']
ypath = vis['ypath']

plt.figure()
plt.imshow(water, cmap='Greys_r', interpolation='None')
plt.plot(xpath, ypath, c='b', lw=3.0, alpha=0.8)
plt.xticks([])
plt.yticks([])
plt.show()

print(len(xpath))
# Generate gif
step = 100
for i in range(len(xpath)//step):
    plt.figure(figsize=(5,5))
    plt.plot(xpath[:i*step], ypath[:i*step], c='k', lw=1.0, alpha=0.8)
    plt.xticks([])
    plt.yticks([])
    plt.xlim(0, water.shape[1])
    plt.ylim(0, water.shape[0])
    plt.savefig(f"plot_{i:03}.png")
    plt.close()

for i in range(water.shape[0]):
    plt.figure(figsize=(5,5))
    plt.plot(xpath, ypath, c='k', lw=1.0, alpha=0.8)
    plt.xticks([])
    plt.yticks([])
    plt.xlim(0, water.shape[1]-1)
    plt.ylim(0, water.shape[0]-1)
    j = len(xpath)//step + i
    plt.imshow(water[:i], cmap='Blues', interpolation='None', vmin=-0.2, vmax=1)
    plt.savefig(f"plot_{j:03}.png")
    plt.close()

os.system("convert -delay 5 -loop 1 plot*png pipe.gif")
os.system("rm plot*png")
