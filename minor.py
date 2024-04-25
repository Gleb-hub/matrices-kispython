from smalldet import smalldet
from submatrix import submatrix
from determinant import determinant


def minor(matrix, i, j):
    minor = submatrix(matrix, i, j)
    minor_det = determinant(minor)
    return minor_det


if __name__ == '__main__':
    matrix = [
        [0, 2, 1, 4],
        [1, 0, 3, 2],
        [0, 1, 4, 0],
        [1, 2, 1, 1]
    ]

    minor = minor(matrix, 0, 0)

    print("Определитель минора:", minor)