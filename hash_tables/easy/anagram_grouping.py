strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = {}

for i in range(len(strs)):
    anogram = "".join(sorted(strs[i]))

    if anogram in result:
        result[anogram].append(strs[i])
    else:
        result[anogram] = [strs[i]]

print(result)