new_list = [1, 2, 3]
result = new_list[0]

# if 1 in new_list:print(True)

# for n in new_list:
#     if n == 1:
#         print(True)
        
# nums = []
# nums.append(2)
# nums.append(200)

# # extends
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# nums1.extend(nums2)

# print(nums1)

# Reserve an array
def reverseArray(a):
    # Write your code here
    arr_end = len(a) - 1
    i = 0
    new_arr = []
    while arr_end >= i:
        new_arr.append(a[arr_end])
        arr_end = arr_end-1
    return new_arr

# 
def rotateLeft(d, arr):
    # Write your code here
    temp = []
    i = 0
    while i < d:
        temp.append(arr[i])
        i = i+1
        arr[i:]
    temp = arr[i:] + temp
    print(temp)
       
        
            
a = [1, 2, 3, 4]
rotateLeft(2, a)


ar = reverseArray(a)
