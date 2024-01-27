import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')
print(type(penguins))
print(penguins.head().to_string())

sns.pairplot(penguins, hue='species')
plt.show()