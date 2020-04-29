#Zad 4
# nie gotowe
import numpy as np  #nie do końca rozumiem funkcji logspace
# n = 2
# m = 4
# c = np.logspace(np.log2(2) , 16, 4)
# print(c)
# print(np.log2(4))

def foo(n,m):
    return [n**(i+1) for i in range(m)]
macierz = foo(2,4)
print(macierz)
