# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        Fast = Slow = dummy

        for i in range(n + 1):
            Fast = Fast.next

        while Fast:
            Fast = Fast.next
            Slow = Slow.next

        Slow.next = Slow.next.next
        return dummy.next


        