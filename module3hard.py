'''Интересный занавес программы'''
def plus_item (item):  # Вспомогательная функция для прибавления очередного числа/строки
    global total_sum
    if type(item) == str:
        total_sum += len(item)
    elif type(item) == int or type(item) == float:
        total_sum += item
    elif type(item) == list:
        summator_in_list(item)
    elif type(item) == dict:
        summator_in_dict(item)
    elif type(item) == set:
        summator_in_set(item)
    elif type(item) == tuple:
        summator_in_tuple(item)

def summator_in_list(list):
    for item in list:
        plus_item(item)

def summator_in_dict(dict):
    for key in dict:
        plus_item(key)
        plus_item(dict[key])

def summator_in_set(set):
    for item in set:
        plus_item(item)

def summator_in_tuple(tuple):
    for item in tuple:
        plus_item(item)

def interesting_summator (*structure): # Функция для загрузки рабочей структуры в работу
    global total_sum
    for item in structure:
        plus_item(item)
    print('Итоговая сумма равна:', total_sum)

'''Рабочая часть программы'''


total_sum = 0

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

interesting_summator(data_structure)

