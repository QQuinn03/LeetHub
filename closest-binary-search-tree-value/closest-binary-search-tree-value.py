# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.diff=float("inf")
        self.res = None
        
        self.helper(root,target,self.res,self.diff)
        return self.res
    def helper(self,root,target,res,diff):
        if not root:
            return 
        if abs(root.val-target) <self.diff:
            self.diff = abs(root.val-target)
            self.res = root.val
        self.helper(root.right,target,res,diff)
        self.helper(root.left,target,res,diff)
        