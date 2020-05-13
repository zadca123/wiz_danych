# Zad 5
# gotowe
import random

a = []
for i in range(20):
    a.append(random.randrange(1,30)) 
print(a)

temp = 0
for i in range(len(a)):
    temp += a[i]
temp = int(temp/len(a))
print(temp)

mniejsze_rowne = []
wieksze = []

for i in range(len(a)):
    if(a[i] > temp):
        wieksze.append(a[i])
    else:
        mniejsze_rowne.append(a[i])

print(mniejsze_rowne)
print(wieksze)