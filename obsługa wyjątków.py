# słownik imion = {
#     'jan': 'john',
#     'Maria': 'Mary',
#     'Jacek': 'Jack'
# }

x = input('podaj liczby do dzielenia: ').split()

try:
    result = int(x[0]) / int(x[1])
except IndexError:
    result = int(x[0])
    print('Nieznana ścieżka pliku')
    raise #jak mamy raise to bład wyswietli się i tak mimo, że wskazalismy co robić
except ZeroDivisionError:
    result = 1
except ValueError:
    result = 0
else:
    print(f'udało się - tworze plik')
    print(f'wynik to: {result}')