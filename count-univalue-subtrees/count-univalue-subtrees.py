# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.count = 0
        self.helper(root)
        return self.count
    
    def helper(self,root):
        if not root:
            return True
        l = self.helper(root.left)
        r = self.helper(root.right)
        if l and r and (not root.left or root.left.val ==root.val) and (not root.right or root.right.val ==root.val):
            print("h",root.val)
            self.count+=1 
            return True
        return False