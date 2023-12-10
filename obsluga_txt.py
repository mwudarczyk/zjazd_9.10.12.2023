

from funkcje import *


# print(f'number of WORDS: {word_count(content)}')
# print(f'unique words:  {no_of_unique_words(content)}')
# my_string = 'Mama.kupiła.psa'
# print('\nusuwanie znaków')


content = read_file('canine.txt')
content = clean_text(content)
print(f'string po usunięciu:  {content}\n')

print(f'liczb roznych slow:   {no_of_unique_words(content)}')

print(f'check the words repeated:  {repeated_words(content)}')



