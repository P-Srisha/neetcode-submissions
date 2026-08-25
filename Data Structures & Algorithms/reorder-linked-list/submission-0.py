# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(head):
            curr = head
            prev = None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        second = slow.next
        slow.next = None

        second = reverse(second)
        first = head

        while first and second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
