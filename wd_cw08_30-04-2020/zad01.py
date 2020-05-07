# Zad 1
# gotowe
import pandas as pd
import xlrd
import openpyxl

a = pd.read_excel('imiona.xlsx')    # Rok, Imie, Liczba, Plec
df=pd.DataFrame(a,columns=['Rok','Imie','Liczba','Plec'])
print(df)