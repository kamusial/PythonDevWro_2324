import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('weight-height.csv')
print(f'wyswietlam plik \n{df}')
print(f'typ pliku {type(df)}\n')
# print(df.head(10))   # wyswietl 10 pierwszych wierszy (domyslnie jest 5)

print('\n Licze ile mezczyzn i ile kobiet')
print(df.Gender.value_counts())   # policz ile razy dana wartosc

df.Height *= 2.54   #pomnoz wszystko z kolumny przez 2.54
df.Weight /= 2.2
print(df)

#zamiana gender na daną numeryczną
df = pd.get_dummies(df)
del (df['Gender_Male'])
print(df)
df = df.rename(columns={'Gender_Female':'Gender'})
print(df)
# 0, false   - facet      1, true 0 kobieta

