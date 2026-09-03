s = "loveleetcode"
seen = {}

for char in s:
    if char not in seen: 
        seen[char] = 1
    else:
        seen[char] += 1
        
for i, char in enumerate(s):
    if seen[char] == 1:
        print(i)
        break
else:
    print(-1)
