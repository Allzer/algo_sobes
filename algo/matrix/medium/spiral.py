matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
]

result = []
top, bottom = 0, len(matrix) - 1
left, right = 0, len(matrix[0]) - 1

while top <= bottom and left <= right:
    # 1. Двигаемся слева направо по верхней строке
    for col in range(left, right + 1):
        result.append(matrix[top][col])
    top += 1
    
    # 2. Двигаемся сверху вниз по правому столбцу
    for row in range(top, bottom + 1):
        result.append(matrix[row][right])
    right -= 1
    
    # 3. Двигаемся справа налево по нижней строке (если она осталась)
    if top <= bottom:
        for col in range(right, left - 1, -1):
            result.append(matrix[bottom][col])
        bottom -= 1
        
    # 4. Двигаемся снизу вверх по левому столбцу (если он остался)
    if left <= right:
        for row in range(bottom, top - 1, -1):
            result.append(matrix[row][left])
        left += 1

print(result)