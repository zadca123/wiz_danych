# Zad 11
# gotowe
import numpy as np

a = np.arange(12)

b = a.reshape((3,4))
c = a.reshape((4,3))
d = a.reshape((2,6))
b = b.ravel()
c = c.ravel()
d = d.ravel()
print(b,c,d)    # są identyczne