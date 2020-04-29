# Zad 3
# gotowe
import numpy as np

def foo(n):
    a = np.arange(1,n*n+1)
    a = a.reshape((n,n))
    return a

b = foo(3)
print(b)