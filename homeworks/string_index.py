
example = 'Топинамбур'
print(example[0])
print(example[-1])
length = int(len(example)/2)

example_char = ''
for char in range(length, len(example), 1):
    example_char += example[char]
print(example_char)

example_char = ''
for char in range((len(example)-1), -1, -1):
    example_char += example[char]
print(example_char)

example_char = ''
for char in range(1, (len(example)), 2):
    example_char += example[char]
print(example_char)