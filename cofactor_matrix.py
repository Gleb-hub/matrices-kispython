def cofactor_matrix(matrix):
    n = len(matrix)
    cofactor_matrix = []
    # Проходим по каждому элементу матрицы
    for i in range(n):
        row = []
        for j in range(n):
            # Вычисляем алгебраическое дополнение для каждого элемента
            row.append(cofactor(matrix, i, j))
        cofactor_matrix.append(row)
    return cofactor_matrix
