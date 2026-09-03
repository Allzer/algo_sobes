nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]

slow = 0

for fast in range(1, len(nums)):    
    if nums[fast] != nums[slow]:
        slow += 1
        nums[slow] = nums[fast]
slow += 1
del nums[slow:]
print(nums, slow)
