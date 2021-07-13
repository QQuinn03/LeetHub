# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
  
        return self.helper(root)
    
    def helper(self,root):
        if not root:
            return 0
        if root.left and root.right:
            return 1+min(self.helper(root.left),self.helper(root.right))
        if not root.left:
             return 1+self.helper(root.right)
        if not root.right:
             return 1+self.helper(root.left)
        