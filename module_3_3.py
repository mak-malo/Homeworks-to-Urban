def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print('\n------------------1.Функция с параметрами по умолчанию:------------------')
print_params(*['a', 'b', 'c'])
print_params("param_a", b = 'param_b', **{'c': 'param_c'})
print_params(b = 25)
print_params(c = [1,2,3])

print('\n------------------2.Распаковка параметров:------------------')
values_list = [52.9, '52.9', {'num_in_list': 52.9}]
values_dict = {'a': 1616.4, 'b': '1616.4', 'c': {'num_in_dict': 1616.4}}
print_params(*values_list)
print_params(**values_dict)

print('\n------------------3. РАспаковка + отдельные параметры:------------------')
value_list_2 = [('anything', 'something', 'anysome'), 90]
print_params(*value_list_2, 42)