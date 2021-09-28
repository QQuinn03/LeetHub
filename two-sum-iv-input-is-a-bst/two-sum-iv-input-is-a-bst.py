# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        check = []
        return self.helper(root,k,check)
        print(check)
    def helper(self,root,k,check):
        if not root:
            return
        if root.val in check:
            return True
        check.append(k-root.val)   
        l=self.helper(root.left,k,check)
        r=self.helper(root.right,k,check)
        return l or r 
      
        
        
        