import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])
def merge_sort(list):
    """"Sorts a list in ascending order
    returns a new sorted list

    divide: Find the midpoint of the  list and divide into sublists
    conquer: Recursively sort the sublists created in previous step
    combine: Merge the sorted sublists created in previous step
    """
    if len(list) <= 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """"
    divide: Find the midpoint of the  list and divide into sublists
    Returns the unsorted list at midpoint into sublists
    """
    midpoint = len(list)//2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right

def merge(left, right):
    """This functions merges two lists and sorting them in the process
        Returns a new merged list
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i = i+1
        else:
            l.append(right[j])
            j+=1
    
    while i < len(left):
        l.append(left[i])
        i+=1
        
    while j < len(right):
        l.append(right[j])
        j+=1

    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [23,38, 88, 103, 12, 43, 77, 3, 8, 1, 4, 54, 84]

# print(verify_sorted(alist))
l = merge_sort(numbers)
# print(verify_sorted(l))
print(l)
# nlist = [20, 9, 8]
# mid = len(nlist)//2
# print(mid)







# def square_nums(nums):
#     """Squares nums and then adds them"""
#     count = 0
#     for num in range(nums+1):
#         square = num**2
#         count += square
#     return count


# square_count = square_nums(10)
# print(square_count)