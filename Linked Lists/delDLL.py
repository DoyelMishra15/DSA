class Node:
  def __init__(self,data):
    self.data=data
    self.prev=None
    self.next=None

def delAtStart(head):
  if head==None:
    return None
  elif not head.next:
    return head
  head=head.next
  head.prev=None
  return head

head = Node(1)

# Node 2
n2 = Node(2)
head.next = n2
n2.prev = head

# Node 3
n3 = Node(3)
n2.next = n3
n3.prev = n2

# Node 4
n4 = Node(4)
n3.next = n4
n4.prev = n3
print(head.data)
head=delAtStart(head)
print(head.data)
