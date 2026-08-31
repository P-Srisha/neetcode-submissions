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
        while c1 and c2:
            s = c1.val + c2.val + carry
            
            if s >= 10:
                carry = 1
                c.next = ListNode(s - 10)
            else:
                carry = 0
                c.next = ListNode(s)
            c1 = c1.next
            c2 = c2.next
            c = c.next
            
        while c1:
            s = c1.val + carry
            if s >= 10:
                carry = 1
                c.next = ListNode(s - 10)
            else:
                carry = 0
                c.next = ListNode(s)
            c = c.next
            c1 = c1.next
        while c2:
            s = c2.val + carry
            if s >= 10:
                carry = 1
                c.next = ListNode(s - 10)
            else:
                carry = 0
                c.next = ListNode(s)
            c = c.next
            c2 = c2.next

        if carry:
            c.next = ListNode(carry)
            
        return result.next