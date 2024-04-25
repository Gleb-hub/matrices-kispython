def transpose_matrix(matrix):
    transposed_matrix = []
    for j in range(len(matrix)):
        temp_row = []
        for i in range(len(matrix[0])):
            temp_row.append(matrix[i][j])
        transposed_matrix.append(temp_row)
    return transposed_matrix


if __name__ == '__main__':
    matrix = [
        [0, 2, 1],
        [1, 0, 3],
        [0, 1, 1]
    ]
    result_matrix = transpose_matrix(matrix)
    print(result_matrix)
