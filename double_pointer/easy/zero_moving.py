nums = [0, 1, 0, 3, 12]

slow = 0

for fast in range(1, len(nums)):
    if nums[fast] != 0:
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow+=1
print(nums)