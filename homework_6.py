my_dict = {'Language': 'Python', 'year': 2024, 'alive?': True}
print('--Начальная версия словаря:', my_dict, sep = '\n')
print('--Значение по ключу "year":', my_dict['year'], sep = '\n')

my_dict.update({'all lessons': 235, 'little dream': (43.345068, 42.465897)})

del_value = my_dict.pop('Language')
print('--Вызов занчение по удаленному ключу:', my_dict.get('Language'), sep = '\n')
print('--Удаленное значение:', del_value, sep = '\n')
print('--Словарь после удаления:', my_dict, sep = '\n')


print('\n----------------------------------------------------------\n')


my_set = {'know', True, 6172, ('bool', 'ball', 'Bill'), 6172, 'I know', True}
print('--Множество:', my_set, sep = '\n')
for item in [51, 'look',True]:
    my_set.add(item)
print('--Множество с добавленными значениями:', my_set, sep = '\n')
my_set.remove(6172)
print('--Множество после удаления элемента 6172:', my_set, sep = '\n')
