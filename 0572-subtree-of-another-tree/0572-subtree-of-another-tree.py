# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node1 , node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return dfs(node1.left , node2.left) and dfs(node1.right , node2.right)

        if not root:
            return False

        if dfs(root , subRoot):
            return True
        return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)



        