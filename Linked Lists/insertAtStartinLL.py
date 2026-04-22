class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

def insertAtStart(data,head):
  n=Node(data)
  n.next=head
  return n
  
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head=insertAtStart(7,head)

while head:
  print(head.data,end="->")
  head=head.next
print("Null")
