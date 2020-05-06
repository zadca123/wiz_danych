# Zad 9
# gotowe
import numpy as np

a = np.arange(9,18).reshape(3,3)

print(a)
b = a.ravel()
print(b)

for i in b:
    print(i)
