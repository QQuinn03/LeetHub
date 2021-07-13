# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        l=self.flatten(root.left)
        r = self.flatten(root.right)
        
        if l:
            root.right =l
            while l and l.right:
                l = l.right
            l.right =r
            root.left = None
        return root    