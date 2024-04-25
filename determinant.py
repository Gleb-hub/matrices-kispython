from smalldet import smalldet
from submatrix import submatrix
ROW = 0


def determinant(matrix):
    n = len(matrix)
    if n == 2:
        return smalldet(matrix)
    else:
        det = 0
        for j in range(n):
            sign = (-1) ** j
            det += sign * matrix[0][j] * determinant(submatrix(matrix, ROW, j))
        return det


if __name__ == '__main__':
    matrix = [
        [0, 2, 1, 4],
        [1, 0, 3, 2],
        [0, 1, 4, 0],
        [1, 2, 1, 1]
    ]

    det = determinant(matrix)

    print("Определитель матрицы:", det)
