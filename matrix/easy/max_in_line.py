matrix = [
    [1, 5, 3],
    [8, 2, 6],
    [4, 9, 7]
]

max_in_line = []

for line in matrix:
    maximum = line[0]
    for num in line:
        if num > maximum:
            maximum = num
    max_in_line.append(maximum)
    
print(max_in_line)