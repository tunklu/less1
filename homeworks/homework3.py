my_string = input()

print('Строка верхний регистр: ', my_string.upper())

print('Строка нижний регистр: ', my_string.lower())

print('Метод удаления пробелов стиль Python: ')
print((''.join(my_string.split())))

print('Метод удаления пробелов 2: ')
stripless_string = ''
for i in my_string:
    if i != ' ':
        stripless_string += i
print(stripless_string)

print('Метод удаления пробелов 3: ')
stripless_string = ''
symbol_ = ''
i = 0
while i < len(my_string):
    if my_string[i] == ' ':
        symbol_ = ''
    else:
        symbol_ = my_string[i]
    stripless_string = stripless_string + symbol_
    i = i + 1
print(stripless_string)

print('Первый элемент: ', my_string[0])

print('Последний элемент стиль Python: ', my_string[-1])

print('Последний элемент классический: ', my_string[len(my_string)-1])
