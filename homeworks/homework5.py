print('Работа со списками.')
my_list = ['Blackberry', 'Raspberry', 'Cranberry', 'Cherry', 'Strawberry']
print('List:', my_list)
print('First:', my_list[0])
print('Last:', my_list[-1])
print('Sublist 3-5:', my_list[2:5])
my_list[2] = 'Cowberry'
print('Modified list:', my_list)
print('Работа со словарями.')
my_dict = {'Blackberry': 'Ежевика' , 'Raspberry': 'Малина', 'Cranberry': 'Клюква', 'Cherry': 'Вишня', 'Strawberry': 'Клубника'}
print('Dictionary:', my_dict)
print('Translation:', my_dict.get('Cherry'))
my_dict['Strawberry'] = 'Земляника'
print('Modified dictionary: ', my_dict)
