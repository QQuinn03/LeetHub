# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.helper(root)
    
    def helper(self,root):
        if not root:
            return 0
        return 1+max(self.helper(root.left),self.helper(root.right))