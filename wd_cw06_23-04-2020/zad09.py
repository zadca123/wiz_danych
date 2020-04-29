# Zad 9
# gotowe
import numpy as np

def fib(n):
    a = np.arange(n*n)
    a[0] = 0
    a[1] = 1
    for i in range(int(len(a)-2)):
        a[i+2] = a[i] + a[i+1]
    a = a.reshape((n,n))
    return a

fibonacci = fib(7)
print(fibonacci)