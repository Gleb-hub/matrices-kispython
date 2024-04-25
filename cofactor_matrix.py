from cofactor import cofactor


def cofactor_matrix(matrix):
    n = len(matrix)
    cofactor_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(cofactor(matrix, i, j))
        cofactor_matrix.append(row)
    return cofactor_matrix


if __name__ == '__main__':
    matrix = [
        [0, 2, 1, 4],
        [1, 0, 3, 2],
        [0, 1, 4, 0],
        [1, 2, 1, 1]
    ]
    cofactor_matrix = cofactor_matrix(matrix)
    print("Матрица алгебраических дополнений:")
    for row in cofactor_matrix:
        print(row)
