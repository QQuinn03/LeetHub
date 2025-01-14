# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x = y = pred = None
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 
            root = stack.pop()
            
            if pred and root.val <pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    break
            pred = root
            root = root.right 
            
        x.val,y.val = y.val,x.val     