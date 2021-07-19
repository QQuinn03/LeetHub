# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float("inf")
        self.helper(root)
        return self.res
    
    def helper(self,root):
        if not root:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        print(l+r+root.val)
        self.res = max(self.res,l+r+root.val)
        if root.val + max(l,r)>0:
            return root.val+max(l,r)
        
        return 0