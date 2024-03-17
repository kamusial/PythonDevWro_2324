import matplotlib.pyplot as plt
import numpy as np
from numpy.random import seed
import pandas as pd
from sklearn.datasets import load_breast_cancer  #, load_wine
from sklearn.neural_network import MLPClassifier
from collections import Counter

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