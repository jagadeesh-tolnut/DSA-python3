# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        t, h = dummy, head
        for i in range(n):
            h = h.next

        while h:
            t = t.next
            h = h.next

        t.next = t.next.next

        return dummy.next

