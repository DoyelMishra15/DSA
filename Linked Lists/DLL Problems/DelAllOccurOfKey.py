class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new = Node(x)
        
        if not self.head:
            self.head = new
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new
        new.prev = temp

    def delete_all(self, key):
        temp = self.head
        
        while temp:
            nxt = temp.next
            
            if temp.val == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                
                if temp.next:
                    temp.next.prev = temp.prev
            
            temp = nxt

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" <-> ")
            temp = temp.next
        print("None")
        
dll = DLL()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(10)
dll.insert_end(30)
dll.insert_end(10)

dll.display()
dll.delete_all(10)
dll.display()
