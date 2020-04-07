import math
import numpy
## radzilbym każde zadanie odkomentowywać i zakomentowywać po kolei
# Zad 1 gotowe
# A = [1/x for x in range(1,11)]
# B = [2**i for i in range(11)]
# C = [x for x in B if x % 4 == 0]
# print(A)
# print(B)
# print(C)

## Zad 2 niedokońca poprawnie
# macierz=numpy.random.rand(4,4)
# print(macierz)
# lista=[]
# for i in range(4):  #len(macierz) nie działało
#     for j in range(4):
#         if i==j:
#             lista.append([macierz[i,j]])
# print(lista)
## lista2 = [macierz[i,j] for i in range(4) and for j in range(4) if i==j]   #nie wiedziałem jak przekonwertowac
## print(lista2)

## Zad 3 gotowe
# zakupy={"Woda": "1L",
#             "Chleb": "1 szt.",
#             "Gruszka": "2kg."}
# zakupy_pc={value: key for key,value in zakupy.items()}
# print(zakupy)
# print(zakupy_pc)

## Zad 4 gotowe
# def monotonicznosc(a,b):
#     if(a>0):
#         print("funkcja rosnaca")
#     elif(a<0):
#         print("funkcja malejaca")
#     else:
#         print("funkcja stala")
# print(monotonicznosc(1,1))
# print(monotonicznosc(-1,1))
# print(monotonicznosc(0,1)

## Zad 5 gotowe
# def prostopadle(x1,y1,x2,y2):
#     if(x1==x2):
#         print("proste sa rownolegle")
#     elif(x1*x2==-1):
#         print("proste sa prostopadle")
#     else:
#         print("proste nie sa ani prostopadle, ani rownolegle")
# print(prostopadle(3,2,4,2))

## Zad 6 gotowe
# def promien(x=0,a=0,y=0,b=0):
#     x = math.sqrt((x-a)**2 + (y-b)**2)
#     return x
# print(promien(1,2,3,3))

## Zad 7 gotowe
# def przeciwprostokatna(a=0,b=0):
#     c=0.0
#     c+=a*a+b*b
#     return c**(1/2)
# print(przeciwprostokatna(3,4))

## Zad 8 niedokońca poprawne
# def suma_ciagu(a=1,r=1,ile=10):
#     if ile == 0:
#         return 0.0
#     else:
#         suma = 0.0
#         for i in range(ile):
#             i+=1  #zbedne ale nie miałem posysłu
#             suma += a
#             a += r
#         return suma
# print(suma_ciagu(1,2,4))

## Zad 9 gotowe
# def suma_iloczynu(*liczby):
#     if len(liczby) == 0:
#         return 0.0
#     else:
#         iloczyn = 1.0
#         for i in liczby:
#             iloczyn*=i
#         return iloczyn
# print(suma_iloczynu2(1,2,3,4))

## Zad 10 gotowe
# zakupy3 = {"Woda": "1L" ," Chleb": "1 szt.","Gruszka": "2kg."}
# def to_lubie(slownik,** zakupy):
#     for klucz,wartosc in slownik.items():
#         print("To jest : ")
#         print(klucz)
#         print(" co lubie ")
#         print(wartosc)
# to_lubie(zakupy3)

## Zad 11 niedokońca poprawnie
## W tym zadaniu nie potrafilem stworzyc pakietu bez błędu więc
## stworzyłem moduły w folderze z plikiem
## import cmath # nie jest potrzebne gdyż stworzone moduły go zawieraja
## from zespolone import *   # dziala czesciowo
## import zespolone          # nie dziala
# import oblicz     # dziala
# import lb_zesp    # dziala 
# x1=3; y1=5; z1=complex(x1,y1)
# x2=6; y2=3; z2=complex(x2,y2)
# print(oblicz.dodaj_zesp(z1,z2))
# print(oblicz.odejmij_zesp(z1,z2))
# print(lb_zesp.rzeczywista(z1))
# print(lb_zesp.urojona(z1))

## Zad 12 niedokońca poprawnie
## podobnie jak w poprzednim zadaniu...
## from ciagi import *
## import ciagi as ciag
# from aryt import *
# from geom import *
# print(suma_ciagu2(1,2,3,4))
# print(suma_iloczynu2(1,2,3,4))