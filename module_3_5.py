def get_multiplied_digits(number):
    #Первое решение
    '''product = 1
    for i in range(len(str(number))):
        if int(number % 10) != 0:
            product *= int(number % 10)
        number /= 10
    return (product)'''

    #Второе решение (после комментария о необходимости наличия рекурсии)
    str_number = str(number)
    first = int(str_number[0])
    if int(number) // 10 == 0:
        return first
    else:
        first = first * get_multiplied_digits(int(str_number[1:]))
        return first

print(get_multiplied_digits(40203))
print(get_multiplied_digits(123456))
