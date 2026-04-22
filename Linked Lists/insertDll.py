class Node:
  def __init__(self,data):
    self.data=data
    self.prev=None
    self.next=None

def insertAtStart(data,head):
  nn=Node(data)
  nn.next=head
  nn.prev=None
  return nn

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
head=insertAtStart(9,head)
print(head.data)
