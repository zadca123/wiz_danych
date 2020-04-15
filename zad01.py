#Zad 1
lista = [x for x in range(4,40,4)]
plik=open("zadanie1.txt","w")
plik.writelines(str(lista))
plik.close()