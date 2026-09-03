values = [1, 3, 5, 7, 9, 11, 15, 20, 25]
target = 15

left = 0
right = len(values) - 1

while left <= right:
    mid = (left + right) // 2
    if values[mid] == target:
        print(True)
        break
    elif values[mid] < target:
        left = mid + 1
    elif values[mid] > target:
        right = mid - 1
else:
    print(False)
