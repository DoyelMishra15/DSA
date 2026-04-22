class Node:
  def __init__(self,data):
    self.data=data
    self.prev=None
    self.next=None


def reverseAtStart(head):
  if head is None or head.next is None:
    return head

  curr = head

  while curr:
    curr.prev, curr.next = curr.next, curr.prev
    head = curr
    curr = curr.prev

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
head=reverseAtStart(head)
print(head.data)
