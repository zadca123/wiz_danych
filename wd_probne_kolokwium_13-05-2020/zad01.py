# Zad 1
# niegotowe?    powinno byc bez numpy
import numpy as np

def foo(lista):
    x = len(lista)
    for i in range(int(x/2)):
        if(i*i == x):
            wynik = np.arange(i*i)
            for p in range(x):
                wynik[p] = lista[p]
            wynik.reshape((i,i))
            # # lub
            # wynik = np.zeros((i,i))
            # for j in range(i):
            #     for k in range(i):
            #         wynik[j,k] = lista[j+k]
    return wynik




a = [2,3,4,5,6,7,2,2,2]
print(foo(a))
# wynik = []
# i=3
# for j in range(i):
#     for k in range(i):
#         wynik[j,k] = a[j+k]