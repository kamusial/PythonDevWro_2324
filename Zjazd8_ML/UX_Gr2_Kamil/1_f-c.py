import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.random import set_seed

set_seed(0)

model = Sequential()
model.add(Dense(1, activation='relu'))  # warstwa wejściowa
model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='linear'))
model.add(Dense(1))  # warstwa wyjściowa

model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

df = pd.read_csv('f-c.csv', usecols=[1, 2])
print(df.head())
plt.scatter(df.F, df.C)
plt.show()

result = model.fit(df.F, df.C, epochs=1000, verbose=2)
print(f'\n{result.history}')  # funkcja straty

df1 = pd.DataFrame(result.history)
print(df1)
df1.plot()
plt.show()

C_pred = model.predict(df.F)
plt.scatter(df.F, df.C)
plt.plot(df.F, C_pred, c='r')
plt.show()

model.save('My_model.keras')   # zapisanie modelu
new_model = tf.keras.models.load_model('My_model.keras')   # załadowanie modelu
C_pred = new_model.predict(df.F)
plt.scatter(df.F, df.C)
plt.plot(df.F, C_pred, c='r')
plt.show()
