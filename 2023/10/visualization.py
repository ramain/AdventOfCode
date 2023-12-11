import numpy as np
import matplotlib.pyplot as plt

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