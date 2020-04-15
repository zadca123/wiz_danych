#Zad 3
import sys
with open("zadanie3.txt","a+") as plik:
    dane = sys.stdin.readline()
    plik.write(dane)

    with open("zadanie3.txt","r") as plik:
        for i in plik:
            print(i, end="")