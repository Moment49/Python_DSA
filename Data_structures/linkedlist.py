class Node:
    """This is a class that models a simple node"""
    def __init__(self, data):
        self.data = data
        self.next_node = None
    
    def __repr__(self):
        return f"<Node: {self.data}>"

class LinkedList:
    """This is a class that models the linked list"""

    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        new_node = Node(new_element)
        current_node = self.head
        if self.head:
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
        else:
            self.head = new_node
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        pos = 1
        while current is not None and pos <= position:
            if pos == position:
                print(f"The data in position {position}: {current.data}")
                return current 
            current = current.next_node
            pos+= 1

        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # new_node = Node(new_element)
        current_node = self.head
        pos = 1
        while current_node is not None and pos < position - 1:
            current_node = current_node.next_node
            pos+=1
        new_element.next_node = current_node.next_node
        current_node.next_node = new_element
        return new_element
    
    def delete(self, value):
        """Delete the first node with a given value."""
        if self.head and self.head.data == value:
            print(f"Deleting head node: {self.head.data}")
            self.head = self.head.next_node 
            return 
        else:
            print(f"Value {value} is not at the head. No deletion performed.")
                
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append(f"<Node: {current.data}>")
            else:
                nodes.append(f"{current.data}")
            current = current.next_node
        return (str(nodes))



e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
# ll.append(e4)

# print(ll.get_position(3).data)

# Test get_position
# Should print 3
# print(ll.head.next_node.next_node.data)

ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).data)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).data)
# Test delete
# ll.delete(2)

# # Should print 4 now
print(ll.get_position(2).data)

# # Should print 3 now
print(ll.get_position(3).data)

# Test insert



# node_1 = Node(5)
# print(node_1)
# node_2 = Node(10)
# node_3 = Node(15)
# node_1.next_node = node_2

# print(node_1.next_node)

# link_1 = LinkedList()
# link_1.append(node_1)
# link_1.append(node_2)
# link_1.append(node_3)

# print(link_1)


 



