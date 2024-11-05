'''
Linked Lists
* Abstract data type for quick insert/delete operations
* Stores data in sequential order (NOT indexed)
* LL ordered using links from Node to Node
    - Value = “value here”
    - Next = memory address of next node
    - None = end of list
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")

print(head.value)           # 1st Node
print(head.next.value)      # 2nd Node
print(head.next.next.value) # 3rd Node