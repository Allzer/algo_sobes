matrix = [
    [1, 2, 5],
    [4, 5, 6],
    [7, 8, 9],    
]

sum_main_diag = 0
sum_no_main_diag = 0

for i in range(len(matrix)):
    sum_main_diag += matrix[i][i]
    sum_no_main_diag += matrix[i][len(matrix[0])-1-i]

print(sum_main_diag)
print(sum_no_main_diag)
        