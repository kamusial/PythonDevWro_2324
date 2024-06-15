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

