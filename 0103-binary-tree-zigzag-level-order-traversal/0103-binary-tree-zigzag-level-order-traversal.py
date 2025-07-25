# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        queue = deque()
        if not root:
            return []

        if root:
            queue.append(root)
        
        res = []
        left_to_right = True
        while len(queue) > 0:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            if not left_to_right:
                level.reverse()

            res.append(level)
            left_to_right = not left_to_right
        return res

            



            


        