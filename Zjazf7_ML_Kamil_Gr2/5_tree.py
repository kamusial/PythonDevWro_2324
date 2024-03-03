import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_decision_regions

df = pd.read_csv('iris.csv')
print(df['class'].value_counts())

species = {
    'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2
}
df['class_value'] = df['class'].map(species) #nowa kolumna z danymi numerycznymi
print(df['class_value'].value_counts())

sample = np.array([5.6, 3.2, 5.2, 1.45])

sns.scatterplot(data=df, x="sepallength", y="sepalwidth", hue='class')
plt.scatter(x=5.6, y=3.2, c='r')
plt.show()

sns.scatterplot(data=df, x="petallength", y="petalwidth", hue='class')
plt.scatter(x=5.2, y=1.45, c='r')
plt.show()

X = df.iloc[:,    :4   ]  # wszystkie wiersze i 2 kolumny - 2 cechy
y = df.class_value
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = DecisionTreeClassifier(max_depth=20, min_samples_split=20)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))
print(pd.DataFrame(model.feature_importances_, X.columns))  #które cechy najwazniejsze

# rysowanie granic decyzyjnych
# plot_decision_regions(X.values, y.values, model)
# plt.show()

# zapis i załadowanie modelu
# import joblib
# joblib.dump(model, 'moj_tree_classifier.model')  #zapis modelu do pliku
# model_new = joblib.load('moj_tree_classifier.model')  #wczytanie modelu
