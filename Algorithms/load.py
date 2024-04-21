def load_numbers(filename):
    nums = []
    with open(filename) as f:
        for line in f:
            nums.append(int(line.strip()))
    return nums
