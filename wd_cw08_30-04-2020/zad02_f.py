# Zad 2f
# niegotowe
# cd wd_cw08_30-04-2020/
import numpy as np
import pandas as pd
import xlrd
import openpyxl

x = pd.read_excel('imiona.xlsx')    # Rok, Imie, Liczba, Plec
df = pd.DataFrame(x,columns=['Rok','Imie','Liczba','Plec'])

# gr_plec = df.groupby(['Plec'])
# gr_liczba = df.groupby(['Liczba'])
# gr_rok = df.groupby(['Rok'])
# a = df.loc[[0,1], ['Liczba']] 
# # print(a)
# # print(df.inc.sort_values(by=['Liczba','Rok'],ascending=[False,True]), a) 
# print(df)
mask = df.groupby(['Rok']).agg('idxmax')
a = df.loc[(df['Liczba'] == np.max), 'Imie']
print(mask)





