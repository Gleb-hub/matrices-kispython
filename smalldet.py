def smalldet(matrix):
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return determinant


if __name__ == '__main__':
    matrix = [
        [4, 3],
        [1, 1]
    ]
    det = smalldet(matrix)
    print(det)
