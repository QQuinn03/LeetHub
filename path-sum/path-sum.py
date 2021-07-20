# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return 
        return self.helper(root,targetSum)
    def helper(self,root,target):
        
        if root and not root.left and not root.right and target==root.val:
            
            return True
        if not root:
            return False
       
        target -=root.val 
        return self.helper(root.left,target) or self.helper(root.right,target)