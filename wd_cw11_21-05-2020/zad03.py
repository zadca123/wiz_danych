import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)

ax1 = fig.add_subplot(321, projection = '3d' )
surf = ax1.plot_surface(X, Y, Z, cmap = cm.viridis, linewidth = 0 , antialiased = False )
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )

ax2 = fig.add_subplot(322, projection = '3d' )
surf = ax2.plot_surface(X, Y, Z, cmap = cm.plasma, linewidth = 0 , antialiased = False )
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )

ax3 = fig.add_subplot(323, projection = '3d' )
surf = ax3.plot_surface(X, Y, Z, cmap = cm.Greys, linewidth = 0 , antialiased = False )
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )

ax4 = fig.add_subplot(324, projection = '3d' )
surf = ax4.plot_surface(X, Y, Z, cmap = cm.Greens, linewidth = 0 , antialiased = False )
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )

ax5 = fig.add_subplot(325, projection = '3d' )
surf = ax5.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0 , antialiased = False )
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )

plt.show()