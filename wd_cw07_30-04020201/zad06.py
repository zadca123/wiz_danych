# Zad 6
# gotowe
import numpy as np

x = np.arange(6,12).reshape(2,3)
b = np.zeros((2,3))
po = len(x)
po1 = len(x[0])

for i in range(po):
    for j in range(po1):
        b[i,j] = np.cos(x[i,j])
        
print(b)
