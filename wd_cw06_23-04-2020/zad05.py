#Zad 5
# gotowe
import numpy as np

def foo(n):
    macierz_diag = np.diag([a+1 for a in range(n)])
    return macierz_diag[::-1]

b = foo(3)
print(b)
