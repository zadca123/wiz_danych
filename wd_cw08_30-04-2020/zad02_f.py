# Zad 2d
# niegotowe
# cd wd_cw08_30-04-2020/
import pandas as pd
import xlrd
import openpyxl

x = pd.read_excel('imiona.xlsx')    # Rok, Imie, Liczba, Plec

df = pd.DataFrame(x,columns=['Rok','Imie','Liczba','Plec'])

a = df[df['Imie'] == 'ADAM']
# print(a)
print(df.sort_values(by='Liczba',ascending=False)) 