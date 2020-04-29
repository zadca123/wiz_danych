# Zad 8
# gotowe
import numpy as np

# kierunek == 1     --tnij w pionie
# kierunek == 0     --tnij w poziomie

def foo(tab, kierunek):
    x = int(len(tab))
    if(len(tab)%2 != 0 or len(tab) != len(tab[0])):
        return 'Macierz nie jest diagonalna lub jest nieparzysta'
    if(kierunek == 0):
        s = slice(0,int(x/2))
        return tab[s]

    if(kierunek == 1):
        tab = tab.reshape((2*x,int(x/2)))
        s = slice(0,x*2,2)
        return tab[s]

n = 6
kierunek = 1
tab = np.arange(n*n)
tab = tab.reshape((n,n))

tab_przetnij = foo(tab,kierunek)
print(tab_przetnij)