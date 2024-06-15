from scipy import stats
import random
import matplotlib.pyplot as plt

X = list(range(10))
Y = [2*x + 1 + random.choice([1, -1]) * random.random() for x in X]

a, b, r_value, p_value, std_err = stats.linregress(X, Y)
Yreg = [a*x + b for x in X]

plt.plot(X, Y, 'ro')
plt.plot(X, Yreg, 'b--')

plt.show()

