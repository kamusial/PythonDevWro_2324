import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')
print(type(penguins))
print(penguins.head().to_string())

penguins_filtered = penguins.dropna().drop(columns=['island', 'sex'])
print(penguins_filtered.head().to_string())

penguins_features = penguins_filtered.drop(columns='species')
target = pd.get_dummies(penguins_filtered['species'])
print(target)

from sklearn.model_selection import train_test_split
from tensorflow import keras
from numpy.random import seed
seed(1)
from tensorflow.random import set_seed
set_seed(2)

X_train, X_test, y_train, y_test = train_test_split(penguins_features, target, test_size=0.2)

inputs = keras.Input(X_train.shape[1])
hidden_layer1 = keras.layers.Dense(4, activation='relu')(inputs)
hidden_layer2 = keras.layers.Dense(4, activation='relu')(hidden_layer1)
output_layer = keras.layers.Dense(3, activation='softmax')(hidden_layer2)

model = keras.Model(inputs=inputs, outputs=output_layer)
# print(model.summary())

model.compile(optimizer="rmsprop", loss=keras.losses.categorical_crossentropy)
result = model.fit(X_train, y_train, epochs=100)
sns.lineplot(x=result.epoch, y=result.history['loss'])
plt.show()

y_pred = model.predict(X_test)
prediction = pd.DataFrame(y_pred, columns=target.columns)
predicted_species = prediction.idxmax(axis='columns')
print(predicted_species)

from sklearn.metrics import confusion_matrix
true_species = y_test.idxmax(axis='columns')
matrix = confusion_matrix(true_species, predicted_species)
print(matrix)