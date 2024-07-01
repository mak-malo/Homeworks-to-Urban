my_string = input('Напишите произволььную строку: ')
print('В Вашей строке', len(my_string), 'символов')

print('\nВ нижнем регистре: ', my_string.lower(), '\n', sep = '')
print('В верхнем регистре: ', my_string.upper(), '\n', sep = '')
print('Без пробелов: ', my_string.replace(' ', ''), '\n', sep = '')
print('Первый символ строки: ', my_string[0], '\n', sep = '')
print('Последний символ строки: ', my_string[-1], '\n', sep = '')