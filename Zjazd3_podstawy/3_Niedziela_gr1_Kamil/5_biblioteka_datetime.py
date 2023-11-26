import datetime

# wyciągnięcie daty i godziny
now = datetime.datetime.now()
print(now)
print(type(now))
# tworzenie napisu z aktualną datą i godziną
date1 = now.strftime('Dzisiaj jest %d/%m/%Y. Godzina %H:%M')
print(date1)
filename = now.strftime('result_%H%M%S')
print(filename)

# now = str(now)
# hour = now[11:13]
# print(hour)
# minute = now[14:16]
# print(minute)
# print('godzina jest ' + hour + '.' + minute)