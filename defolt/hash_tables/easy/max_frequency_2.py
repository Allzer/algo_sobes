nums = [1, 2, 2, 3, 1, 2]

result = {}

for num in nums:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1

print(max(result, key=result.get))