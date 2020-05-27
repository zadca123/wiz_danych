import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as cm

#Zadanie 4
fig = plt.figure(figsize=(8, 3))
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax1 = fig.add_subplot(321, projection='3d')
ax1.bar3d(x, y, bottom, width, depth, top, shade=True, color = 'g')

ax2 = fig.add_subplot(322, projection='3d')
ax2.bar3d(x, y, bottom, width, depth, top, shade=True, color = 'r')

ax3 = fig.add_subplot(323, projection='3d')
ax3.bar3d(x, y, bottom, width, depth, top, shade=True, color = 'y')

ax4 = fig.add_subplot(324, projection='3d')
ax4.bar3d(x, y, bottom, width, depth, top, shade=True, color = 'b')

ax5 = fig.add_subplot(325, projection='3d')
ax5.bar3d(x, y, bottom, width, depth, top, shade=True, color = 'w')
plt.show()