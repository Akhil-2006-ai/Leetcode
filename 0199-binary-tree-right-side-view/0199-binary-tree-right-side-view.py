# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        level = []
        if root:
            queue.append(root)
        while len(queue) > 0:
           rightmost = None
           for _ in range(len(queue)):
                curr = queue.popleft()
                rightmost = curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

           level.append(rightmost.val)
                    
        return level
        