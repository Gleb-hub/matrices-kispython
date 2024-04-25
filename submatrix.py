def submatrix(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]


if __name__ == '__main__':
    matrix = [
        [0, 2, 1],
        [1, 4, 3],
        [2, 1, 1]
    ]
    result_matrix = submatrix(matrix, 0, 1)
    print(result_matrix)
