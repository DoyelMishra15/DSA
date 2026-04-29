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

    def find_pairs(self, k):
        res = []
        
        l = self.head
        r = self.head
        
        # move r to last
        while r and r.next:
            r = r.next
        
        while l and r and l != r and r.next != l:
            s = l.val + r.val
            
            if s == k:
                res.append((l.val, r.val))
                l = l.next
                r = r.prev
            elif s < k:
                l = l.next
            else:
                r = r.prev
        
        return res
        
dll = DLL()
for x in [1,2,3,4,5,6,7]:
    dll.insert_end(x)

print(dll.find_pairs(8))
