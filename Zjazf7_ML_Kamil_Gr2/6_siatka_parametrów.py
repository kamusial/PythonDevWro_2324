import pandas
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from sklearn.model_selection import GridSearchCV

df = pd.read_csv('heart.csv', comment='#')
print(df)

print(df.target.value_counts())

X = df.iloc[:, :-1]  # wszystkie kolumny, bez ostatniej
y = df.target  # kolumna target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = DecisionTreeClassifier(max_depth=5, min_samples_split=2, max_features=4)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))
# print(pd.DataFrame(model.feature_importances_, X.columns))  #które cechy najwazniejsze

print(f'liczba cech {X.shape[1]}')

model = DecisionTreeClassifier()
params = {
    'max_depth': range(3, 14, 2),
    'max_features': range(3, X.shape[1]+1, 2),
    'min_samples_split': [2, 4, 5],
    'criterion': ['gini', 'entropy', 'log_loss']
}
grid = GridSearchCV(model, params, scoring='accuracy', cv=5, verbose=2)
grid.fit(X, y)
print(grid.best_params_)
print(grid.best_estimator_)
print(grid.best_score_)