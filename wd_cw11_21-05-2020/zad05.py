import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# szerokość 2 razy większa niż wysokość
fig = plt.figure()
X = np.arange(- 5 , 5 , 0.25)
Y = np.arange(- 5 , 5 , 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
ax1 = fig.add_subplot(121, projection = '3d' )
surf = ax1.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0 , antialiased = False)
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )


X = np.arange(- 5 , 5 , 0.1)
Y = np.arange(- 5 , 5 , 0.1)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
ax2 = fig.add_subplot(122, projection = '3d' )
surf = ax2.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0 , antialiased = True)
fig.colorbar(surf, shrink = 0.5 , aspect = 5) 

plt.show()