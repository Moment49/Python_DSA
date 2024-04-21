def binary(list, target):
    last = len(list) - 1
    first = 0
    while first < last:
        midpoint = (first+last)//2
        if list[midpoint] == target:
            return (f"print number found at index: {midpoint}")
            # break
        elif list[midpoint] > target:
            last = midpoint - 1
        elif list[midpoint] < target:
            first = midpoint + 1
           


alist = [1,2,3,4,5,6,7,8,9,10]
search = binary(alist, 8)
print(search)

# The Idea of Linear search
for i in range(11):
    if i == 4:
        print("Number found")
    else:
        print("Keep printing")