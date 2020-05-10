# Zad 2d
# gotowe
# cd wd_cw08_30-04-2020/
import pandas as pd
import xlrd
import openpyxl

x = pd.read_excel('imiona.xlsx')    # Rok, Imie, Liczba, Plec
df = pd.DataFrame(x,columns=['Rok','Imie','Liczba','Plec'])
mask = df[df['Rok'] <= 2005]
mask2 = mask.agg({'Liczba':['sum']})
print(mask2)