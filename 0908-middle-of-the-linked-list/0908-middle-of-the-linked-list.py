# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Fast , Slow = head,head
        while Fast and Fast.next:
            Fast = Fast.next.next
            Slow = Slow.next

        return Slow
        