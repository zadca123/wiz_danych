# Zad 3e
# gotowe
# cd wd_cw08_30-04-2020/
import pandas as pd
# import xlrd
# import openpyxl

df = pd.read_csv('zamowienia.csv', delimiter=';') # columns=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg']
# mask = df[(df['Kraj']) == 'Polska' ]
mask2 = df[(df['Data zamowienia'] >= '2005-01-01') 
            & (df['Data zamowienia'] <= '2005-12-31') 
            & (df['Kraj'] == 'Polska')]
print(mask2)