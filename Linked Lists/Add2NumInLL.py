# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode(0)
        temp=dum
        carr=0
        while l1 and l2:
            x=l1.val+l2.val+carr
            if x>9:
                carr=x//10
            else:
                carr=0
            x=x%10
            temp.next=ListNode(x)
            temp=temp.next
            l1=l1.next
            l2=l2.next
        while l1:
            x=l1.val+carr
            if x>9:
                carr=x//10
            else:
                carr=0
            x=x%10
            temp.next=ListNode(x)
            temp=temp.next
            l1=l1.next
        while l2:
            x=l2.val+carr
            if x>9:
                carr=x//10
            else:
                carr=0
            x=x%10
            temp.next=ListNode(x)
            temp=temp.next
            l2=l2.next
        if carr>0:
            temp.next=ListNode(carr)
            temp=temp.next
        temp.next=None
        return dum.next
