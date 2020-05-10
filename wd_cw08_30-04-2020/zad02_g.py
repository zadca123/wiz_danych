# Zad 2g
# gotowe
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

print(mask2_d[0:1],'\n', mask2_c[0:1])