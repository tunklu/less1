immutable_var = (1, 2, 'a', 'b')

print("Immutable tuple:", immutable_var)

try:
    immutable_var[3] = 2
except TypeError as exc:
    print(exc, 'Кортеж является неизменяемым (immutable) типом.')

mutable_list = [1, 2, 'a', 'b']

mutable_list[2] = 'Modified'
mutable_list.append('new_elem')

print("Mutable list:", mutable_list)