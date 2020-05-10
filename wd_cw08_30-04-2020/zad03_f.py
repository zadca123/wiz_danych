# Zad 3f
# gotowe
# cd wd_cw08_30-04-2020/
import pandas as pd
# import xlrd
# import openpyxl

df = pd.read_csv('zamowienia.csv', delimiter=';') # columns=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg']
mask = df[(df['Data zamowienia'] >= '2004-01-01') & 
            (df['Data zamowienia'] <= '2004-12-31')]
print(mask.median())
