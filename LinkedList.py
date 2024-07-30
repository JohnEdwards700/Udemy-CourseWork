class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
        
    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node)
            curr_node = curr_node.next
            
    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            newNode = self.head
            newNode = self.tail
        else:
            self.tail.next = newNode
            self.tail =  newNode
        self.length += 1
        return True
        
    def pop(self):
        if self.length == 0:
            return None
        prev = self.head
        curr = self.head
        while curr.next is not None:
            prev = curr
            curr = curr.next
            
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
            
        return curr
    
    def prepend(self, value):
        newNpde = Node(value)
        if self.length == 0:
            self.head = newNpde
            self.tail = newNpde
        else:
            newNpde.next = self.head
            self.head = newNpde
        self.length += 1
        return True
        
            