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

    def remove_duplicates(self):
        temp = self.head
        
        while temp and temp.next:
            if temp.val == temp.next.val:
                nxt = temp.next
                
                temp.next = nxt.next
                if nxt.next:
                    nxt.next.prev = temp
            else:
                temp = temp.next
dll = DLL()
for x in [1,1,2,3,3,3,4]:
    dll.insert_end(x)

dll.remove_duplicates()
dll.display()
