def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix_m = []
        for i in range(m):
            matrix_m.append(value)
        matrix.append(matrix_m)
    return matrix


print(get_matrix(int(input('Введите количество строк: ')), int(input('Введите количество столбцов: '))
                 , int(input('Введите число: '))))