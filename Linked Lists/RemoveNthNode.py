# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = q = head
        for _ in range(n):
            q = q.next
        if not q:
            return head.next
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        return head
