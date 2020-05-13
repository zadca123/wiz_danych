# Zad 3
# gotowe
# cd wd_cw09_07-05-2020/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

x = pd.read_excel('imiona.xlsx')    # Rok, Imie, Liczba, Plec
df = pd.DataFrame(x,columns=['Rok','Imie','Liczba','Plec'])
print(df)

grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.pie(subplots=True, autopct='%0.2f %%', fontsize=20, figsize=(6, 6))
plt.title('ilosc urodzonych chłopców i dziewczynek w ostatnich 5 latach')
plt.show()

