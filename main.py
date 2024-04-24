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

#sumę wszystkich urodzonych dzieci w całym danym okresie,

suma = df['Liczba'].sum()
print(suma)

#sumę dzieci urodzonych w latach 2000-2005

przedzial = df[(df['Rok']<=2005) & (df['Rok']>=2000)]
suma2 = przedzial['Liczba'].sum()
print(suma2)

#sumę urodzonych chłopców i dziewczynek,

chlopcy = df[df['Plec']=='M']
sum_chlopcy = chlopcy['Liczba'].sum()
print(sum_chlopcy)

dziewczynki = df[df['Plec']=='K']
sum_dziewczynki = dziewczynki['Liczba'].sum()
print(sum_dziewczynki)

#najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),

for rok in range(2000,2018,1):
    dziewczynkirok = dziewczynki[dziewczynki['Rok'] == rok]
    sortd=dziewczynkirok.sort_values(by='Liczba', ascending=False)
    popd=sortd.iloc[0]
    print(popd)

    chlopcyrok = chlopcy[chlopcy['Rok'] == rok]
    sortc = chlopcyrok.sort_values(by='Liczba', ascending=False)
    popc = sortc.iloc[0]
    print(popc)

#najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,


a = dziewczynki.groupby(['Imie']).agg({'Liczba':['sum']})

sortdz=a.sort_values(by=('Liczba','sum'), ascending=False)

print(sortdz.iloc[0])

b = chlopcy.groupby(['Imie']).agg({'Liczba':['sum']})

sortch=b.sort_values(by=('Liczba','sum'), ascending=False)

print(sortch.iloc[0])

####