import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv("iris.csv")
print(df["class"].value_counts())

species = {
    "Iris-setosa":0, "Iris-versicolor":1, "Iris-virginica":2
}
df["class_value"] = df["class"].map(species)

#X = df[ ["sepallength", "sepalwidth"] ]   #słabe cechy
#X = df[ ["petallength", "petalwidth"] ]    #dobre cechy
X = df.iloc[:, :4]    # wszystkie cechy
y = df.class_value
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

model = RandomForestClassifier(n_estimators=100, max_depth=5)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test)) ))


# zapis i załadowanie modelu
import joblib
# joblib.dump(model, 'moj_tree_classifier.model')  #zapis modelu do pliku
model_new = joblib.load('moj_tree_classifier.model')  #wczytanie modelu
print(X_test)
print(X_test.iloc[[4],:])   # wybieram jeden wiersz
print(model_new.predict(X_test.iloc[[4],:]))  # liczę
