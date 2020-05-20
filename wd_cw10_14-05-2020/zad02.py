# Zad 2
# gotowe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

t = np.arange(1.,20,1.)
plt.plot(t,1/t,'g^',t,1/t,'g:',label='f(x)=1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Wykres funkcji f(x) dla x[1,20]")

plt.legend()
plt.show()