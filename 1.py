

def sum_matrices(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        res.append(row)

    return res


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8, 9], [10, 11, 12]]
    result_matrix = sum_matrices(a, b)
    print(result_matrix)