# Zad 3f
# gotowe
# cd wd_cw08_30-04-2020/
import pandas as pd
# import xlrd
# import openpyxl

df = pd.read_csv('zamowienia.csv', delimiter=';') # columns=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg']
mask_2004 = df[(df['Data zamowienia'] >= '2004-01-01') & 
            (df['Data zamowienia'] <= '2004-12-31')]

mask_2005 = df[(df['Data zamowienia'] >= '2005-01-01') & 
            (df['Data zamowienia'] <= '2005-12-31')]

# df.to_csv('plik.csv', header=None, index=False)
mask_2004.to_csv('zamowienia_2004.csv', index=False)
mask_2005.to_csv('zamowienia_2005.csv', index=False)

# cat zamowienia_2004.csv   by sprawdzic
# cat zamowienia_2005.csv   by sprawdzic
