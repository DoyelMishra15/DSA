class Solution:
    def segregate(self, head):
        zeroD = ListNode(-1)
        oneD = ListNode(-1)
        twoD = ListNode(-1)

        zero = zeroD
        one = oneD
        two = twoD

        curr = head

        while curr:
            if curr.val == 0:
                zero.next = curr
                zero = zero.next
            elif curr.val == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next

        zero.next = oneD.next if oneD.next else twoD.next
        one.next = twoD.next
        two.next = None

        return zeroD.next
