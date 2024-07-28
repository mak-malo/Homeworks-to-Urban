'''Интересный занавес программы'''
def plus_item (item):  # Вспомогательная функция для прибавления очередного числа/строки
    global total_sum
    if type(item) == str:
        total_sum += len(item)
    elif type(item) == int or type(item) == float:
        total_sum += item
    elif type(item) == list or type(item) == set or type(item) == tuple:
        summator_in_list_set_tuple(item)
    elif type(item) == dict:
        summator_in_dict(item)

def summator_in_list_set_tuple(list): #Функция для суммирования элементов в Списках, Множествах и Кортежах
    for item in list:
        plus_item(item)

def summator_in_dict(dict): #Функция для суммирования ключей и значений в солварях
    for key in dict:
        plus_item(key)
        plus_item(dict[key])

def interesting_summator (*structure): # Функция для загрузки рабочей структуры в работу
    global total_sum
    for item in structure:
        plus_item(item)
    print('Итоговая сумма равна:', total_sum)

'''Рабочая часть программы'''

total_sum = 0

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

interesting_summator(data_structure)

