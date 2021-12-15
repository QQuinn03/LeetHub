# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max=float("-inf")
        self.helper(root)
        return self.max
    
    def helper(self,root):
        if not root:
            return 0
        l=max(self.helper(root.left),0)
        r=max(self.helper(root.right),0)
        curmax=l+r+root.val
        self.max=max(self.max,curmax)
        
        return root.val+(max(l,r))
  
        
        
