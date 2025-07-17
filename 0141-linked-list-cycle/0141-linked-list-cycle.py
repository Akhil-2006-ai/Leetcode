# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        Fast,Slow = head,head
        while Fast and Fast.next:
            Fast = Fast.next.next
            Slow = Slow.next
            if Fast == Slow:
                return True
        return False
        