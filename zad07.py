class Robaczek:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def idz_w_gore(self,a):
        self.y += a
    def idz_w_dol(self,a):
        self.y -= a
    def idz_w_lewo(self,a):
        self.x -= a
    def idz_w_prawo(self,a):
        self.x += a
    def pokaz_gdzie_jestes(self):
        return '({}, {})'.format(self.x, self.y)

foo = Robaczek(0, 0)
foo.idz_w_dol(3)
foo.idz_w_lewo(4)
foo.idz_w_prawo(3)
foo.idz_w_gore(81)
print(foo.pokaz_gdzie_jestes())