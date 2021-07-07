# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root,None,None)
    def helper(self,root,maxv,minv):
        if not root:
            return True
        else:
            if minv!=None and minv>=root.val:
                return False
            if maxv!=None and maxv<=root.val:
                return False
        return self.helper(root.left,root.val,minv) and  self.helper(root.right,maxv,root.val)