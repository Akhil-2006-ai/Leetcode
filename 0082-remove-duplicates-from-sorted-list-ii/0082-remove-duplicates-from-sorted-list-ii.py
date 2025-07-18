# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       dummy = ListNode(0,head)

       pointer = dummy

       if not head:
        return head


       while pointer and pointer.next and  pointer.next.next:
          if pointer.next.val == pointer.next.next.val:
            nextnode = pointer.next.next.next
            while nextnode and nextnode.val == pointer.next.val:
                nextnode = nextnode.next
            pointer.next = nextnode
          else:
            pointer = pointer.next
       return dummy.next


          
       
      

    


        