'''
singly linked lists: only reference the next node and thus can only be traversed in one direction
doubly linked lists: points to next and previous node to traverse list forward or backward
'''

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)

        # for first node (i.e. empty list)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head Node created:", self.head.value)
            return

        # for all subsequent nodes
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Appended new Node with value:", self.tail.value)


dllist = DoublyLinkedList()
# Head Node created: First Node
dllist.append("First Node")
print(dllist.head.value)
# First Node
print(dllist.tail.value)
# Last Node

dllist.append("Second Node")
# Appended new Node with value: Second Node
print(dllist.head.value)
# First Node
print(dllist.tail.value)
# Second Node
print(dllist.head.next.value)
# Second Node
print(dllist.tail.prev.value)
# First Node

dllist.append("Third Node")
# Appended new Node with value: Third Node
print(dllist.tail.value)
# Third Node
print(dllist.tail.prev.value)
# Second Node
print(dllist.tail.prev.prev.value)
# First Node
print(dllist.head.next.next.value)
# Third Node