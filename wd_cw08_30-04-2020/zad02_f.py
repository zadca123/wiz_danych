# Zad 2f
# niegotowe
# cd wd_cw08_30-04-2020/
import numpy as np
import pandas as pd
import xlrd
import openpyxl

x = pd.read_excel('imiona.xlsx')    # Rok, Imie, Liczba, Plec
df = pd.DataFrame(x,columns=['Rok','Imie','Liczba','Plec'])
mask_d = df[df['Plec'] == 'K']
mask_c = df[df['Plec'] == 'M']
mask2_d = mask_d.sort_values(by='Liczba', ascending=False)
mask2_c = mask_c.sort_values(by='Liczba', ascending=False)

print('Urodzenia chlopcow','\n',mask2_c.groupby(['Rok']).agg({'Liczba':['sum']}))
print('\n')
print('Urodzenia dziewczynek','\n',mask2_d.groupby(['Rok']).agg({'Liczba':['sum']}))