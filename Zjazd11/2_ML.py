import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

df = pd.read_csv('dane.csv', comment='#')
print(df.head().to_string())
print(df.target.value_counts())

X = df.iloc[:, :-1]
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print('\Part1 pojedyncze algorytmy')
print('\nLogistic Regression')
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('\nKNN')
model = KNeighborsClassifier()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

results1 = []
for k in range(1, 50):
    model = KNeighborsClassifier(n_neighbors=k) # , weights='distance')
    model.fit(X_train, y_train)
    results1.append(model.score(X_test, y_test))

plt.title('KNN')
plt.plot(range(1, 50), results1)
plt.show()

results2 = []
for k in range(1, 50):
    model = KNeighborsClassifier(n_neighbors=k, weights='distance')
    model.fit(X_train, y_train)
    results2.append(model.score(X_test, y_test))

plt.title('KNN - distance')
plt.plot(range(1, 50), results2)
plt.show()


print('\nDrzewo decyzyjne')
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

results = []
for k in range(1, 20):
    model = DecisionTreeClassifier(max_depth=k)
    model.fit(X_train, y_train)
    results.append(model.score(X_test, y_test))

plt.title('Tree')
# plt.scatter(x=range(1, 20), y=results) # wykres punktowy
plt.plot(range(1, 20), results, 'b')   # linia ciągła
plt.show()

print('\nSVC')
model = SVC()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

results = []
for kernel in ['linear', 'poly', 'rbf', 'sigmoid']:
    model = SVC(kernel=kernel)
    model.fit(X_train, y_train)
    results.append(model.score(X_test, y_test))

plt.title('SVN - kernels')
plt.scatter(x=range(1, 5), y=results) # wykres punktowy
# plt.plot(range(1, 5), results, 'b')   # linia ciągła
plt.show()

results = []
for degree in range (1, 10):
    model = SVC(kernel='poly', degree=degree)
    model.fit(X_train, y_train)
    results.append(model.score(X_test, y_test))

plt.title('SVN - poly, degree')
# plt.scatter(x=range(1, 10), y=results) # wykres punktowy
plt.plot(range(1, 10), results, 'b')   # linia ciągła
plt.show()

print('Part2 siatka parametrów')

print('\n Logistyczna regresja')
model = LogisticRegression()
params = {
    'penalty': ['None', 'l1', 'l2', 'elasticnet']
}
grid = GridSearchCV(model, params, scoring='accuracy', cv=10, verbose=1)
grid.fit(X_train, y_train)
print(grid.best_params_)
print(grid.best_score_)

print('\nKNN')
model = KNeighborsClassifier()
params = {
    'n_neighbors': range(5, 50, 3),
    'weights': ['uniform', 'distance']
}
grid = GridSearchCV(model, params, scoring="accuracy", cv=10, verbose=1)
grid.fit(X_train, y_train)
print(grid.best_params_)
print(grid.best_score_)

print('\nDrzewo decyzyjne')
model = DecisionTreeClassifier()
params = {
    'max_depth': range(3, 14),
    'max_features': range(3, X_train.shape[1]+1),
    'min_samples_split': [2, 3, 4, 5],
    'criterion': ['gini', 'entropy', 'log_loss']
}
grid = GridSearchCV(model, params, scoring="accuracy", cv=10, verbose=1)
grid.fit(X_train, y_train)
print(grid.best_params_)
print(grid.best_score_)

print('\nSVC')
model = SVC()
params = {
    'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
    'degree': range(2, 10),
}
grid = GridSearchCV(model, params, scoring="accuracy", cv=10, verbose=1)
grid.fit(X_train, y_train)
print(grid.best_params_)
print(grid.best_score_)