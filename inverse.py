from cofactor_matrix import cofactor_matrix
from determinant import determinant
from transpose import transpose


def inverse(matrix):
    det = determinant(matrix)
    cofactor_matrix_A = cofactor_matrix(matrix)
    adjugate_matrix = transpose(cofactor_matrix_A)
    inverse_matrix = [[adjugate_matrix[i][j] / det for j in range(len(matrix))] for i in range(len(matrix))]
    return inverse_matrix


if __name__ == '__main__':
    matrix = [
        [0, 2, 1, 4],
        [1, 0, 3, 2],
        [0, 1, 4, 0],
        [1, 2, 1, 1]
    ]
    inverse_matrix = inverse(matrix)
    print("Обратная матрица:")
    for row in inverse_matrix:
        print(row)
