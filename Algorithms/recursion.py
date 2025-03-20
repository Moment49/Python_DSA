# def sum(numbers):
#     if not numbers:
#         return 0
#     remaining_sum = sum(numbers[1:])
#     return numbers[0] + remaining_sum


# print(sum([1,2,3,6]))


def fibonacci(pos):
    if pos <= 1:
        return pos
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)



x = fibonacci(6)
print(x)