nums1 = [1, 2, 2, 3, 4]
nums2 = [2, 2, 4, 5]

nums1_set = set(nums1)
nums2_set = set(nums2)

result = nums1_set & nums2_set
print(result)