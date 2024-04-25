from minor import minor


def cofactor(matrix, i, j):
    min = minor(matrix, i, j)
    sign = (-1) ** (i + j)
    cofactor = sign * min
    return cofactor


if __name__ == '__main__':
    matrix = [
        [0, 2, 1, 4],
        [1, 0, 3, 2],
        [0, 1, 4, 0],
        [1, 2, 1, 1]
    ]

    cofactor = cofactor(matrix, 0, 0)

    print("Алгебраическое дополнение:", cofactor)
