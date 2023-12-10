def my_function(a, b, c):
    if b > a:
        return b + c
    else:
        return a +c


print(my_function(3, 6, 10))

def my_arg_function(*args):
    print(args[2])
    for arg in args:
        if arg > 0:
            print(arg * 2)
        else:
            print(f'{arg} mniejsze od zera')

my_arg_function(3, 4, 5, -1, 2)


def my_kwargs_function(**kwargs):
    if kwargs['nazwisko'] == 'Kowalski':
        print(f'Jesteś na liście')


my_kwargs_function(imie= 'Kamil', nazwisko='Kowalski', status= 'wolny')


def draw_line(x, y, *coordinates):
    start = [x, y]
    for i in range(0, len(coordinates), 2):
        print(f'rysuję linię z {start} do {coordinates[i]},{coordinates[i+1]}')
        start = [coordinates[1], coordinates[i+1]]

def triangle(**data):
    if 'a' in data.keys() and 'b' in data.keys() and 'c' in data.keys():
        print('liczę podstawę z 3 boków')
    elif 'a' in data.keys() and 'b' in data.keys() and 'alpha' in data.keys():
        print('licze pole z dwóch boków i kąta')
    elif 'a' in data.keys() and 'alpha' in data.keys()and 'beta' in data.keys():
        print('liczę pole z jednego boku i dwóch kątów')
    elif 'a' in data.keys() and 'h' in data.keys():
        print('liczę pole z podstawy i wysokości')
    else:
        print('no nie da się')


triangle(a=5, b=14, alpha=90)

login_database = ['Gosia123', 'Matixx', 'Neo12345', 'Dixi']


def check_logins(*logins):
    available_login_list = []
    for login in logins:
        if login not in login_database:
            print(f'login {login} is available')
            available_login_list.append(login)
    return available_login_list

print(check_logins('Gosia', 'Stasiu', 'Matixx', 'Neo12345', 'Staxi'))


triangle()


def final_function(a, b, c):
    return a + b + c

print(final_function(2, 4, 10))


def final2(a, b, *rest):
    return True

print(final2('mama', 4, 17))


