class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(node):
            if not node:
                return 0
            left = balanced(node.left)
            if left == -1:
                return -1
            right  = balanced(node.right)
            if right == -1:
                return -1


            if abs(left - right) > 1:
                return -1
            return 1 + max(left,right)

        return balanced(root) != -1

            
