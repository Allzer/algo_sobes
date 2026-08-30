nums = [1, 1, 2, 3, 3]

seen = set()

for num in nums:
    if num in seen:
        print(True)
        break
    seen.add(num)