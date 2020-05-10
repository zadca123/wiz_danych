# Zad 2g
# niegotowe
# cd wd_cw08_30-04-2020/
import numpy as np
import pandas as pd
import xlrd
import openpyxl

x = pd.read_excel('imiona.xlsx')    # Rok, Imie, Liczba, Plec
df = pd.DataFrame(x,columns=['Rok','Imie','Liczba','Plec'])

mask = df.groupby(['Imie']).agg({'Liczba':['sum']})
a = df.loc[(df['Liczba'] == np.max), 'Imie']
gr_imie = df.groupby('Imie')

# print(df.[gr_imie])
# print(mask.sort_values(by='Liczba'),ascending=False)





