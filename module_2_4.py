numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Для проверки кода можно заменить входные данные

primes = []
not_primes = []

for num in numbers:
    if num == 1 or num == 2:
        primes.append(num)
        continue
    for i in range(2, num):
        answer = True
        if num % i == 0:
            answer = False
            break
    if answer == False:
        not_primes.append(num)
    else:
        primes.append(num)


print(f'{primes=}')
print(f'{not_primes=}')
