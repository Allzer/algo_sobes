arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def three_min(arr):
    mins = arr[:3]

    if mins[0] > mins[1]:
        mins[0], mins[1] = mins[1], mins[0]

    if mins[1] > mins[2]:
        mins[1], mins[2] = mins[2], mins[1]

    if mins[0] > mins[1]:
        mins[0], mins[1] = mins[1], mins[0]
    
    for num in arr:
        if num < mins[0]:
            mins[2] = mins[1]
            mins[1] = mins[0]
            mins[0] = num

        elif num < mins[1]:
            mins[2] = mins[1]
            mins[1] = num

        elif num < mins[2]:
            mins[2] = num
    return mins

print(three_min(arr))