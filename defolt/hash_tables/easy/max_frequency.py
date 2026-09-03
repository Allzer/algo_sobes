nums = [1, 2, 2, 3, 3, 3, 4, 4, 4]
seen = {}

max_value = 11

for char in nums:
    if char not in seen: 
        seen[char] = 1
    else:
        seen[char] += 1
        
max_value = max(seen.values())
for k in seen.keys():    
    if seen[k] == max_value:
        print(k)