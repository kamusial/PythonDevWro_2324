import matplotlib.pyplot as plt
import numpy as np
from numpy.random import seed
import pandas as pd
from sklearn.datasets import load_breast_cancer  #, load_wine
from sklearn.neural_network import MLPClassifier
from collections import Counter
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold
from sklearn.metrics import accuracy_score

################ Pandas - settings
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 10000)
pd.set_option('display.max_colwidth', 10000)
np.set_printoptions(linewidth=2000)

################ Cancer - analiza danych
X, y = load_breast_cancer(return_X_y=True, as_frame=True)
print(X.shape)
print(X.columns)
print(X.describe())
print(Counter(y))  # zlicz


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=100, activation='relu')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(model.n_layers_)
