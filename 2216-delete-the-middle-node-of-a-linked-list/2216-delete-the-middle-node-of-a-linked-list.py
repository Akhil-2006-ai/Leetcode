# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0,head)
        Slow = dummy
        Fast = head
        while Fast and Fast.next:
            Fast = Fast.next.next
            Slow = Slow.next
        Slow.next = Slow.next.next
        return dummy.next
        