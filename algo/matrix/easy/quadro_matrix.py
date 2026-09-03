matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

matrix = [[matrix[i][j] for i in range(len(matrix)-1, -1, -1)] for j in range(len(matrix[0]))] #Не рационально по памяти

print(matrix)