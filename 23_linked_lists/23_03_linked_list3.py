class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    # initializes any future objects as tail (next is None)

class LinkedList:
    def __init__(self):     # required to know head for ll (linked list)
        self.head = None    # initializes any future objects head as None
    
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            # sets 1st node as head
            print("Head Node created:", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next
            # traverses nodes and sets last node as tail

        node.next = new_node
        print("Appended new Node with value:", node.next.value)

llist = LinkedList()
llist.append("First Node")  # Head Node created: First Node
llist.append("Second Node") # Appended new Node with value: Second Node
llist.append("Third Node")  # Appended new Node with value: Third Node

print(llist)                # <__main__.LinkedList object at 0x10c84ea90>