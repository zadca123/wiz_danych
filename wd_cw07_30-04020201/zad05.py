# Zad 5
# gotowe
import numpy as np

x = np.arange(6).reshape(2,3)
a = np.zeros((2,3))
po = len(x)
po1 = len(x[0])

for i in range(po):
    for j in range(po1):
        a[i,j] = np.sin(x[i,j])
        
print(a)
