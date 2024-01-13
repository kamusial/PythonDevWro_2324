import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

df = pd.read_csv('diabetes.csv')
print(df.head(5).to_string())
print(df.describe().T.to_string())
print(df.isna().sum())   # puste wartości
print(df.outcome.value_counts())

for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin', 'bmi', 'diabetespedigreefunction', 'age']:
    df[col].replace(0, np.NaN, inplace=True)
    mean_ = df[col].mean()
    df[col].replace(np.NaN, mean_, inplace=True)

print(df.isna().sum())
print(df.describe().T.to_string())
