arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(3):
    for y in range(len(arr)-i-1):
        if arr[y] < arr[y+1]:
            arr[y], arr[y+1] = arr[y+1], arr[y]

print(arr) #[-3:]