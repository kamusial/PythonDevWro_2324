import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.svm import SVC  #clasifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('heart.csv', comment='#')
print(df)

print(df.target.value_counts())

X = df.iloc[:, :-1]  # wszystkie kolumny, bez ostatniej
y = df.target  # kolumna target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print('\Regresja logistyczna')
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('\KNN')
model = KNeighborsClassifier(n_neighbors=30, weights='distance')
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('\Drzewo decyzyjne')
model = DecisionTreeClassifier(max_depth=8, min_samples_split=5)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('\nLas losowy')
model = RandomForestClassifier(n_estimators=100, max_depth=9)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test)) ))

print('\SVM')
model = SVC(kernel='rbf', degree=5)
# kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable, default=’rbf’
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))
