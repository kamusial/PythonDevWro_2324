#program, który sprawdzi, czy dane wyrażenie (słowo bądź zdanie) jest palindromem
list_of_sentences = []
sentence = input('Podaj wyrazenie: ')
list_of_sentences.append(sentence)
max_length = len(sentence)
while True:
    print(f'wprowadzono: {sentence}')
    # sentence = sentence.replace(' ','')
    # sentence = sentence.replace('.','')
    # sentence = sentence.replace(',','')
    # sentence = sentence.lower()
    tmp_sentence = sentence.replace(' ','').replace('.','').replace(',','')
    if tmp_sentence.lower() == tmp_sentence[::-1].lower():
        print(f'tak, wyrazenie {sentence} jest palindromem')
    else:
        print(f'nie, to nie jest palindrom')
    decision = input('Czy chcesz sprawdzic kolejne slowo? T/N')
    if decision.lower() == 't':
        sentence = input('Podaj kolejne wyrazenie: ')
        list_of_sentences.append(sentence)
        if len(sentence) > max_length:
            max_length = len(sentence)
    else:
        break

print(f'statystyki:')
print(f'liczba sprawdzonych slow: {len(list_of_sentences)},\nnajdlusze ma: {max_length} znakow')

