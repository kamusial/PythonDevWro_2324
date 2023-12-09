def no_of_words(text):
    text = text.split()
    return len(text)

def no_of_unique_words(text):
    text = text.split()
    text = set(text)
    print(text)
    return len(text)

def clear_text(text):
    character = set('.,(\'\"')
    for char in character:
        text = text.replace(char, '')
    return text

def read_file(filename):
    with open(filename, 'r', encoding='utf8') as file1:
        content = file1.read()
    return content

def words_repeat(text):
    text = text.split()
    my_dict = {}
    for word in text:
        if word in my_dict.keys():
            my_dict[word] += 1
        else:
            my_dict[word] = 1