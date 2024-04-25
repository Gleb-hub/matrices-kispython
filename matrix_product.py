def matrix_product(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            val = 0
            for k in range(len(b)):
                val += a[i][k] * b[k][j]
            row.append(val)
        res.append(row)
    return res


if __name__ == '__main__':
    a = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    b = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    result_matrix = matrix_product(a, b)
    print(result_matrix)
