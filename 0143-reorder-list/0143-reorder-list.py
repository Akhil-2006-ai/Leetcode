# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        Slow , Fast = head,head.next
        while  Fast and Fast.next:
            Fast = Fast.next.next
            Slow = Slow.next

        second = Slow.next
        Slow.next= None
        
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first,second = head,prev
        while second:
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2

      


