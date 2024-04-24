import pandas as pd
import numpy as np
#zad1
xlsx = pd.ExcelFile('imiona.xlsx')

df = pd.read_excel(xlsx, header=0)

#print(df)

#zad2
#Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):

#tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku

print(df[df['Liczba']>1000])

#tylko rekordy gdzie nadane imię jest takie jak Twoje

print(df[df['Imie']=='DENIS'])

