import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('diabetes.csv')
print(df.shape)
print(df.describe().T.to_string())  #ile pustych pól
print(f'klasy: {df["outcome"].value_counts()}')   # czy klasy zbalansowane
print(df.isna().sum())   #ile pustych pol

# tam, gdzie 0 bądź brak wartości -> zamień na średnią wartość


for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin',
       'bmi', 'diabetespedigreefunction', 'age']:
    df[col].replace(0, np.NaN, inplace=True)
    mean_ = df[col].mean()
    df[col].replace(np.NaN, mean_, inplace=True)

print(f'Po obroce:\n{df.isna().sum()}')  # ile pustych pol

df.to_csv('cukrzyca.csv', sep=';', index=False)

X = df.iloc[:, :-1]   #wszystkie kolumny bez ostatniej
y = df.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train) # nauka na 80% danych
print(model.score(X_test, y_test)) # sprawdź model na danych testowych
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('Zmiana danych')
df1 = df.query('outcome==0').sample(n=500)  #wybierz 500 zdrowych
df2 = df.query('outcome==1').sample(n=500)  #wybierz 500 chorych
df3 = pd.concat([df1, df2])

X = df3.iloc[:, :-1]
y = df3.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))