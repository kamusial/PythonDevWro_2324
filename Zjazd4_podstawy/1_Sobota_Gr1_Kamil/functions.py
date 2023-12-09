def no_of_words(text):
    text = text.split()
    return len(text)

def no_of_unique_words(text):
    text = text.split()
    text = set(text)
    print(text)
    return len(text)

def clear_text(text):
    character = ['.', ',', '(', ')', '"']
    for char in character:
        text = text.replace(char, '')
    return text