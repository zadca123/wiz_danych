# Zad 2d
# niegotowe
# cd wd_cw08_30-04-2020/
import pandas as pd
import xlrd
import openpyxl

x = pd.read_excel('imiona.xlsx',delimiter=';')    # Rok, Imie, Liczba, Plec

df = pd.DataFrame(x,columns=['Rok','Imie','Liczba','Plec'])

# print(df.groupby(['Rok']).agg({'Liczba':['sum']}) & (df.where(['Rok' == '2005'])))
# print(df[(df['Rok'])])

# print(df.groupby(['Liczba']).agg({'Liczba':['sum']}))
# print(df[df[]])
# print(df[(df['Rok'] <= 2005) & (df['Imie'] == "ADAM")])
# print(df[(df['Rok'] <= 2005).agg({'Liczba': ['sum']})])


# print(df.groupby(['Liczba']).agg({'Liczba':['sum']}))
a = df['Rok'] <=2005
# b = df.groupby((['Rok']).agg({'Liczba':['sum']}))
c = df.groupby
print(df[a])