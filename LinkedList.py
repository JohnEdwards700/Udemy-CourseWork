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
    
    def pop_first(self):
        if self.length == 0:
            return None
        removed_node = self.head
        new_head = self.head.next
        self.head.next = None
        self.head = new_head
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return removed_node 
    
    def get(self, index):
        #get object at specific index and return object
        if self.length == 0:
            print("empty list: unable to return item")
            return None
        index_node = self.head
        if index == 0:
            return index_node
        count = 0
        while index_node.next is not None:
            count +=1
            if count == index:
                return index_node.next
            index_node = index_node.next
        print("error 419: index out of bounds")
        return None
    
    # Better way to write GET method
        # def get(self, index):
        # if index < 0 or index >= self.length:
        #     return None
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next
        # return temp
        
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return True
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

            