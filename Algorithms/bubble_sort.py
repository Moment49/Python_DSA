def bubble_sort(nums):
    for i in range(len(nums)):
        swapped = False
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],  nums[j+1] = nums[j+1], nums[j]
            swapped = True
        if not swapped:
            break




nums_list = [3, 2, 1, 4, 5, 0]
print(nums_list)
bubble_sort(nums_list)
print(nums_list)
