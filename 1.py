def sum_matrices(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        res.append(row)
    return res


if __name__ == '__main__':
    a = [
        [0, 2],
        [3, 0]
    ]
    b = [
        [1, 4],
        [2, 0]
    ]

    result_matrix = sum_matrices(a, b)
    print(result_matrix)
