# i = 1
# while i < 6:
#     print(i)
#     i = i + 1
#
#
# standard_password = '123'
# user_password = input('Podaj hasło: ')
#
# while standard_password != user_password:
#     user_password = input('Zle haslo, jeszcze raz: ')
#
# print('Hasło poprawne, start programu, dostęp do danych')


# program, który wpuszcza tylko pełnoletnich użytkowników
min_age = 18
user_age = int(input('Podaj wiek: '))

while user_age < min_age:
    user_age = int(input('Jeszcze raz, podaj wiek: '))
    print('na mocy przepisów .......  musimy potwierdzić że masz minimum 18 lat')
print('wiek zweryfikowany, zapraszamy')
