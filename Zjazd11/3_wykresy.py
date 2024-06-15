#Wykres słupkowy

import matplotlib.pyplot as plt
import random

imiona = ['Ania', 'Kamil', 'Mariusz', 'Basia', 'Aga']
wiek = [random.randint(18, 70) for imie in imiona]

plt.bar(imiona, wiek, color=['red', 'green', 'blue'])
plt.xticks(imiona)
plt.yticks(wiek)
plt.show()


#wykres kołowy
wydatki = ['mieszkanie',  'media', 'jedzenie', 'rozrywka', 'nauka', 'inwestycje']
wartosci = [3000, 300, 800, 200, 400, 1000]
wysun = [0 for i in wydatki]
wysun[wydatki.index('media')] = 0.4
wysun[wydatki.index('nauka')] = 0.2

plt.pie(wartosci, labels=wydatki, explode=wysun, shadow=True)
plt.show()

#2 wykresy sąsiadujące poziomo
import math

X = [x for x in range(0, 720+1, 10)]
Y1 = [ math.cos(math.radians(i))                                for i in X]
Y2 = [random.random() for i in X]

plt.subplot(1, 3, 1)   #poziomy, piony, index
plt.plot(X, Y1, 'r.-')
plt.subplot(1, 3, 2)   #poziomy, piony, index
plt.plot(X, Y2, 'bs:')
plt.subplot(1, 3, 3)   #poziomy, piony, index
plt.plot(X, Y1, 'r.-')
plt.subplot(1, 3, 3)   #poziomy, piony, index
plt.plot(X, Y2, 'bs:')
plt.show()