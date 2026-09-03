arr = [1, 2, 4, 6, 8, 9, 14]
target = 13

left = 0
right = len(arr)-1

while left < right:
    if arr[left] + arr[right] < target:
        left += 1
    if arr[left] + arr[right] > target:
        right -= 1
    if arr[left] + arr[right] == target:
        print(arr[left], arr[right])
        break