matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
print(matrix)