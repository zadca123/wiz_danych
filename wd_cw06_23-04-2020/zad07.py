#Zad 7
# gotowe
import numpy as np

def foo(n):
    a = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a[i,j] = 2
            if(i>j):
                a[i,j] += 2*i
                a[i,j] -= 2*j
            if(i<j):
                a[i,j] += 2*j
                a[i,j] -= 2*i
    return a

a = foo(4)
print(a)