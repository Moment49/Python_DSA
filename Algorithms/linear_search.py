def linear_search(list, target):
    """"
    Returns the index pos of the target if Found, else returns None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i     
    return None


def verify(index):
    if index is not None:
        print("Target found at index", index)
    else:
        print("Target not found in list")

nums = list([x for x in range(1, 11)])

results = linear_search(nums, 10)
verify(results)