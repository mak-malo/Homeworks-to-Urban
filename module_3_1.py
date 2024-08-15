count_calls_functions = 0
#________________________________________________________________________________________
def count_calls_up ():
    global coucount_calls_functions
    count_calls_functions = count_calls_functions + 2 
    # Раз для увечиления числа на счетчике вызова функций 
    # я вызываю функцию, то прибавляю сразу 2 - за основную функцию и за count_calls_up
#________________________________________________________________________________________


def count_calls():
    global count_calls_functions
    calls = count_calls_functions 
    # переадресация переменной здесь для того, чтобы при вызове этой функции счетчик вызовов
    # учитывал сам вызов этой функции, но при этом возвращал значение счетчика до вызова count_calls
#_____________________________________
    count_calls_up()
#_____________________________________
    return calls

def string_info(work_str):
    count_calls_up()
    info_tuple = len(work_str), work_str.upper(), work_str.lower()
    return info_tuple

def is_contains(find_str, main_list):
    count_calls_up()
    for i in main_list:
        if i.lower() == find_str.lower():
            return True
    return False


print(string_info('University'))
print(string_info('Ussr'))
print(is_contains('watermelon', ['potato', 'CaRRoT', 'egg', 'sausage', 'cucumber', 'salt', 'meat'])) # В окрошке нет арбуза
print(is_contains('SamaRA', ['Moscow', 'VoroNej', 'SAMAra', 'Magadan', 'etc'])) # Самара - это российский город
print(count_calls())
