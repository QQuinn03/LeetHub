# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.helper(root,targetSum)
    
    def helper(self,root,target):
        if not root:
            return 
        if not root.left and not root.right and root.val ==target:
            return True
        target-=root.val
        
   
        l=self.helper(root.left,target)

        r=self.helper(root.right,target)
            
        return l or r