class Node:
    """"This is a class that models a simple node"""
    next_node = None
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node: {self.data}>"
    


# N1 = Node(20)
# N1.next_node = Node(30)
# print(N1)
# print(N1.next_node)

class LinkedListTry:
    """""Trying to remodel a linked list"""
    def __init__(self):
        self.head = None

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return f"<Found: {current.data}>"
            else:
                current = current.next_node
        return f"<Data not found in linked list>"
    
    

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    def __repr__(self):
        current = self.head
        Nodes_List = []
        while current != None:
            if current is self.head:
                Nodes_List.append(f"<head: {current.data}>")
            elif current.next_node == None:
                Nodes_List.append(f"<Tail: {current.data}>")
            else:
                Nodes_List.append(f"{current.data}")

            current = current.next_node
        return " --> ".join(Nodes_List)

L1 = LinkedListTry()
L1.add(10)
L1.add(20)
L1.add(40)
print(L1)

print(L1.search(20))