# Zad 1
# gotowe
# cd wd_cw08_30-04-2020/
import pandas as pd
import xlrd
import openpyxl

a = pd.read_excel('imiona.xlsx')    # Rok, Imie, Liczba, Plec
df=pd.DataFrame(a,columns=['Rok','Imie','Liczba','Plec'])
print(df)