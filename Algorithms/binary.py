def binary_search(input_array, value):
    """Your code goes here."""
    last = len(input_array) - 1
    first = 0
    if len(input_array) == 0:
            print("Sorry array is emtpy")
    
    while first <= last:
        arr_avg = (first + last) // 2
        if input_array[arr_avg] ==  value:
            print('found the number')
            break
        elif input_array[arr_avg] > value:
            last = arr_avg - 1
        elif input_array[arr_avg] < value:
            first = arr_avg + 1       
    return -1

# test_list = [1,3,9,11,15,19,29]
test_list =[]
test_val1 = 19
test_val2 = 15
print(binary_search(test_list, test_val1))
# print(binary_search(test_list, test_val2))