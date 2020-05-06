# Zad 2
# gotowe
import numpy as np

a = np.arange(1,10).reshape(3,3)
b = np.arange(16,32).reshape(4,4)
b = b[::-1] * (-1)
print(a.min(axis=0))
print(a.min(axis=1))
print(b.min(axis=0))
print(b.min(axis=1))
            