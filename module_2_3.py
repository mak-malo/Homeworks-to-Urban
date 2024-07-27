my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] # Для проверки кода меняйте исходные данные
index_my_list = 0
while index_my_list < len(my_list):
    if my_list[index_my_list] > 0:
        print(my_list[index_my_list])
    elif my_list[index_my_list] < 0:
        break
    index_my_list += 1