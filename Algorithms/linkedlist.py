class Node:
    """An class for storing a single node of a linked list
        Models two atributes - data and the link to the next node in the list
    """   
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return f"<Node data: {self.data}>"

class LinkedList:
    """Singly linked list"""
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def size_n(self):
        """Returns the number of nodes in the list takes 0(n) time"""
        current = self.head
        count = 0
        while current != None:
            current = current.next_node
            count+=1
        return count
    
    def add(self, data):
        """Add new node containing data at head of the list. This takes constant time."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def serach(self, key):
        """""Search for the first node containng data that matches the key
            Return the node or None if not found
        """
        current = self.head

        while current != None:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            pos = index
            current = self.head

            while pos > 1:
                current = current.next_node
                pos -= 1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """"Removes the first item in the linked list if the key matches
            This takes a constant time 0(1) operations. Next check the condition to
            remove at an location in the linked list and thish takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
                return f"[removed: {self.head}]"
            elif current.data == key:
                found = True 
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            pos = 0
            
            while pos < index:
                current = current.next_node
                pos += 1
            return current

    def __repr__(self):
        nodes = []
        current = self.head

        while current != None:
            if current  is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")
            
            current = current.next_node
        return '->'.join(nodes)
    


# l = LinkedList()

# l.add(10)
# # l.add(20)
# item_rem = l.remove(16)
# print(item_rem)
# print(l)
# l.add(20)
# l.add(3)
# l.add(35)

# l.insert(45, 2) 
# print(l.size_n())
# print(l.serach(20))

# N1 = Node(10)
# L = LinkedList()
# N1 = Node(10)
# L.head = N1
# print(L.size_n())

# # print(L.head)
# # print(L.is_empty())

# # N2 = Node(20)
# # N1.next_node = N2

# # print(N1.next_node)