# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preorder(node):
            if not node:
                return []
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return res

        