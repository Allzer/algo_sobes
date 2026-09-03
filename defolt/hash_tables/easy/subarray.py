nums = [1, 2, 3, 2, 1]
target = 3

left = 0
total = 0

for right in range(len(nums)):
    total += nums[right]

    while total > target:
        total -= nums[left]
        left += 1

    if total == target:
        print([left, right])
        break
else:
    print([-1, -1])