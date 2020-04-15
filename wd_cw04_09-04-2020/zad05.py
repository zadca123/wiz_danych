#zad 5
import sys
class ciag_aryt:
    def __init__(self,pierwszy_element,ile_elementow,roznica):
        self.a1 = pierwszy_element
        self.n = ile_elementow
        self.r = roznica
    def wyswietl_dane(self):
        return [self.a1+self.r*i for i in range(self.n)]
    def pobierz_elementy(self):
        print("Wpisz ")
        self.a1 = int(input("pierwszy_element: "))
        self.r = int(input("różnica: "))
        self.n = int(input("ile_elementow: "))
    def pobierz_parametry(self,x,y,z):
        self.a1 = x
        self.r = y
        self.n = z
    def policz_sume(self):
        suma = 0
        for i in range(self.n):
            suma+=self.a1+self.r*i
        return suma
    def policz_elementy(self,x,y,z = 0):
        return [x+y*i for i in range(self.n)]


        
ciag = ciag_aryt(1,10,3)
print(ciag.wyswietl_dane())
print(ciag.pobierz_elementy())
print(ciag.wyswietl_dane())
print(ciag.pobierz_parametry(1,2,3))
print(ciag.policz_sume())
print(ciag.policz_elementy(3,4))