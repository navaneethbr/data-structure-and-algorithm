class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.next != None:
                n = n.next
            n.next = node
    
    def insert(self, data, position):
        node = Node(data)
        n = self.head
        if position==1:
            self.head = node
            node.next = n 
            
        else:
            for i in range(position-2):
                n = n.next
            t = n.next
            n.next = node
            node.next = t
            
    def delete(self, x):
        n = self.head
        if n.data==x:
            self.head=n.next
        while n.next is not None:
            if n.next.data==x:
                t = n.next.next
                n.next = t
                break
            n = n.next
        
    def printList(self):
        n = self.head
        while n != None:
            print(n.data)
            n = n.next

if __name__ == "__main__":
    o = LinkedList()
    o.append(1)
    o.append(2)
    o.append(3)
    o.append(4)
    o.append(5)
    o.insert(6, 6)
#     o.insert(3.5, 1)
    o.delete(4)
    o.delete(1)
    o.printList()