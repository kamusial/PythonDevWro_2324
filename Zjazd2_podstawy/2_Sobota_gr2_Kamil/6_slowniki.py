sample_dict = {'Kamil': 15, 'Marlena': 302, 'Marta': 302, 'Marek': 2}
price_dict = {'marchew': 7.2, 'majonez': 4.32, 'chleb': 4.32, 'marchew': 13.2}

print(price_dict)

colors_of_products = {'kawa': 'black', 'herbata': 'green', 'chleb': 'black'}

print(f'cena marchwi to: {price_dict["marchew"]}')
price_dict['marchew'] = 1.99
price_dict['koperek'] = 2.99
print(price_dict)

x = list(price_dict.keys())
print(x[2])
print(price_dict['marchew'] + price_dict['koperek'])

my_list = [price_dict, colors_of_products, 4, 'mama', [1, 2.3, 'piesek']]
print(my_list[1]['kawa'])