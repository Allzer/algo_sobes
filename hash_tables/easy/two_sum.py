nums = [3, 7, 6, 15]
target = 10

bufer = {}

for i, num in enumerate(nums):
    target_num_in_nums = target - num
    
    if target_num_in_nums in bufer:
        print([bufer[target_num_in_nums], i])
        break
    
    bufer[num] = i