# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = l1, l2
        carry = 0
        result = ListNode(0)
        c = result
        while c1 or c2 or carry:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0

            s = v1 + v2 + carry

            if (s >= 10):
                carry = 1
                s -= 10
            else:
                carry = 0

            c.next = ListNode(s)
            c = c.next

            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next

        return result.next