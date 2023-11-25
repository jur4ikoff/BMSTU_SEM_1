def rotate_square_matrix(matrix):
    """Повернуть нечетные квадраты на 90 градусов"""
    n = len(matrix)
    for i in range(0, n, 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
    return matrix


def rotate_right(mat: list):
    return list(zip(*mat[::-1]))


def rotate_left(mat: list):
    return tuple(zip(*mat))[::-1]

