#Найти индекс первой 2

values=[0, 1, 1, 2, 3, 4]
target = 2

left = 0
right = len(values) - 1
answer = -1

while left <= right:
    mid = (left+right) // 2
    
    if values[mid] == target:
        right = mid-1
        answer = mid
    elif values[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
        
print(answer)