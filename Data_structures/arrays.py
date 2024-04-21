new_list = [1, 2, 3]
result = new_list[0]

# if 1 in new_list:print(True)

for n in new_list:
    if n == 1:
        print(True)
        
nums = []
nums.append(2)
nums.append(200)

# extends
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

nums1.extend(nums2)

print(nums1)