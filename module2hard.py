def find_password(number):
    password = []
    for num_1 in range(1, int(number/2)):
        for num_2 in range(num_1 + 1, number):
            if number % (num_1 + num_2) == 0:
                password.append(str(num_1))
                password.append(str(num_2))
    return ''.join(password)

pw = find_password(int(input('Введите число из первой ячейки, которое нужно проверить: ')))
print(pw)