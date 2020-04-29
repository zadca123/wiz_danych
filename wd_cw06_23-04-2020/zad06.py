# Zad 6
# gotowe
import numpy as np

def krzyzowka(a):
    b = np.fromiter(a, dtype='U1')
    zero = np.zeros((len(b), len(b)), dtype='U1')
    for i in range(len(zero)):
        for j in range(len(zero)):
            zero[i,i] = b[i]
            if(i==0):
                zero[i,j] = b[j]
            if(j == 0):
                zero[i,j] = b[i]
    return zero

a = krzyzowka(input("Wpisz slowo: "))
print(a)

