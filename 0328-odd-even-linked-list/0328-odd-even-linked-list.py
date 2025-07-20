# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        Slow = head
        Fast = head.next
        prev = Fast
        while Fast and Fast.next:
            Slow.next = Fast.next
            Slow = Slow.next

            Fast.next = Slow.next
            Fast = Fast.next
        Slow.next = prev
        return head

        