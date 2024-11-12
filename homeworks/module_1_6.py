my_dict = {'William' : 1999, 'Jacob' : 2000}
print ('Dict: ', my_dict)

print ('Existing value: ', my_dict['William'])

print ('Not existing value: ', my_dict.get('Brandon'))

my_dict.update ({'Austin' : 2001, 'Christopher' : 2002})

a = my_dict.pop('Jacob')
print ('Deleted value: ', a)
print ('Modified dictionary: ', my_dict)
print()

my_set = {1, 2, 3, 'a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c'}
print ('Set: ', my_set)

my_set.add(4.3)
my_set.add((5, 6, 1.6))

my_set.remove(1)
print ('Modified set: ', my_set)