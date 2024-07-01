year = 2024
immutable_var = year, 'Loading...', 2025
print(immutable_var)
year = 2020
print('После изменения переменной year:', immutable_var, sep = '\n')
immutable_var = immutable_var + (2, 2.6, 'Any programing')
print(immutable_var)

#immutable_var[2] = 2021
'''Первый элемент кортежа - переменную - не получилось изменить,
так как ссылка в кортеже уже настроена на значение, указанное
перед объявлением кортежа. Изменить третий элемент через индекс
элемента не получилось, так как ссылка настроена на конретное число
и её невозможно изменить на другую ячейку памяти'''

mutable_list = [2, '158', input('\nЧто-нибудь в список: '), False]
print(mutable_list)
mutable_list = mutable_list + 'second list'.split(' ')
print(mutable_list)
