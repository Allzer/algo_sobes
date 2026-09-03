matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for line in matrix:
    for num in line:
        total += num
print(total)