# Zad 3a
# niegotowe
# cd wd_cw08_30-04-2020/
import pandas as pd
# import xlrd
# import openpyxl

df = pd.read_csv('zamowienia.csv', header=None, nrows=2)
print(df)
df.to_csv('zamowienia.csv', header=None, index=False)
# print(df)

# df = pd.DataFrame(x,columns=['Rok','Imie','Liczba','Plec'])
# print(df)