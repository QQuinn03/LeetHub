from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max = -float("inf")
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.helper(root)
        return self.max
  
    def helper(self,root):
        if not root:
            return[0,0]
        lval,lcount=self.helper(root.left)
        rval,rcount=self.helper(root.right)
        
        cur_max=(lval+rval+root.val)/float(lcount+rcount+1)
        self.max=max(self.max,cur_max)
        return [lval+rval+root.val,lcount+rcount+1]
        
        
  
        
        

        
