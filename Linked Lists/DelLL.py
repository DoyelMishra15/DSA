class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

def delAtStart(head):
  if not head:
    return None
  return head.next

def delAtEnd(head):
  if not head or not head.next:
    return None 
  
  t = head
  while t.next.next:
    t = t.next
  t.next = None
  return head

def delAtPos(pos, head):
  if not head:
    return None
  
  if pos == 1:
    return head.next
  
  t = head
  for i in range(pos - 2):
    if not t.next:
      return head  
    t = t.next
  
  if t.next:
    t.next = t.next.next
  
  return head
  
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head=delAtPos(2,head)

while head:
  print(head.data,end="->")
  head=head.next
print("Null")
