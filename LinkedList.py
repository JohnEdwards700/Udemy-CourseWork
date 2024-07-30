class Node:
    
    def __init__(self, value):
        node = value
        node.next = None
        
class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1