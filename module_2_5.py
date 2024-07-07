def get_matrix(n = 1, m = 1, value = None):
    matrix = []
    for i in range(n):
        line = []
        for i in range(m):
            line.append(value)
        matrix.append(line)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)