#  Binary Search Algorithm
def recursive_binary_serach(list, target):
   if len(list) == 0:
    return False
   else:
    midpoint = (len(list)) // 2
    if list[midpoint] == target:
        return True
    else:
        if midpoint < target:
            return recursive_binary_serach(list[midpoint+1:], target)
        elif midpoint > target:
            return recursive_binary_serach(list[:midpoint], target)
    



def verify(result):
    print("Target found:", result)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# result = recursive_binary_serach(nums, 3)
# verify(result)

def bit_serach(list, target):
   """"Set the boundaries of the serach"""
   first_pos = 0
   last_pos = len(list) - 1

   while first_pos <= last_pos:
    midpoint = (first_pos + last_pos) // 2
    print(midpoint)

    if list[midpoint] == target:
        print("Target found", midpoint)
        break
    elif list[midpoint] < target:
         first_pos = midpoint + 1
        
    elif list[midpoint] > target:
         last_pos = midpoint - 1
      



games = ['tennis', 'soccer', 'golf', 'basketball', 'gym', 'match', 'club']
games.sort()
print(games)

bit_serach(games, 'golf')











