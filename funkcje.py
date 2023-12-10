def word_count(text):
    text = text.split()
    return len(text)


def no_of_unique_words(text):
    text = text.split()
    text = set(text)
    print(text)
    return len(text)


def clean_text(text):
    sign = ['.', ',', '(', ')', '"']
    for i in sign:
        text = text.replace(i, '')
    return text


def read_file(filename):
    with open(filename, 'r', encoding='utf8') as file1:
        content = file1.read()
    return content

def repeated_words(text):
    text = text.split()
    my_dict = {}
    temp_dict = {}
    for word in text:
        if word in my_dict.keys():
            my_dict[word] += 1
            if my_dict[word] / len(text) > 0.02 and word not in temp_dict.keys():
                print(f'słowo {word} występuje za często')
                temp_dict[word] = True
        else:
            my_dict[word] = 1
    return my_dict

