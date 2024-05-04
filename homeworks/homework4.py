immutable_var = 1, 2, 3, True, 3.144, 'OS'
print(immutable_var)
print(type(immutable_var))
print(immutable_var[2])
try:
    print('попытка переназначения элемента кортежа')
    immutable_var[2] = 1
except:
    print("TypeError: 'tuple' object does not support item assignment")
    print('Объект не поддержзивает назначение элементов.')
    print('Кортежи это неизменяемый объект.')

finally:
    print('Задание с кортежем закончено.')
print()
print('Задание 4. Список.')
mutable_list = ["This", "is", "list"]
mutable_list[1] = "is not"
print(mutable_list)
