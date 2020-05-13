# Zad 6
# gotowe
import random

def kostka2():
    x = 0
    y = 0 
    while(x+y != 12):
        x = 0
        y = 0
        x = random.randrange(1,7)
        y += random.randrange(1,7)
        print(x,y,'\n')
    
    return x,y

print(kostka2())