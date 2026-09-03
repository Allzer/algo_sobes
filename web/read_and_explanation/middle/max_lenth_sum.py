values = [4, 1, 1, 1, 4, 1, 1]
target = 3

left = 0
right = 0

max_length = 0
curent_sum = 0

while right < len(values):
    curent_sum += values[right]
    while curent_sum > target:
        curent_sum -= values[left]
        left+=1
    
    max_length = max(max_length, right-left+1)
    right += 1
print(max_length)