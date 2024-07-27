def get_multiplied_digits(number):
    product = 1
    for i in range(len(str(number))):
        if int(number % 10) != 0:
            product *= int(number % 10)
        number /= 10
    return (product)

print(get_multiplied_digits(40203))
print(get_multiplied_digits(123456))