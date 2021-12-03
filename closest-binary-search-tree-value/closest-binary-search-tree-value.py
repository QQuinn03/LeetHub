# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.res=None
        self.diff=float("inf")
        self.helper(root,target)
        return self.res
    
    def helper(self,root,target):
        if not root:
            return 0
        if abs(root.val-target)<self.diff:
            self.res=root.val
            self.diff=abs(root.val-target)
        self.helper(root.left,target)
        self.helper(root.right,target)
        