class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

def delAtStart(head):
  return head.next
  
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head=delAtStart(head)

while head:
  print(head.data,end="->")
  head=head.next
print("Null")
