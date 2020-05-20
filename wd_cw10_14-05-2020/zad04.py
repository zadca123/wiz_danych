# Zad 4
# gotowe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

m=np.arange(0,30,0.1)

y=np.sin(m)+2
x=np.sin(m-3.15)

plt.plot(y,label='sin(x)+2')
plt.plot(x,'tab:orange',label='sin(x)')

plt.xlabel('x')
plt.ylabel('sin(x)')

plt.legend()
plt.show()