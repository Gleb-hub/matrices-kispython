from transpose import transpose
from inverse import inverse
from matrix_product import matrix_product


def moore_penrose(matrix):
    transposed_matrix = transpose(matrix)
    return matrix_product(inverse(matrix_product(transposed_matrix, matrix)), transposed_matrix)


if __name__ == '__main__':
    matrix = [
        [0, 2, 1, 4],
        [1, 0, 3, 2],
        [0, 1, 4, 0],
        [1, 2, 1, 1]
    ]
    moore_penrose_matrix = moore_penrose(matrix)
    print("Псевдообратная матрица Мура-Пенроуза:")
    for row in moore_penrose_matrix:
        print(row)
