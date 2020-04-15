class Slowa:
    def __init__(self,slowo1,slowo2):
        self.x = slowo1
        self.y = slowo2

    def sprawdz_czy_palindrom(self):
        dlugosc = int(len(self.x) - len(self.x)%2)
        for i in range(dlugosc // 2):
            if(self.x[i] != self.x[dlugosc - i]):
                return False
        return True

    def sprawdz_czy_metagramy(self):
        if(len(self.x) != len(self.y)):
            return False
        spr = 0
        for i in range(len(self.x)):
            if(self.x[i] != self.y[i]):
                spr+=1
        if(spr == 1):
            return True
        return False

    def sprawdz_czy_anagramy(self):
        a = sorted(self.x)
        b = sorted(self.y)
        if(a == b):
            return True
        return False
    
    def wyswietl_wyraz(self):
        return '{} {}'.format(self.x,self.y)

a = Slowa("kajak","aajkk")
print(a.sprawdz_czy_palindrom())
print(a.sprawdz_czy_metagramy())
print(a.sprawdz_czy_anagramy())
print(a.wyswietl_wyraz())