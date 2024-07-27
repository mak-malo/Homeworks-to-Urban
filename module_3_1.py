count_calls_functions = 0

def count_calls():
    global count_calls_functions
    calls = count_calls_functions
    return calls

def string_info(work_str):
    global count_calls_functions
    count_calls_functions += 1
    info_tuple = len(work_str), work_str.upper(), work_str.lower()
    return info_tuple

def is_contains(find_str, main_list):
    global count_calls_functions
    count_calls_functions += 1
    for i in main_list:
        if i.lower() == find_str.lower():
            return True
    return False


print(string_info('University'))
print(string_info('Ussr'))
print(is_contains('watermelon', ['potato', 'CaRRoT', 'egg', 'sausage', 'cucumber', 'salt', 'meat'])) # В окрошке нет арбуза
print(is_contains('SamaRA', ['Moscow', 'VoroNej', 'SAMAra', 'Magadan', 'etc'])) # Самара - это российский город
print(count_calls())