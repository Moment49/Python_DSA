from linkedlist import LinkedList
 
def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    Recursively divide the linked list into sublist containing a single node
    Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list
    """
    if linked_list.size_n() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)   
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size_n()
        mid = size//2

        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half
    

def merge(left, right):
    """"
    Merges two linked lists, sorting by data in nodes
    Returns a new, merged list
    """
    merged = LinkedList()
    # Add a fake head that is discarded later
    merged.add(0)
    # Set current to the head of the linked list
    current = merged.head
    # Obtain the head nodes for each sublinked list
    left_head = left.head
    right_head = right.head
    # Iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        # if the head node of left is None, we're past the tail
        if left_head == None:
            current.next_node = right_head
            # Call next on right to set loop cond to False
            right_head = right_head.next_node
            # if the head node of right is None, we're past the tail
            # Add the tail node from left to metged linked list
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            # Not at either tail or head node
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node

    head = merged.head.next_node
    merged.head = head

    return merged




   
l = LinkedList()

l.add(10)
l.add(104)
l.add(102)
l.add(56)
l.add(567)
l.add(109)

print(l)
sorted_linkedlist = merge_sort(l)
print(sorted_linkedlist)