import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('otodom.csv')
print(df.head(3).to_string())
print('Describe')
print(df.describe().to_string())   # T - zamiana wierszy z kolumnami

# print(df.iloc[ 5:15 , 1:3 ])  # wiersz, kolumna

# print(df.iloc[:, 1:].corr())    #wycieta pierwsza kolumna


sns.heatmap(df.iloc[:, 1:].corr(), annot=True)
plt.show()

q1 = df.describe().loc['25%', 'cena']   #wycągnięcie danej komórki
q3 = df.describe().loc['75%', 'cena']
df = df[(df.cena <= q3)]  # najdroższe mieszknaia

sns.histplot(df.cena)
plt.show()

# algorytm - dane testowe i treningowe

X = df.iloc[:, 2:]   #wszystkie kolumny bez ID i bez ceny
y = df.cena
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
model = LinearRegression()
model.fit(X_train, y_train) # nauka na 80% danych
print(model.score(X_test, y_test)) # sprawdź model na danych testowych

print(pd.DataFrame(model.coef_, X.columns))

