class Solution:
    def detectCycle(self, head):
        slow = fast = head


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return 0  


        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next


        cnt = 1
        temp = start.next
        while temp != start:
            cnt += 1
            temp = temp.next

        return cnt
