# Zad 3d
# gotowe
# cd wd_cw08_30-04-2020/
import pandas as pd
# import xlrd
# import openpyxl

df = pd.read_csv('zamowienia.csv', delimiter=';') # columns=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg']
mask = df.groupby(['Kraj']).agg({'idZamowienia':['count']})
print(mask)

# mask2 = df.sort_values(by='Sprzedawca')
# mask3 = df.loc[0:4, mask['Sprzedawca']]

# print(df.sort_values(by=['Sprzedawca']))
# # print(df.inc.sort_values(by=['Liczba','Rok'],ascending=[False,True]), a) 
# df = pd.DataFrame(x,columns=['Rok','Imie','Liczba','Plec'])
# print(df)