# Projekcja 3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import random

np.random.seed(19680801)
def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.gca( projection = '3d' )
n = 100
x = randrange(n,0,1) 
y = randrange(n,0,1) 
z = randrange(n,0,1) 
ax.scatter(x, y, z, c='r', marker='o')

n2 = 10
x = randrange(n2,0,1) 
y = randrange(n2,0,1) 
z = randrange(n2,0,1)
ax.plot(x,y,z)
plt.show()