#Zad 4

class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jedn):
        self.q = nazwa_produktu
        self.w = ilosc
        self.e = jednostka_miary
        self.r = cena_jedn
    def wyswietl_produkt(self):
        return 'nazwa_produktu: {}\nilosc: {}\njednostka_miary: {}\ncena_jedn: {}'.format(self.q,self.w,self.e,self.r)
    def ile_produktu(self):
        return '{} {}{}'.format(self.q,self.w,self.e)
    def ile_kosztuje(self):
        return 'tyle kosztują {}: {}'.format(self.q,self.w*self.r)

zakupy = NaZakupy("ziemniaki",2,"kg",3)
print(zakupy.wyswietl_produkt())
print(zakupy.ile_produktu())
print(zakupy.ile_kosztuje())