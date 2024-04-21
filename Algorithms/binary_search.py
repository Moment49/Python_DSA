def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        print(midpoint)
        if list[midpoint] == target:
            print("Target found at index:", midpoint)
            break
        elif list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1   
    return None


def verify(index):
    if index is not None:
        print("Target found at index", index)
    else:
        print("Target not found in list")

nums = [1, 22, 10, 4, 5, 6, 7, 8, 9, 100 ]
binary_search(nums, 10)

