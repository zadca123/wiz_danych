# Zad 3b
# gotowe
# cd wd_cw08_30-04-2020/
import pandas as pd
# import xlrd
# import openpyxl

df = pd.read_csv('zamowienia.csv', delimiter=';') # columns=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg']

mask = df.sort_values(by='Utarg',ascending=False)
mask2 = mask['Utarg']
print(mask2[0:5])
