# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node , maxvalue):
            if not node:
                return 0
            if node.val >= maxvalue:
                good = 1
            else:
                good = 0
            maxvalue = max(maxvalue , node.val)

            good += dfs(node.left , maxvalue)
            good += dfs(node.right , maxvalue)

            return good


        return dfs(root , root.val)
        


            

        

        
                    
                
                    


        
        
            
            
        
        