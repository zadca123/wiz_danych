import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(19680801)
def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
n = 20
for color, mark, zlow, zhigh in [('r', 'x', 0,10)]:
    xs = randrange(n, 0, 10)
    ys = randrange(n, 0, 10)
    zs = randrange(n, zlow, zhigh)
    ax1.scatter(xs, ys, zs, c=color,marker=mark)

ax2 = fig.add_subplot(122, projection='3d')
z = np.linspace(0, 2 * np.pi,5)
x = np.sin(z)
y = np.cos(z)
ax2.plot(x,y,z)

plt.show()
