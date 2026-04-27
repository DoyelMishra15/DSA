# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = lenB = 0
        temp = headA
        while temp:
            lenA += 1
            temp = temp.next
        temp = headB
        while temp:
            lenB += 1
            temp = temp.next
        h1, h2 = headA, headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                h1 = h1.next
        else:
            for _ in range(lenB - lenA):
                h2 = h2.next
        while h1 and h2:
            if h1 == h2:
                return h1
            h1 = h1.next
            h2 = h2.next  
        return None
