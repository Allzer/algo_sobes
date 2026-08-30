# nums = [1, 2, 3, 4, 5, 6]

# slow = 0

# for fast in range(len(nums)-1, -1, -1):
#     nums[slow], nums[fast] = nums[fast], nums[slow]
#     slow += 1
#     if slow > fast:
#         break
    
# print(nums)

#Более традиционный вариант

nums = [1, 2, 3, 4, 5, 6]

left = 0
right = len(nums) - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]

    left += 1
    right -= 1

print(nums)