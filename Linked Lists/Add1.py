class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head

    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next

    return head


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("NULL")

def solve(head):
  s=""
  
  curr = head
  while curr:
    s=s+str(curr.val)
    curr = curr.next
    
  s=int(s)+1
  s=str(s)
  
  dummy=ListNode(int(s[0]))
  curr = dummy
  
  for i in range(1, len(s)):
    curr.next=ListNode(int(s[i]))
    curr=curr.next
  print_linked_list(dummy)


arr = [1, 2, 0, 1, 0, 2]

head = create_linked_list(arr)

print("Linked List:")
solve(head)
